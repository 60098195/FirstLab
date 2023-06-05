import unittest
import employee_management

class TestEmployeeManagement(unittest.TestCase):
    def test_add_employees(self):
        management = employee_management.EmployeeManagement()
        employee = employee_management.Employee("Jason Roy", 32, 11021, "HR")
        management.add_employee(employee)
        self.assertIn(employee, management.employees)
        
    
    def test_show_employees(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("Jason Roy", 32, 11021, "HR")
        employee2 = employee_management.Employee("Alex Hales", 34, 11001, "HR")
        employee3 = employee_management.Employee("James Anderson", 40, 10921, "IT")
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.add_employee(employee3)
        expected_output = "Name: Jason Roy, Age: 32, ID: 11021, Department: HR\nName: Alex Hales, Age: 34, ID: 11001, Department: HR\nName: James Anderson, Age: 40, ID: 10921, Department: IT\n"
        self.assertEqual(expected_output, self.get_output_string(management.show_employees))
    
    def test_show_employee(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("Jason Roy", 32, 11021, "HR")
        employee2 = employee_management.Employee("Alex Hales", 34, 11001, "HR")
        employee3 = employee_management.Employee("James Anderson", 40, 10921, "IT")
        #employee4 = employee_management.Employee("Stuart Broad", 36, 10989, "IT")
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.add_employee(employee3)
        #emp = employee4
        #self.assertIn(emp, management.employees)
        out = management.show_employee(employee2.id)
        expected_output = "Name: Alex Hales, Age: 34, ID: 11001, Department: HR"
        self.assertEqual(expected_output, out)
    
    def test_delete_employee(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("Jason Roy", 32, 11021, "HR")
        employee2 = employee_management.Employee("Alex Hales", 34, 11001, "HR")
        employee3 = employee_management.Employee("James Anderson", 40, 10921, "IT")
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.add_employee(employee3)
        management.delete_employee(11001)
        self.assertNotIn(employee2, management.employees)
    
    def get_output_string(self, func):
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            func()
        return f.getvalue()


