import csv
print("Hello!")

def create_file():
    #creating outgo csv file
    try:
        outgo = open("outgo.csv", 'r')
    except FileNotFoundError:
        outgo = open("outgo.csv",'w')
        writer = csv.writer(outgo, delimiter=',')
        outgo_header = ['MONTHS','Purchase','Electricity','Telecom','Rent','Interest','Depreciation','Salary','Wages','Maintenance','Tax','Travelling','Advertisement','Inventory Costs','Insurance','Miscellaneous']
        writer.writerow(outgo_header)
        months = ["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec", "Jan","Feb","Mar"]
        for month in months:
            record = [month]
            writer.writerow(record)
        outgo.close()

    #creating income csv file
    try:
        income = open("income.csv", 'r')
    except FileNotFoundError:
        income = open("income.csv", 'w')
        writer = csv.writer(income, delimiter=',')
        income_header = ['MONTHS','Sales','Interest','Rent','Bad Debts Recovered','Miscellaneous']
        writer.writerow(income_header)
        months = ["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec", "Jan","Feb","Mar"]
        for month in months:
            record = [month]
            writer.writerow(record)
        income.close()

if __name__ == '__main__':
    create_file()