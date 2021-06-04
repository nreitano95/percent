from flask import Flask, render_template, json, request, redirect

from flask_talisman import Talisman

import database.db_connector as db

import MySQLdb

# Configuration
application = Flask(__name__)


csp = {
    'default-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'maxcdn.bootstrapcdn.com',
        'use.fontawesome.com'
    ]
}

Talisman(application, content_security_policy=csp)

db_connection = db.connect_to_database()

@application.route('/', methods=('GET', 'POST'))
def root():

    return render_template("index.j2")

@application.route('/database-test-create', methods=('GET', 'POST'))
def dbCreateTest():
    """ Create a new row in the Employees table """

    # Get inputs from POST request and store as variables
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        # Set query to insert a row based on the form inputs
        query = "INSERT INTO UsersTest (first_name, last_name) VALUES (%s, %s)"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(first_name, last_name))
        results = cursor.fetchall()

        return redirect('/db-test')

    return render_template("databaseCreateTest.j2")

@application.route('/db-test', methods=('GET', 'POST'))
def dbTest():

    query = "SELECT * FROM UsersTest ORDER BY last_name;"

    # Execute query to display rows
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    cursor.close()

    return render_template("databaseTest.j2", Users=results)




# run the app.
if __name__ == "__main__":
    
    application.debug = True
    application.run()