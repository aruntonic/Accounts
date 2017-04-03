import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'Accounts.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('ACCOUNTS_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
	"""Opens a new database connection if there is none yet for the
	current application context.
	"""
	print(app.config['DATABASE'])
	if not hasattr(g, 'sqlite_db'):
	    g.sqlite_db = connect_db()
	return g.sqlite_db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select *  from accounts order by type')
    accounts = cur.fetchall()
    credit = 0.0
    debit = 0.0
    sav = 0.0
    for acc in accounts:
    	if acc['type'] in ['CHECKING', 'SAVING']:
    		debit += acc['balance']
    	elif acc['type'] in ['CREDIT']:
    		credit += acc['balance']
    	elif acc['type'] in ['PERSONAL SAVING']:
    		sav += acc['balance']

    return render_template('index.html', accounts=accounts, debit=debit, credit=credit, saving=sav, holding=debit- credit, rem=debit- credit-sav)

if __name__ == '__main__':
	#init_db()
	app.run()




