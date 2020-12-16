#The main file to control access to both the editions
#importing Enterprise and Household editions.
import ent_montra
import dom_montra
import sys

try:
    import numpy as np
    import pandas as pd
    import tabulate as tb
    import matplotlib.pyplot as plt

except ImportError:
    print("Please install Required modules:\nMatplotlib\nPandas\nTabulate\nNumPy\n")
    sys.exit()
    
#ascii art
print("""███    ███  ██████  ███    ██ ████████ ██████   █████  
████  ████ ██    ██ ████   ██    ██    ██   ██ ██   ██ 
██ ████ ██ ██    ██ ██ ██  ██    ██    ██████  ███████ 
██  ██  ██ ██    ██ ██  ██ ██    ██    ██   ██ ██   ██ 
██      ██  ██████  ██   ████    ██    ██   ██ ██   ██""")


while True:
    #main menu for selection of edition.
    print("\nHello there! Welcome to MonTra!")
    print("Which MonTra edition would you like to you use?")
    choice = input("\n0. Exit\n1. Household Edition\n2. Enterprise Edition\nEnter your choice: ")
    try:
        choice = int(choice)
        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 1:
            dom_montra.d_montra()
        elif choice == 2:
            ent_montra.e_montra()
        else:
            print("Invalid selection, try again.")
    except ValueError:
        print("Invalid Selection, try again.")      #ValueError handling to avoid crashing.