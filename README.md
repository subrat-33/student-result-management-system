# Student Result Management System

A console-based Student Result Management System built using Python and MySQL.
This project helps manage student records, marks, grades, and results using CRUD operations and Object-Oriented Programming concepts.

---

## Features

* Add Students
* View Student Records
* Search Students
* Update Student Marks
* Delete Student Records
* Calculate Total Marks
* Calculate Percentage
* Generate Grades

---

## Technologies Used

* Python
* MySQL
* mysql-connector-python
* OOP Concepts
* SQL CRUD Operations

---

## Project Structure

```bash
student-result-system/
│
├── main.py
├── db.py
├── student.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
```

---

## Database Setup

### Create Database

```sql
CREATE DATABASE student_management;
```

### Use Database

```sql
USE student_management;
```

### Create Table

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(20),
    math_marks INT,
    science_marks INT,
    english_marks INT,
    total INT,
    percentage FLOAT,
    grade VARCHAR(5)
);
```

---

## Installation

Clone the repository:

```bash
git clone MY_REPOSITORY_LINK
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and add:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=student_management
```

---

## Run the Project

```bash
python main.py
```

---

## Concepts Learned

* Python Programming
* MySQL Database Integration
* CRUD Operations
* Object-Oriented Programming
* Environment Variables
* Git & GitHub Workflow

---

## Future Improvements

* GUI using Tkinter
* Authentication System
* Student Ranking System
* Charts & Analytics
* Web Version using Flask or Streamlit

---

## Author

Subrat Mallick
