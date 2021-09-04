from model import data_manager, util
from datetime import date

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def list_employees():
    employees = [HEADERS]
    employees.extend(data_manager.read_table_from_file(DATAFILE))

    return employees


def add_employee(new_employee):
    id = util.generate_id()
    new_employee.insert(0, id)
    employees = data_manager.read_table_from_file(DATAFILE)
    employees.append(new_employee)
    data_manager.write_table_to_file(DATAFILE, employees)


def update_employee(id, values):
    employees_list = data_manager.read_table_from_file(DATAFILE)
    for employee in employees_list:
        if employee[0] == id:
            employee[3] = values[0]
            employee[4] = values[1]

    data_manager.write_table_to_file(DATAFILE, employees_list)


def delete_employee(id):
    list_employees()
    employees = data_manager.read_table_from_file(DATAFILE)
    ids = []

    for x in employees:
        ids.append(x[0])

    for line in employees:
        if id in line:
            employees.remove(line)

    data_manager.write_table_to_file(DATAFILE, employees)


def calculate_age(birth_date):
    year, month, day = [int(_ for _ in birth_date.split("-"))]
    birth_date = date(year, month, day)
    today = date.today
    years = today.year - birth_date.year
    return years


def get_average_age():
    employees = data_manager.read_table_from_file(DATAFILE)
    for employee in employees:
        avg_employee_age = sum(calculate_age(employee[2])) / len(employees)
    return avg_employee_age


def next_birthdays():
    pass


def count_employees_with_clearance(clearance):
    employees = data_manager.read_table_from_file(DATAFILE)
    clearance_levels = []
    result = 0
    for _ in employees:
        clearance_levels.append(_[4])
        print(clearance_levels)
    for i in clearance_levels:
        if i == clearance:
            result += 1

    return result


def count_employees_per_department(departament):
    employees = data_manager.read_table_from_file(DATAFILE)
    departments = []
    result = 0
    for _ in employees:
        departament.append(_[3])
    for i in departments:
        if i == departament:
            result += 1

    return result
