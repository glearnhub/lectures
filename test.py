class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
 
    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age}")
 
    def update_details(self, name=None, age=None):
        if name:
            self.name = name
        if age:
            self.age = age
        return f"Record for {self.student_id} updated."
 
 
# ----- Managing multiple students -----
students = []  # empty list to hold Student objects
 
# Adding students
students.append(Student("ST001", "John Doe", 20))
students.append(Student("ST002", "Jane Smith", 22))
students.append(Student("ST003", "Ali Hassan", 19))
 
# Displaying all students
print("---- All Student Records ----")
for student in students:
    student.display_info()
 
# Updating a student's details
print("\n---- Updating ST002 ----")
students[1].update_details(name="Jane K. Smith", age=23)
students[1].display_info()
