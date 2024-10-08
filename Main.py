import sys
from Employee import *
from Login import Login
from Register import Register
from LocalData import LocalData

# Global variable to track login status
is_logged_in = False

# Initializes local data storage, creates instances of Login and Register classes,
# and enters an infinite loop to display the start menu and process user input.
def main():
    global is_logged_in

    local_data = LocalData('userData.txt') # Data is saved in a txt file.
    login_to_account = Login(local_data)

    register_new_account = Register(local_data)

    while True:
        display_start_menu()
        choice = input(": ")
        print("\n")

        if choice == "0":
            if is_logged_in:
                print("Goodbye!")
            sys.exit()
        elif choice == "1":
            is_logged_in = login_to_account.login_employee()
            if is_logged_in:
                print("You are now logged in!")
                account_logged_in()
        elif choice == "2":
            register_new_account.register_employee()
        elif choice == "3":
            if is_logged_in:
                print("--- All registered Employees: ---")
                test_local_data(local_data)
                print("---------------------------------")
            else:
                print("You need to log in to view this information.")
        else:
            print("--- Invalid choice! Please select a valid option. ---")

# Displays the start menu to the console, showing available options to the user.
def display_start_menu():
    print("\n")
    print("--- Welcome to the Admin Login System ---")
    print("0. Exit App")
    print("1. Employee Login")
    print("2. Employee Register")
    print("3. View All Employees")
    print("--->>> Please make a selection <<<---")

# Tests the local data by printing out all registered employees in the system.
def test_local_data(local_data):
    for employee in local_data.get_all_employees():
        print(employee)

# Handles the account menu after a successful login.
def account_logged_in():
    while True:
        print("You are logged in. Please select an option:")
        print("0. Logout")
        print("1. View All Employees")
        print("2. Exit App")
        choice = input(": ")
        if choice == "0":
            global is_logged_in
            is_logged_in = False
            print("You are now logged out.")
            break
        elif choice == "1":
            print("--- All registered Employees: ---")
            local_data = LocalData('userData.txt')
            test_local_data(local_data)
            print("---------------------------------")
        elif choice == "2":
            print("Goodbye!")
            sys.exit()
        else:
            print("--- Invalid choice! Please select a valid option. ---")

if __name__ == "__main__":
    main()