# 🏦 Bank Management System (OOP in Python)

This is a **Bank Management System** developed in Python using **Object-Oriented Programming (OOP)** principles. It allows basic banking operations like creating customers, managing accounts, performing deposits, withdrawals, and calculating interest.

---

## 📁 Project Structure
```
bank-management-system/
│
├── main.py # Entry point of the application
├── bank.py # Bank class managing customers and accounts
├── customer.py # Customer class
├── account.py # Abstract base Account class
├── savings_account.py # Inherits from Account
├── current_account.py # Inherits from Account
├── fixed_account.py # Inherits from Account
├── user_menu.py # Handles user interactions
├── accounts.csv # Stores account data
├── customers.csv # Stores customer data
```

---

## ✅ Features

- Add and remove customers
- Create accounts: **Savings**, **Current**, and **Fixed**
- Deposit and withdraw amounts
- Calculate interest for:
  - **Savings Account** (based on a fixed interest rate)
  - **Fixed Account** (based on deposit duration)
- Data stored in CSV files for simplicity

---

## 💡 Object-Oriented Concepts Used

- **Abstraction:** `Account` is an abstract base class
- **Encapsulation:** Private attributes with property decorators
- **Inheritance:** `SavingsAccount`, `CurrentAccount`, and `FixedAccount` extend `Account`
- **Polymorphism:** Overridden methods like `withdraw()` and `calculate_interest()`
- **Composition & Aggregation:** `Bank` class manages `Customer` and `Account` objects

---

## 🖥️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/NazarAbbas12/bank-management-system.git
   cd bank-management-system
   ```
2. Run the program:
```bash
python main.py
```

📌 Notes

- Interest can be calculated for both Savings and Fixed accounts.

- Current account does not support interest by default.

- Input validation can be improved for more robust applications.

🤝 Contributing

Contributions, feedback, or suggestions are welcome! Feel free to fork this project or open an issue.

📬 Contact

Developed by Nazar Abbas

📧 Email: [nazarabbasmm4@gmail.com]

🔗 LinkedIn: https://www.linkedin.com/in/nazar-abbas-60170b340/


