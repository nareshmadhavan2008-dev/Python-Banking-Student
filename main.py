from bank import Bank

bank = Bank()

while True:
    print("\n===== PYTHON BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        account_number = input("Enter account number: ")

        print("1. Savings Account")
        print("2. Current Account")
        account_type = input("Select account type: ")

        bank.create_account(
            name, account_number, account_type
        )

    elif choice in ["2", "3", "4", "5"]:
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)

        if account is None:
            print("Account not found!")
            continue

        if choice == "2":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "4":
            print("Customer:", account.name)
            print("Type:", account.account_type())
            print("Balance: Rs.", account.balance)

        elif choice == "5":
            account.show_history()

    elif choice == "6":
        print("Thank you for using our Banking System!")
        break

    else:
        print("Invalid choice!")