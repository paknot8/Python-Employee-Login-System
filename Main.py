import sys
from Employee import *
from Login import Login
from Register import Register
from LocalData import LocalData

# Main function: entry point of the program
# Initializes local data storage, creates instances of Login and Register classes,
# and enters an infinite loop to display the start menu and process user input.
def main():
    local_data = LocalData('userData.txt')
    login_to_account = Login(local_data)
    register_new_account = Register(local_data)

    while True:
        display_start_menu()
        choice = input(": ")
        print("\n")

        if choice == "0":
            sys.exit()
        elif choice == "1":
            login_to_account.login_employee()
        elif choice == "2":
            register_new_account.register_employee()
        elif choice == "3":
            print("--- All registered Employees: ---")
            test_local_data(local_data)
            print("---------------------------------")
        else:
            print("--- Invalid choice! Please select a valid option. ---")

# Displays the start menu to the console, showing available options to the user.
def display_start_menu():
    print("\n")
    print("--- Welcome to the Zoo Management System ---")
    print("0. Exit App")
    print("1. Employee Login")
    print("2. Employee Register")
    print("3. View All Employees")
    print("--->>> Please make a select <<<---")

# Tests the local data by printing out all registered employees in the system.
def test_local_data(local_data):
    for employee in local_data.get_all_employees():
        print(employee)

if __name__ == "__main__":
    main()