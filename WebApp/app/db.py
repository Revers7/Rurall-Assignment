import sqlite3

import click
from flask import current_app, g
from models.Models import db



def get_db():
    if 'db' not in g:
        db.init_app(current_app)
        db.create_all()
        g.db = db

    return g.db

def init_db():
    db = get_db()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()