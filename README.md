# Financial Tracker App

## Description
This Financial Tracker App is a desktop application built with Python that allows users to track their personal finances. It provides a user-friendly interface for recording transactions, viewing financial history, and generating basic reports. The app uses SQLite for local and lightweight data storage, while keeping financial data private and accessible on your personal computer.

## Features
- User authentication system
- Record income and expenses
- Categorize transactions
- View transaction history
- Generate basic financial reports
- Local data storage using SQLite

## Database

The application uses **SQLite** as its database, with **SQLAlchemy** as the ORM (Object-Relational Mapping) tool to facilitate interactions with the database. SQLAlchemy provides a high-level API for managing database operations and relationships between models.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps
1. Clone this repository:
git clone https://github.com/yourusername/financial-tracker-app.git


2. Navigate to the project directory:
cd financial-tracker


3. Create a virtual environment:
python -m venv .venv


4. Activate the virtual environment:
- On Windows:
  ```
  .venv\Scripts\activate
  (if using powershell:> .venv\Scripts\Activate.ps1)
  ```
- On macOS and Linux:
  ```
  source .venv/bin/activate
  ```

5. Install required packages:
pip install -r requirements.txt


## Usage
1. Ensure your virtual environment is activated.

2. Run the application:
python main.py


3. Register a new user account or log in with existing credentials.

4. Use the interface to add transactions, view your financial history, and generate reports.

5. When you're done, you can deactivate the virtual environment:
 (from .venv\Scripts\) type deactivate

## Database Schema
The app uses SQLite with the following main tables:
- `users`: Stores user account information
- `transactions`: Records all financial transactions
- `catetories`: Records the various categories of transactions

## Contributing
Contributions to improve the Financial Tracker App are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` file for more information.

## Contact
Alexander Creznic - alex.creznic@gmail.com

Project Link: https://github.com/exnihilo20/financial-tracker

## Acknowledgements
- [Python](https://www.python.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [PyQt](https://riverbankcomputing.com/software/pyqt/intro) (if you're using PyQt for GUI)
