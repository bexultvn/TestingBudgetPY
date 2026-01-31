# TestingBudgetPY — Automated Testing Project (pytest)

**TestingBudgetPY** is an automated testing project for a console-based Python application that manages a personal budget.  
The repository demonstrates a complete **QA Automation workflow** using **pytest**.

The project focuses on testing business logic, data persistence, and edge cases, and is intended for **educational and portfolio purposes**.

---

##  Tech Stack

- **Programming Language:** Python 3.10+
- **Testing Framework:** pytest
- **Test Coverage:** pytest-cov
- **Test Types:** unit, integration, negative, boundary testing
- **Data Storage:** JSON
- **Environment:** virtual environment (venv)
- **Version Control:** Git, GitHub

---

## Application Overview

The application provides the following functionality:
- user balance management;
- income and expense tracking;
- transaction categorization;
- savings goals management;
- data persistence using JSON files.

---

## Testing Scope

### Types of Testing

The project includes:
- Unit testing;
- Integration testing;
- Negative testing;
- Boundary value testing.

### Covered Modules

| Module | Status |
|------|------|
| Account (balance) | Tested |
| Transactions | Tested |
| Categories | Tested |
| Savings | Tested |
| JSON Storage | Tested |
| State persistence | Tested |

---

## Project Structure

```text
TestingBudgetPY/
├── src/
│   ├── core/
│   ├── models/
│   ├── storage/
│   └── __init__.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── docs/
│   ├── requirements.md
│   ├── test_plan.md
│   └── test_conclusion.md
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
