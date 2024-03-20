from flask import Flask, render_template
from datetime import date
import yfinance as yf
import json

def load_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def get_portfolio_summary(portfolio):
    total_value = 0
    adjusted_contribution = []
    
    for symbol, quantity in portfolio.items():
        # Fetch stock data from Yahoo Finance
        stock = yf.Ticker(symbol)
        current_price = stock.history(period='1d')['Close'].iloc[-1]
        stock_value = current_price * quantity
        total_value += stock_value
        
        # Note the total market value of every specific stock
        adjusted_contribution.append(stock_value)
    
    # Calculate overall return
    # Here you can calculate returns based on initial investment, cost basis, etc.
    overall_return = 0  # Placeholder for demonstration

    return {
        'Total Value': total_value,
        'Adjusted_contribution': adjusted_contribution,
        'Overall Return': overall_return
    }

app = Flask(__name__)

@app.route('/')
def home():
    data = load_data_from_json('data.json')

    # ---------This should be done outside the main loop----------------
    tickers = data['tickers']
    amounts = data['amount']

    
    portfolio = {label: value for label, value in zip(tickers, amounts)}
    # ------------------------------------------------------------------

    summary = get_portfolio_summary(portfolio)
    total_value = summary.get('Total Value')
    adjusted_contribution = summary.get('Adjusted_contribution')
    
    today = date.today().strftime("%b-%d-%Y")
    return render_template("index.html", spy=total_value, current_date=today)

if __name__ == '__main__':
    app.run(debug=True)
