import sqlite3

connection = sqlite3.connect('simcard.db')
cursor = connection.cursor()

# cursor.execute('CREATE TABLE services(name text, code text)')
# cursor.execute('CREATE TABLE vouchers(code text, status)')

vouchers_list = [
    ('88976540', 'active'),
    ('56129000', 'active'),
    ('99342100', 'active'),
    ('88014725', 'active')
]

service_list = [
    ('Mobile service', '*148*01#'),
    ('M-PESA', '*150*00#')
]

cursor.executemany('INSERT INTO vouchers values (?, ?)', vouchers_list)
cursor.executemany('INSERT INTO services values (?, ?)', service_list)

for row in cursor.execute('SELECT * FROM vouchers'):
    print(row)



def get_vouchers_list():
    for row in cursor.execute('SELECT * FROM vouchers'):
        return row

def get_all_services():
    services = cursor.execute('SELECT * FROM services')
    final_data = []
    for service in services:
        final_data.append({"service_name":f"{service[0]}", "service_code":f"{service[1]}"})
    return final_data

print(get_all_services())

#connection.close()
