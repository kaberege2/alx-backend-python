# Context Managers and Asynchronous Programming in Python

This project demonstrates the use of **class-based context managers** and **asynchronous programming** using `asyncio` and `aiosqlite` in Python. It is part of the ALX Backend Specialization curriculum.

## 📁 Project Structure

python-context-async-perations-0x02/
├── 0-databaseconnection.py
├── 1-execute.py
├── 3-concurrent.py
└── README.md

---

## 📌 Tasks Overview

### ✅ Task 0: Custom Database Context Manager

**File:** `0-databaseconnection.py`  
Creates a class-based context manager `DatabaseConnection` that automatically opens and closes a SQLite connection.

- Performs the query: `SELECT * FROM users`
- Results are printed inside the context block

### ✅ Task 1: Reusable Query Context Manager

**File:** `1-execute.py`  
Defines a reusable context manager `ExecuteQuery` that accepts a SQL query and parameters, executes it, and returns the results.

- Executes: `SELECT * FROM users WHERE age > ?` with parameter `25`
- Connection is managed internally using `__enter__` and `__exit__`

### ✅ Task 2: Concurrent Asynchronous Queries

**File:** `3-concurrent.py`  
Uses `aiosqlite` and `asyncio.gather()` to run two queries concurrently:

- `async_fetch_users()`: Fetches all users
- `async_fetch_older_users()`: Fetches users older than 40
- Results from both queries are printed concurrently using `asyncio.run()`

---

## 📦 Requirements

- Python 3.7+
- `aiosqlite` (Install with: `pip install aiosqlite`)

---

## 🧪 Example Usage

To run any script:

```bash
python3 0-databaseconnection.py
python3 1-execute.py
python3 3-concurrent.py
📙 Notes
Make sure a users table exists in my_database.db

You can modify the database name in each script or generalize it further

These tasks demonstrate how to manage resources cleanly and run database operations efficiently using both synchronous and asynchronous techniques
```
