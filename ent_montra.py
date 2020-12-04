import sys
import ent_csv_creation as cc

try:
    import matplotlib.pyplot as plt
    import pandas as pd
    import tabulate as tb
except:
    print("Please install the required modules:\nMatplotlib\nPandas\nTabulate\n")
    sys.exit()

def e_montra():
    cc.create_file()

    file = open('help.txt','r')
    inc = pd.read_csv('ent_income.csv', index_col=0)
    exp = pd.read_csv('ent_expense.csv', index_col=0)

    print("\nWelcome to MonTra Enterprise Edition\nA Simple yet efficient CLI-Based Finance-Tracker for your Enterprise")
    print("Currency is assumed as per user's preference.")

    mnt = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
    incl = ['Sales','Interest_inc','Rent_inc','Bad_Debts_Recovered','Commission','Other_inc']
    expl = ['Purchase','Electricity','Telecom','Rent','Interest','Salary/Wages','Maintenance','Tax','Travelling','Advertisement','Inventory Costs','Insurance','Other']
    sym = ['=','+','-','*','/']
    syn_er = "There's a syntax error in your command, please recheck."
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
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '+':    
                        inc.loc[cmdl[2],cmdl[4]] += float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '-':    
                        inc.loc[cmdl[2],cmdl[4]] -= float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '*':    
                        inc.loc[cmdl[2],cmdl[4]] *= float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '/':    
                        inc.loc[cmdl[2],cmdl[4]] /= float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    suc = 1
                    
                else:
                    print(syn_er)
                    err = 1
                
            elif cmdl[0] == 'expense' and  len(cmdl) == 7:
                if cmdl[2] in mnt and cmdl[4] in expl and cmdl[5] in sym and cmdl[1] == ':' and cmdl[3] == ':' and type(float(cmdl[6])) == float:
                    if cmdl[5] == '=':
                        exp.loc[cmdl[2],cmdl[4]] = float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '+':    
                        exp.loc[cmdl[2],cmdl[4]] += float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '-':    
                        exp.loc[cmdl[2],cmdl[4]] -= float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '*':    
                        exp.loc[cmdl[2],cmdl[4]] *= float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '/':    
                        exp.loc[cmdl[2],cmdl[4]] /= float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    suc = 1
                else:
                    print(syn_er)
                    err = 1

        except ValueError:
            print(syn_er)
            err = 1
        except IndexError:
            print("'' - not a command, try again.")
            err = 1
            next_cmd = 0

        if cmd == 'credits':
            print("Developers:")
            print("Sneh Gupta\tYash Patel\tDhruvil Joshi")           
                
        elif cmd == 'save':
            inc.to_csv('ent_income.csv')
            exp.to_csv('ent_expense.csv')
            next_cmd = 0

        elif cmd == 'help':
            print(file.read())

        elif cmd == 'show':
            print("INCOME Table\n", tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
            print("EXPENSE Table\n", tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))

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
                    inc.to_csv('ent_income.csv')
                    exp.to_csv('ent_expense.csv')
                    break
                else:
                    print('Invalid selection')  
            break

        else:
            if err == 1 or suc == 1:
                pass
            else:
                print("'"+cmd+"'-",'not a command, try again.')

if __name__ == '__main__':
    e_montra()