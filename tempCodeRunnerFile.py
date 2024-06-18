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

@app.route('/add_class', methods=['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        course_id = request.form['course_id']
        student_id = request.form['student_id']
        class_date = datetime.datetime.strptime(request.form['class_date'], '%Y-%m-%d').date()
        average_grade = float(request.form['average_grade'])
        
        query = """
            INSERT INTO class (course_id, student_id, class_date, average_grade)
            VALUES (%s, %s, %s, %s)
        """
        session.execute(query, (course_id, student_id, class_date, average_grade))
        return 'Class record added successfully!'
    return render_template('add_class.html')

@app.route('/view_table', methods=['GET', 'POST'])
def view_table():
    if request.method == 'POST':
        table_name = request.form['table_name']
        rows = session.execute(f"SELECT * FROM {table_name}")
        return render_template('view_table.html', rows=rows, table_name=table_name)
    return render_template('view_table_form.html')

if __name__ == '__main__':
    app.run(debug=True)