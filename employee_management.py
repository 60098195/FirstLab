class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        department = ["Finance", "HR", "IT", "Sales", "Marketing"]
        for e in self.employees:
            if e.id == employee.id:
                raise Exception("Employee with the same ID already exists!")
        if employee.age < 18:
            raise Exception("Employee cannot be under 18 years of age!")
        if employee.department not in department:
            raise Exception("Invalid department")
        self.employees.append(employee)

    def show_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Age: {employee.age}, ID: {employee.id}, Department: {employee.department}")

    def show_employee(self, id):
        for i, employee in enumerate(self.employees):
            if employee.id == id:
                return(f"Name: {employee.name}, Age: {employee.age}, ID: {employee.id}, Department: {employee.department}")
                break

    def delete_employee(self, id):
        for i, employee in enumerate(self.employees):
            if employee.id == id:
                del self.employees[i]
                break
        else:
            raise Exception("Employee not found")