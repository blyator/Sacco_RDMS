# Sacco RDMS

## Overview

This is a custom-built Relational Database Management System (RDBMS) implemented in Python, specifically designed for managing a Savings and Credit Cooperative (Sacco). It provides a complete in-memory database engine, SQL-like command-line interface, RESTful API via Flask and a modern React-based web frontend.

The system impliments core RDBMS concepts like table schemas, CRUD operations, indexing, constraints and basic joins. 

## Features

### Core Database Engine
- **Table Declaration**: Define tables with typed columns (int, str) and constraints
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Indexing**: Automatic indexing on primary and unique keys
- **Key Constraints**: Strict enforcement of primary and unique key integrity
- **Join Operations**: Inner joins between tables 
- **In-Memory Storage**: Fast, volatile data storage with no disk persistence

### Interfaces
- **SQL-like REPL**: Interactive command-line interface with parsed SQL commands
- **REST API**: Flask-based HTTP API for programmatic access
- **Web Frontend**: React with DaisyUI components
- **Transaction Support**: Built-in deposit/withdrawal logic with balance validation


## System Requirements

- **Python**: 3.8 or higher
- **Node.js**: 16+ (for frontend development)
- **Operating System**: Linux, macOS, or Windows
- **Dependencies**: Flask (Python), React (Node.js)

## Installation

### 1. Clone Repository
```bash
git clone <repository-url>
cd sacco-rdms
```

### 2. Python Setup
```bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install flask
```

### 3. Frontend Setup
```bash
cd frontend
npm install
cd ..
```

### 4. Verify Installation
```bash
# Test Python import
python -c "from db.database import Database; print('Database import successful')"

# Test Flask app
python -m web.app  # Should start server on port 5000
```

## Database Schema

The system implements a normalized schema for Sacco management:

### Members Table
```sql
CREATE TABLE members (
    member_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    national_id VARCHAR(20) UNIQUE NOT NULL
);
```
- **Purpose**: Stores basic member information
- **Constraints**: Primary key on member_id, unique on national_id
- **Relationships**: Referenced by accounts table

### Accounts Table
```sql
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    member_id INT NOT NULL,
    balance INT DEFAULT 0
);
```
- **Purpose**: Manages member account balances
- **Constraints**: Primary key on account_id
- **Relationships**: Foreign key reference to members.member_id

### Transactions Table
```sql
CREATE TABLE transactions (
    txn_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    txn_type ENUM('deposit', 'withdraw') NOT NULL,
    amount INT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
- **Purpose**: Audit trail for all account transactions
- **Constraints**: Primary key on txn_id
- **Relationships**: References accounts.account_id

## Usage Guide

### Command-Line REPL

The REPL provides an interactive SQL-like interface for direct database manipulation.

#### Starting the REPL
```bash
python db/repl.py
```

#### Supported Commands

**INSERT Operations:**
```sql
INSERT INTO members VALUES (1, 'Billy', 'ID123456');
INSERT INTO accounts VALUES (1, 1, 1000);
```
- Values must match column order
- Strings should be quoted
- Auto-conversion for numeric types

**SELECT Queries:**
```sql
SELECT * FROM members;
SELECT * FROM accounts WHERE member_id = 1;
```
- Supports WHERE clauses with equality conditions
- Returns formatted result sets

**UPDATE Operations:**
```sql
UPDATE accounts SET balance = 1500 WHERE account_id = 1;
```
- Single column updates with WHERE conditions
- Type conversion for numeric values

**DELETE Operations:**
```sql
DELETE FROM members WHERE member_id = 1;
```


#### REPL Examples
```
> INSERT INTO members VALUES (1, 'Billy', 'NJ123456')
members row inserted successfully

> SELECT * FROM members WHERE member_id=1
[{'member_id': 1, 'name': 'Billy', 'national_id': 'NJ123456'}]

> exit
```

### REST API

The Flask API provides HTTP endpoints for programmatic access.

#### Starting the Server
```bash
python -m web.app
```
Server runs on `http://localhost:5000` by default.

#### API Endpoints

**Members Endpoints:**

`POST /members`
- **Purpose**: Register a new member
- **Request Body**:
```json
{
  "member_id": 2,
  "name": "kip",
  "national_id": "BS789012"
}
```
- **Response**: `{"status": "success"}` or error details
- **Validation**: Checks for duplicate IDs and national IDs

`GET /members`
- **Purpose**: Retrieve all members
- **Response**:
```json
[
  {
    "member_id": 1,
    "name": "Billy",
    "national_id": "NJ123456"
  }
]
```

**Accounts Endpoints:**

`POST /accounts`
- **Purpose**: Create a new account
- **Request Body**:
```json
{
  "account_id": 1,
  "member_id": 1,
  "balance": 500
}
```
- **Response**: `{"status": "success"}` or validation errors
- **Validation**: Ensures member exists

`GET /accounts`
- **Purpose**: List all accounts
- **Response**: Array of account objects with balances

**Transactions Endpoints:**

`POST /transactions`
- **Purpose**: Execute deposit or withdrawal
- **Request Body**:
```json
{
  "account_id": 1,
  "txn_type": "deposit",
  "amount": 200
}
```
- **Response**: Success message with new balance
- **Logic**: Updates account balance, logs transaction

`GET /transactions?account_id=1`
- **Purpose**: Get transaction history for an account
- **Response**: Array of transaction records

#### API Usage Examples
```bash
# Add a member
curl -X POST http://localhost:5000/members \
  -H "Content-Type: application/json" \
  -d '{"member_id": 1, "name": "Billy", "national_id": "ID001"}'

# Get all members
curl http://localhost:5000/members

# Add an account
curl -X POST http://localhost:5000/accounts \
  -H "Content-Type: application/json" \
  -d '{"account_id": 1, "member_id": 1, "balance": 1000}'
```

### Web Frontend

A modern React application provides a graphical interface for database management.

#### Starting the Frontend
```bash
cd frontend
npm run dev
```
Opens at `http://localhost:5173`.


#### Interface Components
- **Add Member Form**: Input fields for member details
- **Member List**: Display table with search/filter
- **Add Account Form**: Account creation with member validation
- **Account Overview**: Balance tracking and transaction history

## Testing

### Running Tests
```bash
python test.py
```

### Test Coverage
- Database table creation and constraints
- CRUD operations with various data types
- Index performance and correctness
- Join operations between tables
- API endpoint functionality
- Error handling and edge cases


## Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit pr


## License

This project is licensed under the MIT License - see the LICENSE file for details.



---

For questions or support, please open an issue in the repository.