from Employee import *

class Register:
    def __init__(self, local_data):
        self.local_data = local_data

    def register_employee(self):
        username = self.get_input("Enter your username: ", "Invalid username. Please try again.")
        if self.local_data.find_employee(username):
            print("Username already exists. Please choose a different username.")
            return

        password = self.get_input("Enter your password: ", "Invalid password. Please try again.")
        confirm_password = self.get_confirm_password(password)
        first_name = self.get_input("Enter your first name: ", "Invalid first name. Please try again.")
        last_name = self.get_input("Enter your last name: ", "Invalid last name. Please try again.")
        age = self.get_positive_integer("Enter your age: ", "Invalid age. Please try again.")
        salary = self.get_positive_float("Enter your salary: ", "Invalid salary. Please try again.")
        phone_number = self.get_input("Enter your phone number: ", "Invalid phone number. Please try again.")
        email_address = self.get_input("Enter your email address: ", "Invalid email address. Please try again.")
        address = self.get_input("Enter your address: ", "Invalid address. Please try again.")

        employee = Employee(first_name, last_name, age, salary, phone_number, email_address, address, username, password)
        print(f"ID: {employee.get_id()}, First Name: {employee.get_first_name()}, Last Name: {employee.get_last_name()}, Age: {employee.get_age()}, Salary: {employee.get_salary()}, Phone Number: {employee.get_phone_number()}, Email Address: {employee.get_email_address()}, Address: {employee.get_address()}, Username: {employee.get_username()}")

        self.local_data.add_employee(employee)
        print("Employee registered successfully!")

    def get_input(self, prompt, error_message):
        while True:
            user_input = input(prompt)
            if user_input.strip():
                return user_input
            else:
                print(error_message)

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