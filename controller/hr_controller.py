import os
import platform

from model.hr import hr
from view import terminal as view


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Darwin":
        os.system("clear")
    else:
        print(
            "This program cannot clear the screen in your operating system. \n It only works with Windows and Linux"
        )


def list_employees():
    employees = hr.list_employees()
    view.print_table(employees)


def add_employee():
    new_data = view.get_inputs(hr.HEADERS[1:])
    hr.add_employee(new_data)
    print("Employee added!")


def update_employee():
    list_employees()
    id = view.get_input(hr.HEADERS[0])
    values = view.get_inputs(hr.HEADERS[3:])
    hr.update_employee(id, values)
    print("Employee updated!")


def delete_employee():
    list_employees()
    id = view.get_input(hr.HEADERS[0])
    hr.delete_employee(id)
    print("Employee deleted!")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    avg_age = hr.get_average_age()
    print(f"Average age of employees is  {avg_age}")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    clearance = view.get_input(hr.HEADERS[4])
    result = hr.count_employees_with_clearance(clearance)
    print(f"There are {result} employees with clearance level: {clearance}")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = [
        "Back to main menu",
        "List employees",
        "Add new employee",
        "Update employee",
        "Remove employee",
        "Oldest and youngest employees",
        "Employees average age",
        "Employees with birthdays in the next two weeks",
        "Employees with clearance level",
        "Employee numbers by department",
    ]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != "0":
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
