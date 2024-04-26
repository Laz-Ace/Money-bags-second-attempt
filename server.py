from flask import Flask, render_template
from datetime import date
from Backend.main import get_portfolio_summary
import json

def load_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

app = Flask(__name__)
base_url = 'http://127.0.0.1:5000'

@app.route('/')
def home():
    data = load_data_from_json('data.json')

    tickers = data['tickers']
    amounts = data['amount']

    portfolio = {label: value for label, value in zip(tickers, amounts)}

    summary = get_portfolio_summary(portfolio)
    total_value = summary.get('Total Value')

    today = date.today().strftime("%b-%d-%Y")
    return render_template("index.html", spy=total_value, current_date=today)

if __name__ == '__main__':
    app.run(debug=True)
