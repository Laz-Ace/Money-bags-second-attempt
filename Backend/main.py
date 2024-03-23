import yfinance as yf
import csv
import matplotlib.pyplot as plt
import json

def load_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def fetch_stock_data_to_csv(ticker, start_date, end_date, output_file):
    # Fetch stock data
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    
    # Extract relevant information
    data = {
        'Date': df.index,
        'Open': df['Open'],
        'High': df['High'],
        'Low': df['Low'],
        'Close': df['Close'],
        'Volume': df['Volume']
        # Add more data as needed
    }

    # Write data to CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(len(data['Date'])):
            writer.writerow({field: data[field][i] for field in fieldnames})

def generate_pie_chart(data, labels):
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Pie Chart')
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping.
    
    # Save the plot to a file or directly show it.
    plt.savefig('static\pie_chart.png')  # Save the plot as a file.
    # plt.show()  # Directly show the plot (use this if you want to display it in the Flask app).
    plt.close()

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

data = load_data_from_json('data.json')
tickers = data['tickers']
amounts = data['amount']

portfolio = {label: value for label, value in zip(tickers, amounts)}

summary = get_portfolio_summary(portfolio)
adjusted_contribution = summary.get('Adjusted_contribution')

generate_pie_chart(adjusted_contribution, tickers)