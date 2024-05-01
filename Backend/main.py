import robin_stocks.robinhood as rs
# import matplotlib.pyplot as plt
import json

def load_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data



# Log in to Robinhood
rs.login(username="Email", password="Password")

with open('data.json', 'w') as file:
    # Get your current holdings
    holdings = rs.build_holdings()
    json.dump(holdings, file, indent=4)
