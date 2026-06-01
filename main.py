from db import conn, cursor
from student import Student

student = Student()

while True:

  print("\n===== STUDENT MANAGEMENT SYSTEM =====")
  print("1. Add Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Update Marks")
  print("5. Delete Student")
  print("6. Exit")

  choice = input("Enter choice: ")
    
  if choice == "1":

      name = input("Enter Name: ")
      roll = input("Enter Roll No: ")
      
      math = int(input("Math Marks: "))
      science = int(input("Science Marks: "))
      english = int(input("English Marks: "))
      
      total = student.calculate_total(math, science, english)
      
      percentage = student.calculate_percentage(total)
      
      grade = student.calculate_grade(percentage)
      
      query = """
      INSERT INTO students
      (name, roll_no, math_marks, science_marks, english_marks, total, percentage, grade)
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
      """
      
      values = (name, roll, math, science, english, total, percentage, grade)
      
      cursor.execute(query, values)
      conn.commit()
      
      print("Student Added Successfully!")
    
  elif choice == "2":

    query = "SELECT * FROM students"
    
    cursor.execute(query)
    
    students = cursor.fetchall()
    
    for s in students:
      print(f"ID: {s[0]}, Name: {s[1]}, Roll No: {s[2]}, Math: {s[3]}, Science: {s[4]}, English: {s[5]}, Total: {s[6]}, Percentage: {s[7]}%, Grade: {s[8]}")
      
  elif choice == "3":
    
    roll = input("Enter Roll No: ")
    
    query = "SELECT * FROM students WHERE roll_no = %s"
    
    cursor.execute(query,(roll,))
    
    result = cursor.fetchone()
    
    print(result)
    
  
  elif choice == "4":

    roll = input("Enter Roll No: ")
    subject = input("Enter Subject (math/science/english): ")
    
    marks = int(input("Enter New Marks: "))
    
    query = f"UPDATE students SET {subject}_marks = %s WHERE roll_no = %s"
    
    cursor.execute(query,(marks, roll))
    conn.commit()
    
    print("Updated Successfully!")
    
    
  elif choice == "5":

    roll = input("Enter Roll No: ")
    
    query = "DELETE FROM students WHERE roll_no = %s"
    
    cursor.execute(query,(roll,))
    
    conn.commit()
    
    print("Deleted Successfully!")
    
  
  elif choice == "6":
    print("Exiting...")
    break 
  
  
cursor.close()
conn.close()
