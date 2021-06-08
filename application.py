from flask import Flask, render_template, json, request, redirect

from flask_talisman import Talisman

import database.db_connector as db

import MySQLdb

# Configuration
application = Flask(__name__)
db_connection = db.connect_to_database()

# SSL Certificate Verification
csp = {
    'default-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'maxcdn.bootstrapcdn.com',
        'use.fontawesome.com'
    ]
}

Talisman(application, content_security_policy=csp)


@application.route('/', methods=('GET', 'POST'))
def root():

    return render_template("index.j2")

@application.route('/database-test-create', methods=('GET', 'POST'))
def dbCreateTest():
    """ Create a new row in table """

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
    """ Method to display test users on screen  """

    query = "SELECT * FROM UsersTest ORDER BY last_name;"

    # Execute query to display rows
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    cursor.close()

    return render_template("databaseTest.j2", Users=results)


@application.route('/<int:id>/database-test-update', methods=('GET', 'POST'))
def dbUpdateTest(id):
    """ Update a row in the Users table """

    user = getUserTest(id)

    # Get inputs from POST request and store as variables
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        # Set query to update a row based on the form inputs
        query = "UPDATE UsersTest SET first_name=%s, last_name=%s WHERE id=" + str(id)
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(first_name, last_name))
        results = cursor.fetchall()

        return redirect('/db-test')

    return render_template("databaseUpdateTest.j2", user=user)

@application.route('/<int:id>/delete', methods=('GET', 'POST'))
def dbDeleteTest(id):
    """ Delete a row in the Users table """

    # Get the employee based on employee_id
    user = getUserTest(id)

    # Set and execute the query
    query = "DELETE FROM UsersTest WHERE id = " + str(id)
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    return redirect('/db-test')

def getUserTest(id): 
    """ Helper method to get a user based on id """

    query = "SELECT * FROM UsersTest WHERE id = " + str(id)

    # Execute query to display rows
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchone()
    cursor.close()
    user = results

    return user


# run the app.
if __name__ == "__main__":
    
    application.debug = True
    application.run()