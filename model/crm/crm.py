from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def get_customers_list():
    customers = [HEADERS]
    customers.extend(data_manager.read_table_from_file(DATAFILE))
    return customers


def add_customer(new_customer: list):
    id = util.generate_id()
    new_customer.insert(0, id)
    customers = data_manager.read_table_from_file(DATAFILE)
    customers.append(new_customer)
    data_manager.write_table_to_file(DATAFILE, customers)


def update_customer(update: list):
    customers = data_manager.read_table_from_file(DATAFILE)
    for i in range(len(customers)):
        if customers[i][0] == update[0]:
            customers[i] = update
            data_manager.write_table_to_file(DATAFILE, customers)
            break


def delete_customer(deleted: list):
    customers = data_manager.read_table_from_file(DATAFILE)
    for i in range(len(customers)):
        if customers[i][0] == deleted[0]:
            customers.remove(deleted)
            data_manager.write_table_to_file(DATAFILE, customers)
            break
