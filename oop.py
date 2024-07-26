### 8. Basic Object-Oriented Programming (OOP) with Student Example

### Classes and Objects
#  **Class**: A blueprint for creating objects (a particular data structure).
#  **Object**: An instance of a class.

#### Defining a Class

class Student:
    # Class attribute
    school = "XYZ University"

    # Initializer / Instance attributes
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    # Instance method
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"

    # Another instance method
    def is_adult(self):
        return self.age >= 18


#### Creating an Object

# Creating an instance of the Student class
student1 = Student("Alice", 20, "S12345")

# Accessing attributes
print(student1.name)  # Outputs: Alice
print(student1.age)   # Outputs: 20
print(student1.student_id)  # Outputs: S12345
print(student1.school)  # Outputs: XYZ University

# Calling methods
print(student1.display_info())  # Outputs: Name: Alice, Age: 20, ID: S12345
print(student1.is_adult())  # Outputs: True


### Inheritance
#Inheritance allows a class to inherit attributes and methods from another class.

#### Defining a Subclass

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, degree):
        super().__init__(name, age, student_id)
        self.degree = degree

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, Degree: {self.degree}"


#### Creating an Object of a Subclass

grad_student = GraduateStudent("Bob", 24, "G12345", "MSc Computer Science")
print(grad_student.display_info())  # Outputs: Name: Bob, Age: 24, ID: G12345, Degree: MSc Computer Science


### Encapsulation
# Encapsulation restricts direct access to some of an object’s components,
# which can prevent the accidental modification of data.

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.__age = age  # Private attribute
        self.student_id = student_id

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Creating an object
student = Student("Alice", 20, "S12345")
print(student.name)  # Outputs: Alice
print(student.get_age())  # Outputs: 20

# Trying to access private attribute directly
# print(student.__age)  # AttributeError: 'Student' object has no attribute '__age'

# Using setter to change age
student.set_age(21)
print(student.get_age())  # Outputs: 21


### Polymorphism
# Polymorphism allows methods to do different things based on the object it is acting upon,
# even though they share the same name.

class UndergraduateStudent(Student):
    def display_info(self):
        return f"Undergraduate: {self.name}, Age: {self.age}, ID: {self.student_id}"

class GraduateStudent(Student):
    def display_info(self):
        return f"Graduate: {self.name}, Age: {self.age}, ID: {self.student_id}, Degree: {self.degree}"

# Function to demonstrate polymorphism
def print_student_info(student):
    print(student.display_info())

# Creating objects
undergrad_student = UndergraduateStudent("Charlie", 19, "U12345")
grad_student = GraduateStudent("Bob", 24, "G12345", "MSc Computer Science")

# Calling function
print_student_info(undergrad_student)  # Outputs: Undergraduate: Charlie, Age: 19, ID: U12345
print_student_info(grad_student)  # Outputs: Graduate: Bob, Age: 24, ID: G12345, Degree: MSc Computer Science


### Practical Exercises

# 1. **Class and Object Creation**
#    Create a `Student` class with attributes `name`, `age`, and `student_id`.
#    Include methods to display the student's information and check if the student is an adult.

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"

    def is_adult(self):
        return self.age >= 18

student1 = Student("Alice", 20, "S12345")
print(student1.display_info())  # Outputs: Name: Alice, Age: 20, ID: S12345
print(student1.is_adult())  # Outputs: True


# 2. **Inheritance**
#    - Create a subclass `GraduateStudent` that inherits from `Student` and adds an attribute `degree`.

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, degree):
        super().__init__(name, age, student_id)
        self.degree = degree

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, Degree: {self.degree}"

grad_student = GraduateStudent("Bob", 24, "G12345", "MSc Computer Science")
print(grad_student.display_info())  # Outputs: Name: Bob, Age: 24, ID: G12345, Degree: MSc Computer Science


# 3. **Encapsulation**
# Create a `Student` class with a private attribute `__age`. Include methods to get and set the age.

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.__age = age  # Private attribute
        self.student_id = student_id

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

student = Student("Alice", 20, "S12345")
print(student.get_age())  # Outputs: 20
student.set_age(21)
print(student.get_age())  # Outputs: 21


# 4. **Polymorphism**
#  Create two subclasses, `UndergraduateStudent` and `GraduateStudent`,
#  each with a method `display_info`. Write a function to print the student's information.

class UndergraduateStudent(Student):
    def display_info(self):
        return f"Undergraduate: {self.name}, Age: {self.age}, ID: {self.student_id}"

class GraduateStudent(Student):
    def display_info(self):
        return f"Graduate: {self.name}, Age: {self.age}, ID: {self.student_id}, Degree: {self.degree}"

# Function to demonstrate polymorphism
def print_student_info(student):
    print(student.display_info())

undergrad_student = UndergraduateStudent("Charlie", 19, "U12345")
grad_student = GraduateStudent("Bob", 24, "G12345", "MSc Computer Science")

print_student_info(undergrad_student)  # Outputs: Undergraduate: Charlie, Age: 19, ID: U12345
print_student_info(grad_student)  # Outputs: Graduate: Bob, Age: 24, ID: G12345, Degree: MSc Computer Science

