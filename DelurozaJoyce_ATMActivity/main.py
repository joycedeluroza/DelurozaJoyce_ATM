# ATM Program with Loop

Delurozabalance = 1000.0

while True:
    # menu
    print("\n============== ATM MENU ==============")
    print("           1. Check Balance")
    print("           2. Deposit Money")
    print("           3. Withdraw Money")
    print("           4. Exit")

    print("======================================")
    Delurozachoice = input("     Enter your choice (1-4): ")
    print("======================================")

    if Delurozachoice == "1":
        # Check Balance
        print(f"  Your current balance is: ₱ {Delurozabalance:.2f}")
        print("======================================")
        print()
        print()

    elif Delurozachoice == "2":
        # Deposit Money
        while True:
            try:
                Delurozaamount = float(input("\n   Enter amount to deposit: ₱ "))
                print()
            except ValueError:
                print("======================================")
                print("   Invalid amount! Please try again.")
                print("======================================")
                continue

            if Delurozaamount > 0:
                Delurozabalance += Delurozaamount
                print("======================================")
                print(f"    Successfully deposited ₱ {Delurozaamount:.2f}")
                print("======================================")
                print(f"        New balance: ₱ {Delurozabalance:.2f}")
                print("======================================")
                print()
                print()
                break
            else:
                print("======================================")
                print("   Invalid amount! Please try again.")
                print("======================================")

    elif Delurozachoice == "3":
        # Withdraw Money
        while True:
            try:
                Delurozaamount = float(input("\n   Enter amount to withdraw: ₱ "))
                print()
            except ValueError:
                print("======================================")
                print("   Invalid amount! Please try again.")
                print("======================================")
                continue

            if Delurozaamount > 0 and Delurozaamount <= Delurozabalance:
                Delurozabalance -= Delurozaamount
                print("======================================")
                print(f"    Successfully withdrew ₱ {Delurozaamount:.2f}")
                print("======================================")
                print(f"        New balance: ₱ {Delurozabalance:.2f}")
                print("======================================")
                print()
                print()
                break

            elif Delurozaamount > Delurozabalance:
                print("======================================")
                print("Insufficient funds!  Please try again.")
                print("======================================")
            else:
                print("======================================")
                print("   Invalid amount! Please try again.")
                print("======================================")

    elif Delurozachoice == "4":
        # Exit
        print(" Thank you for using the ATM. Goodbye!")
        print("======================================")
        break

    else:
        print("  Invalid choice. Please select 1-4.")
        print("======================================")
        print()
        print()