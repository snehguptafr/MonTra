import pandas as pd
import numpy as np

def create_file():
    try:
        exp = pd.read_csv('expense.csv')
    except FileNotFoundError:
        exp = pd.DataFrame({'Purchase': np.NaN,'Electricity': np.NaN,'Telecom': np.NaN,'Rent': np.NaN,'Interest': np.NaN,'Salary/Wages': np.NaN,'Maintenance': np.NaN,'Tax': np.NaN,'Advertisement': np.NaN,'Insurance': np.NaN,'Miscellaneous': np.NaN}, index=["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec", "Jan","Feb","Mar"])
        exp.to_csv('expense.csv')

    try:
        inc = pd.read_csv('income.csv')
    except FileNotFoundError:
        inc = pd.DataFrame({'Sales': np.NaN,'Interest': np.NaN,'Rent': np.NaN,'Bad_Debts_Recovered': np.NaN,'Commission': np.NaN,'Miscellaneous': np.NaN}, index=["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar"])
        inc.to_csv("income.csv")

if __name__ == '__main__':
    create_file()