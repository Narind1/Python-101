class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

emp1 = Employee("John Doe", 10000)
emp1.print_details()
