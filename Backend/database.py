import sqlite3

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('instance/bills.db')

# Function to create the bills table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount_monthly REAL NOT NULL,
            principal REAL,
            interest_rate REAL
        )
    ''')

    conn.commit()
    conn.close()

# Function to insert a new bill
def insert_bill(name, amount_monthly, principal=None, interest_rate=None):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO bills (name, amount_monthly, principal, interest_rate)
        VALUES (?, ?, ?, ?)
    ''', (name, amount_monthly, principal, interest_rate))

    conn.commit()
    conn.close()

# Function to retrieve all bills
def get_all_bills():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM bills')
    bills = cursor.fetchall()

    conn.close()

    return bills

# Function to update a bill
def update_bill(id, name, amount_monthly, principal=None, interest_rate=None):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE bills
        SET name=?, amount_monthly=?, principal=?, interest_rate=?
        WHERE id=?
    ''', (name, amount_monthly, principal, interest_rate, id))

    conn.commit()
    conn.close()

# Function to delete a bill
def delete_bill(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM bills WHERE id=?', (id,))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    entries = [
        {"name": "Car Loan", "amount_monthly": 297.32, "principal": 12328.53, "interest_rate": 8.89},
        {"name": "Internet", "amount_monthly": 81, "principal": None, "interest_rate": None},
        {"name": "Gym", "amount_monthly": 245, "principal": None, "interest_rate": None},
        # Add more entries as needed
    ]

    # Insert each entry into the database
    for entry in entries:
        insert_bill(entry["name"], entry["amount_monthly"], entry["principal"], entry["interest_rate"])

    update_bill(2, "Rent", 500, None, None)
