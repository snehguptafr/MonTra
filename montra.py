import os

try:
    import matplotlib.pyplot as plt
    import csv_creation as cc
    import pandas as pd
except:
    print("Please install the required modules.")
    #os.exit()
cc.create_file()

file = open('help.txt','r')
inc = pd.read_csv('income.csv', index_col=0)
exp = pd.read_csv('expense.csv', index_col=0)

print("Welcome to MonTra λ\nOne-Stop CLI-Based Finance-Tracker")
print("All the figures mentioned by the user are the currency of the user's country.")

mnt = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
incl = ['Sales','Interest','Rent','Bad_Debts_Recovered','Commission','Miscellaneous']
expl = ['Purchase','Electricity','Telecom','Rent','Interest','Salary/Wages','Maintenance','Tax','Travelling','Advertisement','Inventory Costs','Insurance','Miscellaneous']
sym = ['=','+','-','*','/']
next_cmd = 0

while True:
    cmd = input('\nMonTra λ ')
    cmdl = cmd.split()
    suc = 0
    err = 0
    next_cmd += 1
    if next_cmd == 1:
        saved = 1

    #['income',':','Apr',':','Sales','=',2000]
    try:
        if cmdl[0] == 'income' and len(cmdl) == 7:
            if cmdl[2] in mnt and cmdl[4] in incl and cmdl[5] in sym and cmdl[1] == ':' and cmdl[3] == ':' and type(float(cmdl[6])) is float:
                if cmdl[5] == '=':
                    inc.loc[cmdl[2],cmdl[4]] = float(cmdl[6])
                    print(inc)
                elif cmdl[5] == '+':    
                    inc.loc[cmdl[2],cmdl[4]] += float(cmdl[6])
                    print(inc)
                elif cmdl[5] == '-':    
                    inc.loc[cmdl[2],cmdl[4]] -= float(cmdl[6])
                    print(inc)
                elif cmdl[5] == '*':    
                    inc.loc[cmdl[2],cmdl[4]] *= float(cmdl[6])
                    print(inc)
                elif cmdl[5] == '/':    
                    inc.loc[cmdl[2],cmdl[4]] /= float(cmdl[6])
                    print(inc)
                suc = 1
                edit = True
                
            else:
                print("There's a syntax error in your command, please recheck.")
                err = 1
            
        elif cmdl[0] == 'expense' and  len(cmdl) == 7:
            if cmdl[2] in mnt and cmdl[4] in expl and cmdl[5] in sym and cmdl[1] == ':' and cmdl[3] == ':' and type(float(cmdl[6])) == float:
                if cmdl[5] == '=':
                    exp.loc[cmdl[2],cmdl[4]] = float(cmdl[6])
                    print(exp)
                elif cmdl[5] == '+':    
                    exp.loc[cmdl[2],cmdl[4]] += float(cmdl[6])
                    print(exp)
                elif cmdl[5] == '-':    
                    exp.loc[cmdl[2],cmdl[4]] -= float(cmdl[6])
                    print(exp)
                elif cmdl[5] == '*':    
                    exp.loc[cmdl[2],cmdl[4]] *= float(cmdl[6])
                    print(exp)
                elif cmdl[5] == '/':    
                    exp.loc[cmdl[2],cmdl[4]] /= float(cmdl[6])
                    print(exp)
                edit = True
                suc = 1
            else:
                print("There's a syntax error in your command, please recheck.")
                err = 1

    except ValueError:
        print("There's a syntax error in your command, please recheck.")
        err = 1
    except IndexError:
        print("'' - not a command, try again.")
        err = 1
        next_cmd = 0

    if cmd == 'credits':
        print("Developers:")
        print("Sneh Gupta\tYash Patel\tDhruvil Joshi")           
            
    elif cmd == 'save':
        inc.to_csv('income.csv')
        exp.to_csv('expense.csv')
        next_cmd = 0

    elif cmd == 'help':
        print(file.read())

    elif cmd == 'show':
        print('Income Table:\n',inc)
        print('Expense Table:\n',exp)

    elif cmd == 'plot':
        alls = input('Mention income/expense category(ies)(separate them by space) which you wish to observe graphically: ')
        lall = alls.split()
        if len(lall) == 0:
            print("'' - invalid income/expense")
        elif len(lall) > 0:
            for items in lall:
                if items in incl:
                    plt.plot(mnt, list(inc[items]), label = items)
                    plt.xlabel('Months')
                    plt.ylabel('Amount')
                    plt.legend()
                elif items in expl:
                    plt.plot(mnt, list(exp[items]), label = items)
                    plt.xlabel('Months')
                    plt.ylabel('Amount')
                    plt.legend()
            plt.show()
        else:
            print('Invalid income selection')
        
    elif cmd == 'exit':
        if saved == 1 and next_cmd == 1:
            print("Exiting...\nDone")
            break
        while True:
            save = input('Save and exit?[Y/n]: ')
            if save == 'n':
                print('Exiting...\nDone')
                break
            elif save == 'y' or save == 'Y' or save == '':
                print('Saving and exiting...\nDone')
                inc.to_csv('income.csv')
                exp.to_csv('expense.csv')
                break
            else:
                print('Invalid selection')  
        break

    else:
        if err == 1 or suc == 1:
            pass
        else:
            print("'"+cmd+"'-",'not a command, try again.')
