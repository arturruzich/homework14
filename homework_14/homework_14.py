class Student:
    def __init__(self, first_name, last_name, age, average_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_mark = average_mark

    def update_average_mark(self, new_mark):
        self.average_mark = new_mark

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Average Mark: {self.average_mark}")


student = Student("Artur", "Ruzich", 23, 85.5)


student.display_info()


student.update_average_mark(90.0)


print("\nAfter changing the average mark:")
student.display_info()
