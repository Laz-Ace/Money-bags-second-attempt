import yfinance as yf
import csv
import matplotlib.pyplot as plt

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
    plt.savefig('static/pie_chart.png')  # Save the plot as a file.
    # plt.show()  # Directly show the plot (use this if you want to display it in the Flask app).
    plt.close()