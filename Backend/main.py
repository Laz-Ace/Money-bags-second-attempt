import robin_stocks.robinhood as rs
import matplotlib.pyplot as plt
import json

def read_equity_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    equity_dict = {}
    for stock, info in data.items():
        equity_dict[info['name']] = float(info['equity'])
    
    return equity_dict

def plot_pie_chart(data, title="Investment Chart", figsize=(8, 8), filename="pie_chart.png"):
    """
    Plot a pie chart from a dictionary of data and save it as a PNG file.

    Parameters:
        data (dict): A dictionary where keys represent categories and values represent data points.
        title (str): Title of the pie chart (default is "Pie Chart").
        filename (str): File name to save the PNG file (default is "pie_chart.png").

    Returns:
        None
    """
    # Extract keys (categories) and values (data points)
    categories = list(data.keys())
    values = list(data.values())

    # Plotting the pie chart
    plt.figure(figsize=figsize)
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(filename)  # Save the pie chart as a PNG file
    plt.close()  # Close the plot to prevent displaying it

# Log in to Robinhood
rs.login(username="email", password="password")

with open('Data/holdings.json', 'w') as file:
    # Get your current holdings
    holdings = rs.build_holdings()
    json.dump(holdings, file, indent=4)

data = read_equity_from_json('Data/holdings.json')
plot_pie_chart(data, title='Distribution of Categories', filename='static/pie_chart.png')