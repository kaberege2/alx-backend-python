# 📬 Messaging App (Kubernetes-Ready + CI/CD)

A secure messaging application built with Django and Django REST Framework, containerized with Docker, orchestrated with Kubernetes, and now fully integrated with CI/CD pipelines using **Jenkins** and **GitHub Actions**.

Supports user registration, JWT-based authentication, conversations, message handling, custom permissions, pagination, and filtering.

---

## 🚀 Features

- 🔐 **JWT Authentication** (using `djangorestframework-simplejwt`)
- 👤 Custom User Model (UUID-based)
- 💬 Conversations & Messaging System
- 🔒 Fine-grained Permissions (only participants access conversations/messages)
- 📃 Pagination (20 messages per page)
- 🔎 Filtering (by date range & conversation)
- 🐳 Fully Dockerized & Kubernetes Deployable
- ⚙️ CI/CD with Jenkins & GitHub Actions
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
- Jenkins (pipeline automation)
- GitHub Actions (testing, linting, coverage, Docker builds)

---

## 📦 Local Setup with Docker

Follow the same steps as before (clone repo, create `.env`, build & run with Docker Compose).

```bash
git clone https://github.com/kaberege2/alx-backend-python.git
cd alx-backend-python/messaging_app
docker-compose up --build
```

---

## ☸️ Kubernetes Deployment

### 1. Build & Push Image

```bash
docker build -t dockerhub-xxxxx/messaging-app:latest .
docker push dockerhub-xxxxx/messaging-app:latest
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

---

## ⚙️ CI/CD Pipelines

This project includes **two CI/CD setups**:

### 🔹 Jenkins Pipeline

- Installed via Docker (`jenkins/jenkins:lts`)
- Pipeline defined in `messaging_app/Jenkinsfile`
- **Stages**:

  1. Checkout code from GitHub
  2. Install dependencies
  3. Run tests with `pytest` and generate reports
  4. Build Docker image
  5. Push Docker image to Docker Hub

Trigger manually or on each commit.

### 🔹 GitHub Actions Workflows

Located in `.github/workflows/`

- **`ci.yml`** → Runs on every push & pull request

  - Linting with `flake8`
  - Unit tests with `pytest`
  - Coverage reports (uploaded as artifacts)
  - MySQL service container for DB testing

- **`dep.yml`** → Runs on pushes to `main`

  - Builds Docker image
  - Pushes image to Docker Hub (using GitHub Secrets for credentials)

---

## 🔑 Secrets & Credentials

- **Jenkins**:

  - GitHub credentials (`github-credentials`)
  - Docker Hub credentials (`dockerhub-credentials`)

- **GitHub Actions**:

  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN`
