import ent_montra
import dom_montra

while True:
    print("\nHello there! Welcome to MonTra!")
    print("Which MonTra edition would you like to you use?")
    choice = input("\n0. Exit\n1. Household Edition\n2. Enterprise Edition\nEnter your choice: ")
    try:
        choice = int(choice)
        if choice == 0:
            break
        elif choice == 1:
            dom_montra.d_montra()
        elif choice == 2:
            ent_montra.e_montra()
        else:
            print("Invalid selection, try again.")
    except ValueError:
        print("Invalid Selection, try again.")