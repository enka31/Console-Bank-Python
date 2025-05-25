import random

customers = {}

def generate_unique_id():
    while True:
        new_id = str(random.randrange(1, 10000000))
        if new_id not in customers:
            return new_id

def create_customer():
    print("Please enter a Username:")
    new_user = input().strip()
    print("Please enter a Password:")
    new_pass = input().strip()
    print("Please enter how much you want to deposit:")
    while True:
        try:
            new_deposit = float(input().strip())
            if new_deposit < 0:
                print("Deposit cannot be negative, try again:")
                continue
            break
        except ValueError:
            print("Please enter a valid number:")
    new_id = generate_unique_id()
    customers[new_id] = {
        "user": new_user,
        "password": new_pass,
        "balance": new_deposit
    }
    print(f"New Customer Created Successfully! Your Customer ID is: {new_id}")
    input("Press Enter to go back to main menu...")

def customer_menu(user_id):
    while True:
        print("\nCustomer Menu:")
        print("1. See Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout (Go Back)")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"Your current balance is: £{customers[user_id]['balance']:.2f}")
            input("Press Enter to continue...")
        elif choice == "2":
            print("Enter amount to deposit:")
            try:
                amount = float(input().strip())
                if amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    customers[user_id]['balance'] += amount
                    print(f"Deposited £{amount:.2f}. New balance: £{customers[user_id]['balance']:.2f}")
            except ValueError:
                print("Invalid amount.")
            input("Press Enter to continue...")
        elif choice == "3":
            print("Enter amount to withdraw:")
            try:
                amount = float(input().strip())
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif amount > customers[user_id]['balance']:
                    print("Insufficient balance.")
                else:
                    customers[user_id]['balance'] -= amount
                    print(f"Withdrew £{amount:.2f}. New balance: £{customers[user_id]['balance']:.2f}")
            except ValueError:
                print("Invalid amount.")
            input("Press Enter to continue...")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option, try again.")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. See all customers")
        print("2. Transfer money between customers")
        print("3. Logout (Go Back)")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            if not customers:
                print("No customers found.")
            else:
                print("\nAll Customers:")
                for cid, info in customers.items():
                    print(f"ID: {cid} | Username: {info['user']} | Balance: £{info['balance']:.2f}")
            input("Press Enter to continue...")
        elif choice == "2":
            if len(customers) < 2:
                print("Need at least two customers to do transfer.")
                input("Press Enter to continue...")
                continue

            print("Enter sender customer ID:")
            sender_id = input().strip()
            if sender_id not in customers:
                print("Sender ID not found.")
                input("Press Enter to continue...")
                continue

            print("Enter receiver customer ID:")
            receiver_id = input().strip()
            if receiver_id not in customers:
                print("Receiver ID not found.")
                input("Press Enter to continue...")
                continue

            if sender_id == receiver_id:
                print("Sender and receiver cannot be the same.")
                input("Press Enter to continue...")
                continue

            print("Enter amount to transfer:")
            try:
                amount = float(input().strip())
                if amount <= 0:
                    print("Amount must be positive.")
                elif customers[sender_id]['balance'] < amount:
                    print("Sender has insufficient funds.")
                else:
                    customers[sender_id]['balance'] -= amount
                    customers[receiver_id]['balance'] += amount
                    print(f"Transferred £{amount:.2f} from {sender_id} to {receiver_id}.")
            except ValueError:
                print("Invalid amount.")
            input("Press Enter to continue...")
        elif choice == "3":
            print("Logging out of admin...")
            break
        else:
            print("Invalid option, try again.")

def customer_login():
    print("Please enter your Customer ID:")
    cid = input().strip()
    if cid not in customers:
        print("Customer ID not found.")
        input("Press Enter to go back...")
        return
    print("Please enter your Username:")
    username = input().strip()
    print("Please enter your Password:")
    password = input().strip()
    if customers[cid]['user'] == username and customers[cid]['password'] == password:
        print(f"Welcome back, {username}!")
        customer_menu(cid)
    else:
        print("Incorrect username or password.")
        input("Press Enter to go back...")

def main():
    while True:
        print("\n--- Welcome to Console Bank ---")
        print("Do you want to login as Admin, Customer, or Exit?")
        usertype = input().strip().lower()

        if usertype == "admin":
            print("Please enter admin username:")
            adminuser = input().strip()
            print("Please enter admin password:")
            adminpass = input().strip()
            if adminuser == "admin" and adminpass == "123":
                print("Successfully logged in as admin!")
                admin_menu()
            else:
                print("Invalid admin credentials.")
                input("Press Enter to continue...")
        elif usertype == "customer":
            print("Do you want to Login or Sign Up? (type 'back' to go back)")
            custmrExist = input().strip().lower()
            if custmrExist == "login":
                customer_login()
            elif custmrExist == "sign up":
                create_customer()
            elif custmrExist == "back":
                continue
            else:
                print("Invalid option.")
                input("Press Enter to continue...")
        elif usertype == "exit":
            print("Thank you for using Console Bank. Goodbye!")
            break
        else:
            print("Invalid user type.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
