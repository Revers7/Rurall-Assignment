import os

from flask import Flask
basedir = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + 'db'

#  application factory function
#  1. Permette di creare più istanze della stessa app, molo utile in caso di unit test!!
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__,instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
        )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        pass#app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .routes import routes
    app.register_blueprint(routes)

    from app.models.Models import db
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    application = app
    return app