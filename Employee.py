class Employee:
    __id_counter = 0

    def __init__(self, first_name, last_name, age, salary, phone_number, email_address, address, username, password):
        Employee.__id_counter += 1
        self.__id = Employee.__id_counter
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__salary = salary
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__address = address
        self.__username = username
        self.__password = password

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_email_address(self):
        return self.__email_address

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def verify_password(self, password):
        return self.__password == password