# Write a menu-driven Python program using a class Student
#     to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.
#
# class Student:
#     def __init__(self):
#         self.rollno = int(input("Enter roll number: "))
#         self.name = input("Enter name: ")
#         self.marks = float(input("Enter marks: "))
#
#     def display(self):
#         print("Roll No:", self.rollno)
#         print("Name:", self.name)
#         print("Marks:", self.marks)
#
# students=[]
#
# while True:
#     print("\n--- STUDENT MENU ---")
#     print("1. Add Student")
#     print("2. Update Marks")
#     print("3. Display All Student Details")
#     print("4. Search Student by Roll Number")
#     print("5. Delete Student")
#     print("6. Exit")
#
#     ch = int(input("Enter your choice: "))
#
#     # 1. Add Student
#     if ch == 1:
#         s = Student()
#         students.append(s)
#         print("Student added successfully")
#
#     # 2. Update Marks
#     elif ch == 2:
#         roll = int(input("Enter roll number: "))
#
#         for s in students:
#             if s.rollno == roll:
#                 s.marks = int(input("Enter new marks: "))
#                 print("Marks updated successfully")
#                 break
#         else:
#             print("Student not found")
#
#     # 3. Display All Students
#     elif ch==3:
#             for s in students:
#                 s.display()
#
#     # 4. Search Student
#     elif ch == 4:
#         roll = int(input("Enter roll number: "))
#
#         for s in students:
#             if s.rollno == roll:
#                 s.display()
#                 break
#         else:
#             print("Student not found")
#
#     # 5. Delete Student
#     elif ch == 5:
#         roll = int(input("Enter roll number: "))
#
#         for s in students:
#             if s.rollno == roll:
#                 students.remove(s)
#                 print("Student deleted successfully")
#                 break
#         else:
#             print("Student not found")
#
#     # 6. Exit
#     elif ch == 6:
#         print("Thank you")
#         break
#
#     else:
#         print("Invalid choice")