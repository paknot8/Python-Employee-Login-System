from Employee import *

class Register:
    # Initializes the Register object with local data
    def __init__(self, local_data):
        self.local_data = local_data

    # Registers a new employee
    def register_employee(self):
        username = self.get_username()
        if self.local_data.find_employee(username):
            print("Username already exists. Please choose a different username.")
            return

        password = self.get_password()
        employee_data = self.get_employee_data()
        employee = self.create_employee(username, password, employee_data)
        self.local_data.add_employee(employee)
        print("Employee registered successfully!")

    # Gets the username from the user with validation
    def get_username(self):
        while True:
            username = self.get_input("Enter your username: ", "Invalid username. Please try again.")
            if not self.local_data.find_employee(username):
                return username
            else:
                print("Username already exists. Please choose a different username.")

    # Gets the password from the user with validation
    def get_password(self):
        while True:
            password = self.get_input("Enter your password: ", "Invalid password. Please try again.")
            confirm_password = self.get_confirm_password(password)
            if password == confirm_password:
                return password
            else:
                print("Passwords do not match. Please try again.")

    # Gets the employee data from the user with validation
    def get_employee_data(self):
        first_name = self.get_input("Enter your first name: ", "Invalid first name. Please try again.")
        last_name = self.get_input("Enter your last name: ", "Invalid last name. Please try again.")
        age = self.get_positive_integer("Enter your age: ", "Invalid age. Please try again.")
        salary = self.get_positive_float("Enter your salary: ", "Invalid salary. Please try again.")
        phone_number = self.get_input("Enter your phone number: ", "Invalid phone number. Please try again.")
        email_address = self.get_input("Enter your email address: ", "Invalid email address. Please try again.")
        address = self.get_input("Enter your address: ", "Invalid address. Please try again.")
        return {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "salary": salary,
            "phone_number": phone_number,
            "email_address": email_address,
            "address": address
        }

    # Creates a new Employee object with the given data
    def create_employee(self, username, password, employee_data):
        return Employee(
            employee_data["first_name"],
            employee_data["last_name"],
            employee_data["age"],
            employee_data["salary"],
            employee_data["phone_number"],
            employee_data["email_address"],
            employee_data["address"],
            username,
            password
        )

    # Gets input from the user with validation
    def get_input(self, prompt, error_message):
        while True:
            user_input = input(prompt)
            if user_input.strip():
                return user_input
            else:
                print(error_message)

    # Gets confirm password from the user with validation
    def get_confirm_password(self, password):
        while True:
            confirm_password = input("Confirm your password: ")
            if confirm_password.strip():
                if confirm_password == password:
                    return confirm_password
                else:
                    print("Passwords do not match. Please try again.")
            else:
                print("Invalid confirm password. Please try again.")

    # Gets a positive integer input from the user with validation
    def get_positive_integer(self, prompt, error_message):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input > 0:
                    return user_input
                else:
                    print(error_message)
            except ValueError:
                print(error_message)

    # Gets a positive float input from the user with validation
    def get_positive_float(self, prompt, error_message):
        while True:
            try:
                user_input = float(input(prompt))
                if user_input > 0:
                    return user_input
                else:
                    print(error_message)
            except ValueError:
                print(error_message)