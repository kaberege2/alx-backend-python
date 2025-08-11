# 📬 Messaging App (Kubernetes-Ready)

A secure messaging application built with Django and Django REST Framework, now containerized with Docker and orchestrated using Kubernetes. Supports user registration, JWT-based authentication, conversations, message handling, custom permissions, pagination, and filtering.

---

## 🚀 Features

- 🔐 **JWT Authentication** (using `djangorestframework-simplejwt`)
- 👤 Custom User Model (UUID-based)
- 💬 Conversations & Messaging System
- 🔒 Fine-grained Permissions (only participants access conversations/messages)
- 📃 Pagination (20 messages per page)
- 🔎 Filtering (by date range & conversation)
- 🐳 Fully Dockerized & Kubernetes Deployable
- 🧪 API tested with Postman

---

## 🛠️ Tech Stack

- Django 5.2
- Django REST Framework (DRF)
- SimpleJWT
- django-filter
- MySQL
- Docker & Docker Compose
- Kubernetes (Deployments, Services, ConfigMaps, Secrets, Persistent Volumes)

---

## 📦 Local Setup with Docker

Follow the same steps as before (clone repo, create `.env`, build & run with Docker Compose).

---

## ☸️ Kubernetes Deployment

### 1. Build & Push Image

```bash
docker build -t <dockerhub-username>/messaging-app:latest .
docker push <dockerhub-username>/messaging-app:latest
```

### 2. Apply Kubernetes Configurations

```bash
kubectl apply -f k8s/mysql-secret.yaml
kubectl apply -f k8s/mysql-configmap.yaml
kubectl apply -f k8s/mysql-pvc.yaml
kubectl apply -f k8s/mysql-deployment.yaml
kubectl apply -f k8s/django-secret.yaml
kubectl apply -f k8s/django-deployment.yaml
kubectl apply -f k8s/django-service.yaml
```

### 3. Run Migrations

```bash
kubectl exec -it <django-pod-name> -- python manage.py migrate
```

### 4. (Optional) Create Superuser

```bash
kubectl exec -it <django-pod-name> -- python manage.py createsuperuser
```

---

## 🗃️ Data Persistence

- MySQL uses a PersistentVolumeClaim to ensure data survives pod restarts.

---

## 🧪 API Testing

- Use Postman with Kubernetes service URLs or port-forwarding.

```bash
kubectl port-forward svc/django-service 8000:8000
```

Then test APIs locally at `http://localhost:8000/api/...`
