import sys
import dom_csv_creation as cc

try:
    import matplotlib.pyplot as plt
    import pandas as pd
    import tabulate as tb
except:
    print("Please install the required modules:\nMatplotlib\nPandas\nTabulate\n")
    sys.exit()

def d_montra():
    cc.create_file()

    file = open('help.txt','r')
    inc = pd.read_csv('dom_income.csv', index_col=0)
    exp = pd.read_csv('dom_expense.csv', index_col=0)

    print("\nWelcome to MonTra Household Edition\nA Simple yet efficient CLI-Based Finance-Tracker for your household.")
    print("Currency is assumed as per user's preference.")

    mnt = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
    incl = ['Earnings','Interest_on_Investments','Dividend','Rent','Other_inc']
    expl = ['Housing','Electricity','Telecom','Groceries','Entertainment','Healthcare','Insurance','Tax','Other']
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

        if cmdl[0] == 'credits':
            print("Developers:")
            print("Sneh Gupta\tYash Patel\tDhruvil Joshi")           
                
        elif cmdl[0] == 'save':
            inc.to_csv('dom_income.csv')
            exp.to_csv('dom_expense.csv')
            next_cmd = 0

        elif cmdl[0] == 'help':
            print(file.read())

        elif cmdl[0] == 'show':
            print("INCOME Table\n", tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
            print("EXPENSE Table\n", tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))

        elif cmdl[0] == 'plot':
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
            
        elif cmdl[0] == 'exit':
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
                    inc.to_csv('dom_income.csv')
                    exp.to_csv('dom_expense.csv')
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
    d_montra()