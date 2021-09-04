from model.crm import crm
from view import terminal as view
from model import data_manager


def get_customers_list():
    customers = crm.get_customers_list()
    view.print_table(customers)


def add_customer():
    new_customer = view.get_inputs(crm.HEADERS[1:])
    crm.add_customer(new_customer)
    print("Successfully added")


def update_customer():
    update = view.get_inputs(crm.HEADERS)
    crm.update_customer(update)
    print("Update successful")


def delete_customer():
    deleted = view.get_inputs(crm.HEADERS)
    crm.delete_customer(deleted)
    print("Delete successful")


def get_subscribed_emails():
    temp_list = data_manager.read_table_from_file(crm.DATAFILE)
    print('Subscribed Customers emails')
    for item in temp_list:
        if item[3] == "1":
            print(item[2])


def run_operation(option):
    if option == 1:
        get_customers_list()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
