# Rule Engine with Abstract Syntax Tree (AST)

## Description
This project is a simple rule engine that uses an Abstract Syntax Tree (AST) to determine user eligibility based on attributes like age, department, salary, and experience. The system allows for dynamic creation, combination, and evaluation of rules based on input data.

## Features
- Create rules using a string representation of logical conditions.
- Combine multiple rules into a single AST.
- Evaluate rules based on user-provided input data.
- Store rules in an SQLite database for persistence.

## Technologies Used
- Python 3.x
- SQLite (for database storage)

## Setup Instructions
### Prerequisites:
- Python 3.x must be installed on your machine.
- SQLite3 is required for database operations.

### Step-by-Step Setup:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/via23-ma/rule-engine-ast.git
   cd rule-engine-ast
2. **Run the application**: In the terminal, execute the following command to run the application:
   python main.py
3. **Database**: The application uses SQLite3 to store and retrieve rules. The database will be automatically created in the project folder as rules.db when you run the application.

# Example Usage
1. **Create a rule**:
Example rule string: "age > 30 AND department = 'Sales'"

This rule checks if a user is over 30 years old and works in the Sales department.

2. **Evaluate the rule**:
The following data will be used to evaluate the rule:
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
The rule will return True if the data matches the rule logic.

3. **Store and retrieve rules from the database**:
The rule we create will be stored in the SQLite database (rules.db). we can later retrieve and evaluate stored rules.

# Project Structure
├── main.py         # Main entry point for running the rule engine
├── rule_ast.py     # Contains the AST logic for creating and combining rules
├── database.py     # Handles rule storage in the SQLite database
├── README.md       # Project instructions and setup guide
└── rules.db        # SQLite database file (created automatically when the app runs)

# Contribution
Feel free to submit pull requests or open issues to improve the functionality or add new features.

# License
This project is licensed under the MIT License.

# GitHub Repository Link
  https://github.com/via23-ma/rule-engine-ast