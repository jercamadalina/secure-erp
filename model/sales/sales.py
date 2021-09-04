from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def list_transactions():
    transactions = [HEADERS]
    transactions.extend(data_manager.read_table_from_file(DATAFILE))

    return transactions


def add_transaction(values):
    id = util.generate_id()
    values.insert(0, id)
    transactions = data_manager.read_table_from_file(DATAFILE)
    transactions.append(values)
    data_manager.write_table_to_file(DATAFILE, transactions)


def update_transaction(values):
    transactions = data_manager.read_table_from_file(DATAFILE)

    for t in transactions:
        if t[0] == values[0]:
            t[1] = values[1]
            t[2] = values[2]
            t[3] = values[3]
            t[4] = values[4]
            break

    data_manager.write_table_to_file(DATAFILE, transactions)


def delete_transaction(id):
    transactions = data_manager.read_table_from_file(DATAFILE)

    lenghtT = len(transactions)

    for transaction in transactions:
        if id in transaction:
            transactions.remove(transaction)
            break

    if lenghtT == len(transactions):
        print("This id does not exist.")
        return

    data_manager.write_table_to_file(DATAFILE, transactions)


def get_biggest_revenue_product():
    transactions = data_manager.read_table_from_file(DATAFILE)
    price = float(0)
    best_product_transaction = ["could be NONE"]
    for i in transactions:
        if price < float(i[3]):
            best_product_transaction = i
            price = float(i[3])
    return best_product_transaction


def get_transactions_between(dateMinStr, dateMaxStr):
    from datetime import datetime
    dateMin = datetime.strptime(dateMinStr, '%Y-%m-%d')
    dateMax = datetime.strptime(dateMaxStr, '%Y-%m-%d')

    transactions = data_manager.read_table_from_file(DATAFILE)

    filtered_transactions = []
    for t in transactions:
        dateT = datetime.strptime(t[4], '%Y-%m-%d')
        if dateT >= dateMin and dateT <= dateMax:
            filtered_transactions.append(t)

    return filtered_transactions
