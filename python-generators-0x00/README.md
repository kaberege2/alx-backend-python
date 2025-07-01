# 📦 python-generators-0x00

This project focuses on using **Python generators** to process and stream data from a MySQL database efficiently. It demonstrates key techniques like lazy loading, memory-efficient processing, and batch pagination—core skills for handling large datasets.

---

## 🚀 Project Objectives

- Set up and seed a MySQL database with user data.
- Stream database rows one by one using generators.
- Process user data in batches efficiently.
- Implement lazy pagination to simulate paginated queries.
- Compute aggregate values like average using memory-efficient streaming.

---

## 🧰 Technologies Used

- Python 3
- MySQL
- `mysql-connector-python`
- CSV for data seeding

---

## 📁 Project Structure

```bash
python-generators-0x00/
│
├── seed.py                  # Database connection, creation, and data seeding
├── 0-stream_users.py        # Generator streaming one user row at a time
├── 1-batch_processing.py    # Generator to stream users in batches and filter by age
├── 2-lazy_paginate.py       # Lazy pagination generator to load data page by page
├── 4-stream_ages.py         # Streaming user ages to compute average efficiently
├── user_data.csv            # CSV data to seed the database
├── 0-main.py                # Test script for seeding and verifying DB
├── 1-main.py                # Test script for streaming users
├── 2-main.py                # Test script for batch processing
├── 3-main.py                # Test script for lazy pagination
├── 4-main.py                # Test script for average age
└── README.md                # This file
```
