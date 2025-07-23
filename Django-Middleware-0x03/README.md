# 📬 Messaging App + Custom Middleware

A secure messaging platform built with Django and Django REST Framework. It supports JWT authentication, user role-based permissions, conversation handling, message exchange, pagination, filtering, and **custom middleware for request logging, time-based access control, rate limiting, offensive content filtering, and role enforcement**.

---

## 🚀 Features

- 🔐 **JWT Authentication** (via `djangorestframework-simplejwt`)
- 👤 Custom UUID-based User Model
- 💬 Create Conversations & Send Messages
- 🔒 Role-based Access (Admin, Moderator, User)
- 📃 Pagination: 20 messages per page
- 🔎 Filtering by time and conversation
- 🧪 API tested with Postman
- 🧩 **Custom Middleware** for:
  - Request logging
  - Time-based access restriction
  - Offensive language detection
  - Message rate-limiting by IP
  - Admin/moderator role enforcement

---

## 🛠️ Tech Stack

- Django
- Django REST Framework (DRF)
- djangorestframework-simplejwt
- django-filter
- SQLite (for local development)

---

## 📦 Installation

```bash
git clone https://github.com/kaberege/alx-backend-python.git
cd alx-backend-python/Django-Middleware-0x03
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
