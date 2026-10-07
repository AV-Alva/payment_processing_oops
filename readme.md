# Payment Processing System – Polymorphism & Abstraction in Python

## Project Description

This project is a simple Payment Processing System built using Python Object-Oriented Programming (OOP).

The main purpose of the project is to demonstrate:

- Abstraction
- Abstract Classes
- Abstract Methods
- Inheritance
- Method Overriding
- Runtime Polymorphism
- Exception Handling
- Logging
- Python Packages and Modules

The system supports three payment methods:

1. Credit Card Payment
2. UPI Payment
3. Net Banking Payment

All payment methods inherit from a common abstract `Payment` class and implement their own version of the `pay()` method.

---

## Project Structure

```text
payment_processing/
│
├── payment/
│   ├── __init__.py
│   ├── payment.py
│   ├── credit_card.py
│   ├── upi.py
│   ├── net_banking.py
│   ├── exceptions.py
│   └── logger_config.py
│
├── logs/
│   └── payment.log
│
├── main.py
├── README.md
└── .gitignore