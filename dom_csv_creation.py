#importing required modules
import pandas as pd
import numpy as np

#function to create or check required files
def create_file():
    try:
        exp = pd.read_csv('dom_expense.csv')
    except FileNotFoundError:
        exp = pd.DataFrame({'Housing': np.NaN,'Electricity': np.NaN,'Telecom': np.NaN,'Groceries': np.NaN,'Entertainment': np.NaN,'Healthcare': np.NaN,'Insurance': np.NaN,'Tax': np.NaN,'Other': np.NaN}, index=["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec", "Jan","Feb","Mar"])
        exp.to_csv('dom_expense.csv')

    try:
        inc = pd.read_csv('dom_income.csv')
    except FileNotFoundError:
        inc = pd.DataFrame({'Earnings': np.NaN,'Interest_on_Investments': np.NaN,'Dividend': np.NaN,'Rent': np.NaN,'Other_inc': np.NaN}, index=["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar"])
        inc.to_csv("dom_income.csv")

#if this file is run as main, run this function.
if __name__ == '__main__':
    create_file()