Sure! Here is the entire README content as a **single markdown file**—all together, neatly formatted:

````markdown
# Console Bank

A simple command-line banking system implemented in Python. This project allows customers to create accounts, log in, check balances, deposit and withdraw money, and enables an admin to manage customer accounts.

---

## Features

### Customer
- **Sign Up**: Create a new account with a username, password, and initial deposit.
- **Login**: Access your account using Customer ID, username, and password.
- **Balance Inquiry**: View your current account balance.
- **Deposit**: Add funds to your account.
- **Withdraw**: Remove funds from your account.

### Admin
- **Login**: Access admin functions with username `admin` and password `123`.
- **View Customers**: List all customer accounts with their balances.
- **Transfer Funds**: Move money between customer accounts.

---

## Technologies Used

- Python 3.x
- Built-in modules: `random`

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/enka31/Console-Bank-Python.git
   cd Console-Bank-Python
````

2. Run the program:

   ```bash
   python console_bank.py
   ```
3. Follow the on-screen prompts to interact with the system.

---

## Example Usage

### Starting the Application

```bash
$ python console_bank.py

--- Welcome to Console Bank ---
Do you want to login as Admin, Customer, or Exit?
```

### Customer Flow

* **Sign Up:**

  ```plaintext
  Do you want to Login or Sign Up? (type 'back' to go back)
  sign up

  Please enter a Username:
  johndoe
  Please enter a Password:
  ********
  Please enter how much you want to deposit:
  1000
  New Customer Created Successfully! Your Customer ID is: 1234567
  ```

* **Login:**

  ```plaintext
  Do you want to Login or Sign Up? (type 'back' to go back)
  login

  Please enter your Customer ID:
  1234567
  Please enter your Username:
  johndoe
  Please enter your Password:
  ********

  Welcome back, johndoe!

  Customer Menu:
  1. See Balance
  2. Deposit Money
  3. Withdraw Money
  4. Logout (Go Back)
  Choose an option:
  ```

* Check Balance, Deposit, Withdraw operations follow with prompts accordingly.

---

### Admin Flow

* **Login:**

  ```plaintext
  Please enter admin username:
  admin
  Please enter admin password:
  123

  Successfully logged in as admin!

  Admin Menu:
  1. See all customers
  2. Transfer money between customers
  3. Logout (Go Back)
  Choose an option:
  ```
* View all customers lists customer IDs, usernames, and balances.
* Transfer money between customer accounts after inputting sender ID, receiver ID, and amount.

---

## Important Notes

* **Data Persistence:** Customer data is stored in memory and will be lost when the program exits.
* **Security:** Passwords are stored as plain text, and admin credentials are hardcoded (`admin` / `123`). Not secure for production use.
* **Customer ID:** Unique numeric IDs are randomly generated for each customer.
* **Input Validation:** Basic validation is implemented for numeric inputs and options, but could be improved.

---

## Future Enhancements

* Add persistent storage (e.g., files or databases).
* Implement password hashing and better authentication.
* Improve input validation and error handling.
* Add a GUI for enhanced usability.
* Implement role-based access control.

---

## License

This project is for educational purposes and does not include a formal license.

---

*Enjoy managing your simple console bank!*

```

You can just copy-paste this as your `README.md` file in your repo!
```
