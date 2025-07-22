# 📬 Messaging App

A secure messaging application built with Django and Django REST Framework that supports user registration, login via JWT, real-time-like conversations, message handling, permissions, pagination, and filtering.

---

## 🚀 Features

- 🔐 **JWT Authentication** (using `djangorestframework-simplejwt`)
- 👤 Custom User Model (UUID-based)
- 💬 Create Conversations & Send Messages
- 🔒 Permissions: Only participants can access their conversations/messages
- 📃 Pagination: Fetch 20 messages per page
- 🔎 Filtering: Filter messages by time range and conversation
- 🧪 API tested with Postman

---

## 🛠️ Tech Stack

- Django
- Django REST Framework (DRF)
- djangorestframework-simplejwt
- django-filter
- SQLite (for development)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/alx-backend-python.git
cd alx-backend-python/messaging_app
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

---

## ⚙️ Setup

### 1. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

### 3. Run Development Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication

### Register

`POST /api/auth/register/`

```json
{
  "email": "user@example.com",
  "username": "john_doe",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "1234567890"
}
```

### Login (returns JWT tokens)

`POST /api/auth/login/`

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

> Use `Authorization: Bearer <access>` in headers for protected routes.

---

## 📩 Conversations & Messages

### Create Conversation

`POST /api/conversations/`

### Send Message

`POST /api/messages/`

```json
{
  "conversation": "uuid-of-conversation",
  "message_body": "Hello!"
}
```

### Get Messages (Paginated & Filtered)

`GET /api/messages/?conversation=<uuid>&sent_at__gte=2024-01-01&sent_at__lte=2024-12-31&page=1`

---

## 🔒 Permissions

- Only authenticated users can access APIs.
- Only participants of a conversation can:

  - View, send, update or delete messages.
  - Access specific conversations.

---

## ⚙️ Configuration

### `settings.py` Highlights

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'chats.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

---

## 🧪 Testing with Postman

Test all endpoints with Postman:

- Register/Login
- Auth token usage
- Conversations and messages CRUD
- Pagination and filtering

Collection: `/postman-collections/messaging_app.json` (Create this if needed)

---

## 📁 Project Structure

```
messaging_app/
│
├── chats/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── auth.py
│   ├── permissions.py
│   ├── pagination.py
│   └── filters.py
│
├── messaging_app/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── requirements.txt
```

---

## ✅ To Do

- ✅ JWT Auth
- ✅ Custom Permissions
- ✅ Pagination & Filters
- ✅ Postman Testing
