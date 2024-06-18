from flask import Flask, request, render_template
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid
import datetime

app = Flask(__name__)

# Cassandra connection details
cassandra_host = '127.0.0.1'
keyspace_name = 'mykeyspace'

# Authentication details
username = 'cassandra'
password = 'cassandra'

# Set up authentication provider and connect to Cassandra
auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster([cassandra_host], auth_provider=auth_provider)
session = cluster.connect(keyspace_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_id = uuid.uuid4()
        course_name = request.form['course_name']
        course_description = request.form['course_description']
        course_credits = int(request.form['course_credits'])
        course_duration = request.form['course_duration']
        
        query = """
            INSERT INTO courses (course_id, course_name, course_description, course_credits, course_duration)
            VALUES (%s, %s, %s, %s, %s)
        """
        session.execute(query, (course_id, course_name, course_description, course_credits, course_duration))
        return 'Course added successfully!'
    return render_template('add_course.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = uuid.uuid4()
        student_name = request.form['student_name']
        student_email = request.form['student_email']
        gpa = float(request.form['gpa'])
        
        query = """
            INSERT INTO students (student_id, student_name, student_email, gpa)
            VALUES (%s, %s, %s, %s)
        """
        session.execute(query, (student_id, student_name, student_email, gpa))
        return 'Student added successfully!'
    return render_template('add_student.html')

@app.route('/add_degree_class', methods=['GET', 'POST'])
def add_degree_class():
    if request.method == 'POST':
        # Get values from the form
        degree_id = uuid.uuid4()
        degree_name = request.form['degree_name']
        class_name = request.form['class_name']
        class_year = request.form['class_year']
        number_of_students = int(request.form['number_of_students'])

        # Generate a unique ID for the degree
        degree_id = uuid.uuid4()
        
        # INSERT query for the new table structure
        query = """
            INSERT INTO degree_class (degree_id, degree_name, class_name, class_year, number_of_students)
            VALUES (%s, %s, %s, %s, %s)
        """
        session.execute(query, (degree_id, degree_name, class_name, class_year, number_of_students))
        return 'Degree class record added successfully!'
    
    # Render a different template for adding degree class records
    return render_template('add_degree_class.html')


@app.route('/view_table', methods=['GET', 'POST'])
def view_table():
    if request.method == 'POST':
        table_name = request.form['table_name']
        rows = session.execute(f"SELECT * FROM {table_name}")
        return render_template('view_table.html', rows=rows, table_name=table_name)
    return render_template('view_table_form.html')

if __name__ == '__main__':
    app.run(debug=True)
