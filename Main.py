import sys
from Employee import *
from Login import Login
from Register import Register
from LocalData import LocalData

def StartMenu():
    print("\n")
    print("--- Welcome to the Zoo Management System ---")
    print("0. Exit App")
    print("1. Employee Login")
    print("2. Employee Register")
    print("3. View All Employees")
    print("--->>> Please make a select <<<---")

def test_local_data(local_data):
        all_employees = local_data.get_all_employees()
        for employee in all_employees:
            print(employee)

def main():
    local_data = LocalData('userData.txt')
    login_to_account = Login(local_data)
    register_new_account = Register(local_data)

    while True:
        StartMenu()
        choice = input(": ")
        print("\n")

        if choice == "0":
            sys.exit()
        elif choice == "1":
            test_local_data(local_data)
            login_to_account.login_employee()
        elif choice == "2":
            register_new_account.register_employee()
        elif choice == "3":
            print("--- All registered Employees: ---")
            test_local_data(local_data)
            print("---------------------------------")
        else:
            print("--- Invalid choice! Please select a valid option. ---")

if __name__ == "__main__":
    main()