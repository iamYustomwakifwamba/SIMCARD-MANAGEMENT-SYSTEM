import sqlite3

connection = sqlite3.connect('simcard.db')
cursor = connection.cursor()

# cursor.execute('CREATE TABLE services(name text, code text)')
# cursor.execute('CREATE TABLE vouchers(code text, status)')
# cursor.execute('CREATE TABLE customers(phonenumber text, customer_name text, country text, balance real)')
#cursor.execute('CREATE TABLE users(username text, password text, role text)')

vouchers_list = [
    ('88976540', 'active'),
    ('56129000', 'active'),
    ('99342100', 'active'),
    ('88014725', 'active')
]

users_list = [
    ('yusto', '1234', 'admin'),
    ('clinton', '3000', 'admin')
]

customers_list = [
    ('0769350103', 'YUSTO MWAKIFWAMBA', 'Tanzania', 0),
    ('0768456700', 'JUMA NGALIWA', 'Tanzania', 0),
    ('0785901760', 'MAJALIWA HAMISI', 'Burundi', 0)
]

service_list = [
    ('Mobile service', '*148*01#'),
    ('M-PESA', '*150*00#'),
    ('admin dashboard', "*102#"),
]

cursor.executemany('INSERT INTO vouchers values (?, ?)', vouchers_list)
cursor.executemany('INSERT INTO services values (?, ?)', service_list)
cursor.executemany('INSERT INTO users values (?, ?, ?)', users_list)


def get_admin_users_only():
    users = cursor.execute("SELECT FORM customers WHERE role = 'admin'")
    fetched_data = []
    for user in users:
        fetched_data.append({
            "username":f"{user[0]}",
            "password":f"{user[1]}",
            "role":f"{user[2]}"
        })
    return fetched_data

def get_all_customers():
    customers = cursor.execute('SELECT * FROM customers')
    fetched_data = []
    for customer in customers:
        fetched_data.append({
            "phonenumber":f"{customer[0]}",
            "name":f"{customer[1]}",
            "nation":f"{customer[2]}",
            "balance":f"{customer[3]}"
        })
    return fetched_data

def get_all_services():
    services = cursor.execute('SELECT * FROM services')
    final_data = []
    for service in services:
        final_data.append({"service_name":f"{service[0]}", "service_code":f"{service[1]}"})
    return final_data

print(get_all_services())

#connection.close()
