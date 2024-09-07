import sys
from Employee import *
from LocalData import *

class Login:
    def __init__(self, local_data):
        # Initialize the Login object with local data
        self.local_data = local_data

    def login_employee(self):
        # Login an existing employee
        print("--- You are logging in as an existing Employee ---")
        attempts = 0

        while attempts < 3:
            username = self.get_input("Enter your username: ", "Invalid username. Please try again.")
            password = self.get_input("Enter your password: ", "Invalid password. Please try again.")

            # Check if the username and password match a registered employee
            employee = self.local_data.find_employee(username, password)
            if employee:
                print(f"Welcome, {employee['first_name']} {employee['last_name']}!")
                print(f"ID: {employee['id']}, First Name: {employee['first_name']}, Last Name: {employee['last_name']}, Age: {employee['age']}, Salary: {employee['salary']}, Phone Number: {employee['phone_number']}, Email Address: {employee['email_address']}, Address: {employee['address']}, Username: {employee['username']}")
                return

            attempts += 1
            print(f"Incorrect username or password. You have {3 - attempts} attempts left.")

        print("Exiting app due to multiple incorrect login attempts.\n")
        sys.exit()

    def get_input(self, prompt, error_message):
        # Get input from the user with validation
        while True:
            user_input = input(prompt)
            if user_input.strip():  # check if input is not empty
                return user_input
            else:
                print(error_message)