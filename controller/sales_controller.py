from model.sales import sales
from view import terminal as view


def list_transactions():
    transactions = sales.list_transactions()
    view.print_table(transactions)


def add_transaction():
    new_data = view.get_inputs(sales.HEADERS[1:])
    sales.add_transaction(new_data)
    print("Record added successfully")


def update_transaction():
    values = view.get_inputs(sales.HEADERS)
    sales.update_transaction(values)
    print("Update successful")


def delete_transaction():
    id = view.get_input(sales.HEADERS[0])
    sales.delete_transaction(id)
    print("Delete successful")


def get_biggest_revenue_transaction():
    print(sales.get_biggest_revenue_product())


def get_biggest_revenue_product():
    prod = sales.get_biggest_revenue_product()

    if len(prod) != 0:
        print(f"{prod[2]}: {prod[3]}")


def count_transactions_between():
    dateMin = view.get_input("Date start")
    dateMax = view.get_input("Date end")
    transactions = sales.get_transactions_between(dateMin, dateMax)

    print(f"# of transactions:{len(transactions)}")


def sum_transactions_between():
    dateMin = view.get_input("Date start")
    dateMax = view.get_input("Date end")
    transactions = sales.get_transactions_between(dateMin, dateMax)

    total = 0
    for t in transactions:
        total += float(t[3])

    print(f"Sum of transactions:{total}")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum number of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
            print("")
        except KeyError as err:
            view.print_error_message(err)
