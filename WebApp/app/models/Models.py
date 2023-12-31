from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):

    __tablename__ = "employee"
    
    email = db.Column(db.String(40), primary_key=True) # preferisco là dove possibile usare come chiave primaria una chiave naturale. L'email per sua natura non ammette duplicati, una candidata perfetta!
    firstname = db.Column(db.String(30),nullable=False)
    lastname = db.Column(db.String(30),nullable=False)
    username = db.Column(db.String(40),nullable=False)
    gender = db.Column(db.String(10),nullable=False)
    title = db.Column(db.String(30),nullable=False)
    department = db.Column(db.String(10),nullable=False)
    
    # Costruttore classe Employee
    def __init__(self,email,firstname,lastname,username,gender,title,department):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.gender = gender
        self.title = title
        self.department = department
     
    def to_dict(self):
        return {
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'gender': self.gender,
            'title':self.title,
            'department':self.department
        }

class Report(db.Model):

    __tablename__ = "report"
    
    id = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(30),nullable=False)
    description = db.Column(db.String(100),nullable=False)
    priority = db.Column(db.String(4),nullable=False)
    
    # Costruttore della classe Report
    def __init__(self,id,title,description,priority):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        
    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'priority':selfpriority
        }

# identifica relazione molti a molti tra employee e report
class Charged(db.Model):
    __tablename__ = "charged"
    employee_id = db.Column(db.String(40), db.ForeignKey('employee.email'), primary_key=True)
    report_id = db.Column(db.String(10), db.ForeignKey('report.id'), primary_key=True)
    
    # Costruttore della classe charge
    def __init__(self,report_id,employee_id):
        self.report_id = report_id
        self.employee_id = employee_id