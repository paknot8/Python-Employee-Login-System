from Employee import *

class LocalData:
    def __init__(self, filename):
        """
        Initialize the LocalData object with a filename.

        This method sets up the LocalData object with a filename and loads the employees from the file.
        """
        self.filename = filename
        self.employees = self.load_employees()

    def load_employees(self):
        """
        Load employees from a file.

        This method reads the employees from the file specified in the filename attribute and returns them as a list of dictionaries.
        Each dictionary represents an employee with their id, first name, last name, age, salary, phone number, email address, address, username, and password.
        """
        try:
            with open(self.filename, 'r') as file:
                employees = []
                for line in file:
                    employee_data = line.strip().split(',')
                    if len(employee_data) != 10:
                        raise ValueError("Invalid employee data")
                    employee = {
                        'id': int(employee_data[0]),
                        'first_name': employee_data[1],
                        'last_name': employee_data[2],
                        'age': int(employee_data[3]),
                        'salary': float(employee_data[4]),
                        'phone_number': employee_data[5],
                        'email_address': employee_data[6],
                        'address': employee_data[7],
                        'username': employee_data[8],
                        'password': employee_data[9]
                    }
                    employees.append(employee)
                return employees
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def add_employee(self, employee):
        """
        Add a new employee to the local data.

        This method adds a new employee to the list of employees and saves the updated list to the file.
        It checks if the employee object is valid before adding it to the list.
        """
        if not isinstance(employee, Employee):
            raise ValueError("Invalid employee object")
        self.employees.append({
            'id': employee.get_id(),
            'first_name': employee.get_first_name(),
            'last_name': employee.get_last_name(),
            'age': employee.get_age(),
            'salary': employee.get_salary(),
            'phone_number': employee.get_phone_number(),
            'email_address': employee.get_email_address(),
            'address': employee.get_address(),
            'username': employee.get_username(),
            'password': employee.get_password()
        })
        self.save_employees()

    def save_employees(self):
        """
        Save the employees to a file.

        This method writes the list of employees to the file specified in the filename attribute.
        It overwrites any existing data in the file.
        """
        with open(self.filename, 'w') as file:
            for employee in self.employees:
                file.write(','.join([
                    str(employee['id']),
                    employee['first_name'],
                    employee['last_name'],
                    str(employee['age']),
                    str(employee['salary']),
                    employee['phone_number'],
                    employee['email_address'],
                    employee['address'],
                    employee['username'],
                    employee['password']
                ]) + '\n')

    def find_employee(self, username, password=None):
        """
        Find an employee by username and password.

        This method searches for an employee with the specified username and password in the list of employees.
        If a password is provided, it checks if the password matches the employee's password.
        If no password is provided, it returns the employee object if the username matches.
        """
        for employee in self.employees:
            if employee['username'] == username:
                if password is not None and employee['password'] == password:
                    return employee
                elif password is None:
                    return employee
        return None

    def get_all_employees(self):
        """
        Get all employees.

        This method returns the list of all employees.
        """
        return self.employees