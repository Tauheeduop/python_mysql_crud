import pymysql
from contextlib import contextmanager

class StudentDB:
    def __init__(self):
        # Database connection parameters for XAMPP MySQL
        self.host = 'localhost'
        self.user = 'root'  # Default XAMPP MySQL user
        self.password = ''  # Default XAMPP MySQL password (empty)
        self.database = 'school'

    @contextmanager
    def get_db_connection(self):
        """Context manager for database connections"""
        conn = None
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4'
            )
            yield conn
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()

    def get_all_students(self):
        """Retrieve all students from the database"""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            # Using the existing students table structure from school.sql
            cursor.execute('SELECT student_id, first_name, email FROM students ORDER BY student_id')
            return cursor.fetchall()

    def add_student(self, name, email):
        """Add a new student to the database"""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            # Using the existing students table structure from school.sql
            cursor.execute('INSERT INTO students (first_name, email) VALUES (%s, %s)', (name, email))
            conn.commit()
            return cursor.lastrowid

    def delete_student(self, student_id):
        """Delete a student from the database"""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            # First delete related enrollment records
            cursor.execute('DELETE FROM enrollments WHERE student_id = %s', (student_id,))
            # Then delete the student record
            cursor.execute('DELETE FROM students WHERE student_id = %s', (student_id,))
            conn.commit()

    def get_student(self, student_id):
        """Get a specific student by ID"""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT student_id, first_name, email FROM students WHERE student_id = %s', (student_id,))
            return cursor.fetchone()

    def update_student(self, student_id, name, email):
        """Update a student's information"""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE students SET first_name = %s, email = %s WHERE student_id = %s', (name, email, student_id))
            conn.commit()