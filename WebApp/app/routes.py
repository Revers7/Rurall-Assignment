from flask import Blueprint,render_template,jsonify,request,url_for,flash,redirect
from app.models.Models import db,Employee,Report,Charged
from app.utils.versions import getAppVersion, getDBVersion
from sqlalchemy import exc

routes = Blueprint('routes', __name__, static_folder='static', template_folder='templates')

jinja_args_dict = {
    "app_name":"Company s.r.l",
    "arg":"employee",
    "static_prefix_path":"",
    "client_ver":getAppVersion(),
    "db_ver":getDBVersion(),
    "endpoint":""
}

@routes.route('/')
def isAlive():
    return jsonify({"msg":"server up!"})
    
@routes.route('/home',methods=['GET'])
def home():
    page = request.args.get('page', 1, type=int)
    employees = Employee.query.paginate(page=page, per_page=10)
    jinja_args_dict['arg'] = 'employee'
    jinja_args_dict['endpoint'] = url_for('routes.home')
    jinja_args_dict['pagination'] = employees
    print(jinja_args_dict)
    return render_template('index.html',be_variables = jinja_args_dict)
    
@routes.route('/report',methods=['GET','POST'])
def reports():
    jinja_args_dict['arg'] = 'report'
    jinja_args_dict['endpoint'] = url_for('routes.reports')
    page = request.args.get('page', 1, type=int)
    if request.method == 'GET':
        reports = Report.query.paginate(page=page, per_page=10)
        jinja_args_dict['pagination'] = reports
        return render_template('index.html',be_variables = jinja_args_dict)
    elif request.method == 'POST':
        sch_username = request.form['search-user']
        sch_priority = request.form['search-priority']
        
        if sch_username == '' and sch_priority == '':
            return redirect(url_for('routes.reports'))
        q = Report.query.paginate(page=page)
        if sch_username != '' and sch_priority != '':
            q = db.session.query(Report)\
                .join(Charged)\
                .join(Employee)\
                .filter(Employee.username == sch_username)\
                .filter(Report.priority == sch_priority)\
                .paginate(page=page)
        
        elif sch_username != '':
            q = db.session.query(Report)\
                    .join(Charged)\
                    .join(Employee)\
                    .filter(Employee.username == sch_username)\
                    .paginate(page=page)
        
        elif sch_priority != '':
            q = db.session.query(Report)\
                .join(Charged)\
                .join(Employee)\
                .filter(Report.priority == sch_priority)\
                .paginate(page=page)            

        flash(f'Search result for: username = "{sch_username}" , priority = "{sch_priority}"')
        jinja_args_dict['pagination'] = q
        return render_template('index.html',be_variables = jinja_args_dict)

@routes.route('/assign',methods=['GET'])
def assign():
    page = request.args.get('page', 1, type=int)
    charged = Charged.query.paginate(page=page, per_page=10)
    jinja_args_dict['arg'] = 'assign'
    jinja_args_dict['endpoint'] = url_for('routes.assign')
    jinja_args_dict['pagination'] = charged
    return render_template('index.html',be_variables = jinja_args_dict)
    
@routes.route('/employee/add',methods=['GET','POST'])
def empAdd():
    if request.method == 'GET':
        jinja_args_dict['arg'] = 'emp-add'
        jinja_args_dict['endpoint'] = url_for('routes.empAdd')
        print(url_for('routes.empAdd'))
        return render_template('index.html',be_variables = jinja_args_dict)
    elif request.method == 'POST':
        print(request.form)
        firstname = request.form['emp-firstname']
        lastname = request.form['emp-lastname']
        username = request.form['emp-username']
        email = request.form['emp-email']
        gender = request.form['emp-gender']
        title = request.form['emp-title']
        department = request.form['emp-department']
        employee = Employee.query.filter(Employee.email == email).first()
        if employee:
            flash('Error: User already register!')
            return redirect(url_for('routes.home'))
        employee = Employee(email,firstname,lastname,username,gender,title,department)
        db.session.add(employee)
        db.session.commit()
        flash('Success!')
        return redirect(url_for('routes.home'))
        
@routes.route('/report/add',methods=['GET','POST'])
def repAdd():
    if request.method == 'GET':
        jinja_args_dict['arg'] = 'rep-add'
        jinja_args_dict['endpoint'] = url_for('routes.repAdd')
        print(url_for('routes.repAdd'))
        return render_template('index.html',be_variables = jinja_args_dict)
    elif request.method == 'POST':
        print(request.form)
        id = request.form['rep-id']
        title = request.form['rep-title']
        description = request.form['rep-description']
        priority = request.form['rep-priority']
        report = Report.query.filter(Report.id == id).first()
        if report:
            flash('Error: Report already register!')
            return redirect(url_for('routes.home'))
        report = Report(id,title,description,priority)
        db.session.add(report)
        db.session.commit()
        flash('Success!')
        return redirect(url_for('routes.reports'))
        

@routes.route('/assign/add',methods=['GET','POST'])
def assAdd():
    if request.method == 'GET':
        employees = Employee.query.all()
        reports = Report.query.all()
        jinja_args_dict['arg'] = 'ass-add'
        jinja_args_dict['employees'] = employees
        jinja_args_dict['reports'] = reports
        jinja_args_dict['endpoint'] = url_for('routes.assign')
        print(url_for('routes.assign'))
        return render_template('index.html',be_variables = jinja_args_dict)
    elif request.method == 'POST':
        print(request.form)
        rep_id = request.form['ass-rep']
        emp_id = request.form['ass-emp']
        try:
            charged = Charged(rep_id,emp_id)
            db.session.add(charged)
            db.session.commit()
            flash('Success!')
        except exc.IntegrityError as e:
            flash(f'Error: {emp_id} already assigned to report {rep_id}')
        except Exception as e:
            flash(f'Error: {e}')
        
        return redirect(url_for('routes.assign'))