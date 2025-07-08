# Python Decorators - Database Enhancements

This project demonstrates how to use Python decorators to enhance database operations in a clean, reusable, and modular way. It is part of the ALX Backend curriculum and focuses on real-world applications of decorators in SQLite-based systems.

## 📌 Project Overview

The goal is to implement custom decorators that:

- Log SQL queries
- Handle database connections automatically
- Manage transactions safely
- Retry failed operations
- Cache query results

All operations are tested against a SQLite3 database with a `users` table.

---

## ✅ Learning Objectives

By completing this project, you will:

- Deepen your understanding of Python decorators
- Automate and simplify common database tasks
- Improve error handling and transaction safety
- Boost performance via query caching
- Apply best practices for clean, maintainable backend code

---

## 🗃️ Project Structure

```

python-decorators-0x01/
├── 0-log_queries.py # Logs SQL queries before execution
├── 1-with_db_connection.py # Opens and closes DB connection automatically
├── 2-transactional.py # Commits or rolls back transactions
├── 3-retry_on_failure.py # Retries query execution on transient failure
├── 4-cache_query.py # Caches SQL query results
└── README.md # Project documentation

```

---

## 🛠️ Requirements

- Python 3.8+
- SQLite3
- A `users.db` file with a table `users` having at least:
  ```sql
  CREATE TABLE users (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      email TEXT NOT NULL
  );
  ```

````

---

## 🧪 Example Usage

```bash
# Task 0: Logs the SQL query
$ python3 0-log_queries.py
Executing SQL Query: SELECT * FROM users

# Task 1: Auto connection
$ python3 1-with_db_connection.py
(1, 'Jane Doe', 'jane@example.com')

# Task 4: Caching
$ python3 4-cache_query.py
Returning cached result
```

---

## 💡 Tips

- Use `functools.wraps` in decorators to preserve metadata
- Make decorators stackable (e.g., `@with_db_connection @retry_on_failure`)
- Use `kwargs.get('query')` or `args[0]` for query extraction in decorators
````
