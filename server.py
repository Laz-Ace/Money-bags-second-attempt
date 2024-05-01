from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from Backend.main import get_portfolio_summary # <---- Remove from this file. Should be a Backend thing
import json

# Should be switched with function to pull info from SQL Database
def load_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Initializing Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

# Default route 
@app.route('/')
def home():
    data = load_data_from_json('data.json')

    tickers = data['tickers']
    amounts = data['amount']
    portfolio = {label: value for label, value in zip(tickers, amounts)}

    summary = get_portfolio_summary(portfolio)
    total_value = summary.get('Total Value')
    dynamic_dict_data = {                    # ----------------------------------------------------------------
        'Checking': '----',                  #  TODO
        'Savings': '----',                   #  1. Dont love this. Probably should move most of this to back-
        'Investment': round(total_value, 2)  #     end file. Want to keep only POST/GET requests in this sections.
    }                                        #
    goal_dict = {                            #
        'Car': '----',                       #
        'House': '----',                     #
        'Travel': '----'                     #
    }                                        # -----------------------------------------------------------------
    today = date.today().strftime("%b-%d-%Y")
    return render_template("index.html", spy=total_value,  dynamic_dict=dynamic_dict_data, goals=goal_dict, current_date=today) # <- Way too long?

if __name__ == '__main__':
    app.run(debug=True)
