# Degree and Class Management System

This project is a web-based application for managing courses, students, and degree classes. It uses Flask as the web framework and Apache Cassandra as the database. The system allows users to add new courses, students, and degree classes, and also to view the data stored in the database.

## Features

- **Add Course**: Users can add new courses by providing details like course name, description, credits, and duration.
- **Add Student**: Users can add new students by entering their name, email, and GPA.
- **Add Degree Class**: Users can create a new degree class record by specifying the degree name, class name, class year, and number of students.
- **View Data**: Users can view data from the selected tables (Courses, Students, or Degree Classes) in a tabular format.

## Project Structure

- **App.py**: The main Flask application file that handles routing, form submissions, and database interactions.
- **Index.html**: The homepage that links to various functionalities like adding courses, students, degree classes, and viewing data.
- **Add_course.html**: The form page for adding a new course.
- **Add_student.html**: The form page for adding a new student.
- **Add_degree_class.html**: The form page for adding a new degree class.
- **View_table_form.html**: A form for selecting which table to view.
- **View_table.html**: Displays the data from the selected table.
- **Names.txt**: Contains the database schema definitions for the tables used in the system.

## Prerequisites

- **Python 3.7+**
- **Apache Cassandra**
- **Flask**

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/degree-management-system.git
   cd degree-management-system
   
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   
3. **Set up Apache Cassandra**:
   - Install Cassandra and start the service.
   - Create a keyspace and tables using the schema provided in Names.txt.

4. **Configure the application**:
   Update the Cassandra connection details (host, username, password, and keyspace) in App.py.

5. **Run the application**:
   - The application will be accessible at http://127.0.0.1:5000/.
   ```bash
   python App.py

## Usage
- Navigate to http://127.0.0.1:5000/ to access the home page.
- Use the provided links to add courses, students, or degree classes.
- View the data stored in the database by selecting the desired table.

   
