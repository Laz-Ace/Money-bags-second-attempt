from flask import Flask, render_template
import sqlite3
from datetime import date
import json

# Initializing Flask app
app = Flask(__name__)

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('instance/bills.db')

def read_equity_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    equity_dict = {}
    for stock, info in data.items():
        equity_dict[info['name']] = float(info['equity'])
    
    return equity_dict

# Default route 
@app.route('/')
def home():
    data = read_equity_from_json('Data/holdings.json')
    total_value = sum(int(value) for value in data.values())

    today = date.today().strftime("%b-%d-%Y")
    return render_template("index.html", spy=total_value, current_date=today)

# Route to display list of bills
@app.route('/bills')
def display_bills():
    # Connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # Retrieve bills data from the database
    cursor.execute('SELECT name, amount_monthly FROM bills')
    bills = cursor.fetchall()

    # Calculate days remaining for each bill
    bills_with_days_remaining = []
    for bill in bills:
        name, amount_monthly = bill
        cursor.execute("SELECT strftime('%s', 'now') - strftime('%s', 'now', 'start of month', '+1 month', '-1 day') AS days_remaining")
        days_remaining = cursor.fetchone()[0]
        bills_with_days_remaining.append((name, amount_monthly, days_remaining))

    # Close database connection
    conn.close()

    return render_template('bills.html', bills=bills_with_days_remaining)


@app.route('/cal')
def calendar():
    return render_template('cal.html')

if __name__ == '__main__':
    app.run(debug=True)
