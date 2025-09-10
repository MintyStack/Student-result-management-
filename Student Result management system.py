# ---------------- Student Result Management System ----------------
# Author: Nandhika Sri (GitHub Project)
# ------------------------------------------------------------------

import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    mark1 INTEGER,
    mark2 INTEGER,
    mark3 INTEGER,
    total INTEGER,
    average REAL,
    grade TEXT
)
""")

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 75: return "A"
    elif avg >= 60: return "B"
    elif avg >= 40: return "C"
    else: return "F"

# Add student
def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    m1 = int(input("Enter Mark 1: "))
    m2 = int(input("Enter Mark 2: "))
    m3 = int(input("Enter Mark 3: "))

    total = m1 + m2 + m3
    avg = total / 3
    grade = calculate_grade(avg)

    cursor.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?,?)",
                   (roll, name, m1, m2, m3, total, avg, grade))
    conn.commit()
    print("✅ Student added successfully!\n")

# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n---- Student Records ----")
    for row in rows:
        print(row)
    print("-------------------------\n")

# Delete student
def delete_student():
    roll = int(input("Enter Roll No to delete: "))
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
    conn.commit()
    print("🗑️ Student deleted!\n")

# Main Menu
while True:
    print("=== Student Result Management ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")

conn.close()
