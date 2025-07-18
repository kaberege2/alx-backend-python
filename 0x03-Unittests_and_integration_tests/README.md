# 0x03. Unittests and Integration Tests

This project is part of the ALX Backend Specialization. It focuses on writing and executing **unit tests** and **integration tests** for Python applications using `unittest`, `parameterized`, and `mock`.

---

## 📚 Learning Objectives

By the end of this project, you should be able to:

- Differentiate between unit and integration tests
- Use `unittest` to write test cases in Python
- Use `mock` and `patch` to replace external calls with fake data
- Use `parameterized` to test multiple inputs and expected outputs
- Write integration tests that test actual code paths with minimal mocking
- Apply memoization techniques and verify their behavior using tests

---

## 📁 Files Included

### 🔹 utils.py

Contains utility functions:

- `access_nested_map`
- `get_json`
- `memoize` decorator

### 🔹 client.py

Defines `GithubOrgClient`, which:

- Fetches organization details from GitHub
- Lists public repositories
- Filters repos by license

### 🔹 fixtures.py

Includes mocked JSON payloads used in integration tests for:

- GitHub organization data
- Repository lists

### 🔹 test_utils.py

Contains unit tests for:

- `access_nested_map`
- `get_json`
- `memoize`

### 🔹 test_client.py

Contains both unit and integration tests for:

- `GithubOrgClient` class methods like `org`, `public_repos`, `has_license`

---

## 🧪 Running the Tests

Run any test file using:

```bash
python3 -m unittest test_utils.py
python3 -m unittest test_client.py
```
