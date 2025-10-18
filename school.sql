-- 1. Database create karna
CREATE DATABASE IF NOT EXISTS school;
USE school;

-- 2. Students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender ENUM('Male', 'Female'),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Courses table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    course_code VARCHAR(20),
    credit_hours INT
);

-- 4. Enrollments table
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- 5. Sample data insert karna
INSERT INTO students (first_name, last_name, age, gender, email) VALUES
('Ali', 'Khan', 18, 'Male', 'ali.khan@example.com'),
('Sara', 'Ahmed', 19, 'Female', 'sara.ahmed@example.com'),
('Ahmed', 'Raza', 20, 'Male', 'ahmed.raza@example.com'),
('Hina', 'Malik', 21, 'Female', 'hina.malik@example.com'),
('Usman', 'Iqbal', 22, 'Male', 'usman.iqbal@example.com');

INSERT INTO courses (course_name, course_code, credit_hours) VALUES
('Mathematics', 'MATH101', 3),
('Physics', 'PHYS101', 4),
('Chemistry', 'CHEM101', 3),
('English', 'ENG101', 2),
('Computer Science', 'CS101', 4);

INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2025-01-10'),
(1, 2, '2025-01-12'),
(2, 3, '2025-01-15'),
(2, 4, '2025-01-17'),
(3, 1, '2025-01-10'),
(3, 5, '2025-01-20'),
(4, 2, '2025-01-18'),
(5, 3, '2025-01-19'),
(5, 4, '2025-01-21');
