# 🌾 AgriLink Hub

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)](https://www.djangoproject.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.101-lightblue?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

AgriLink Hub is a **farming and food supply chain platform** connecting farmers, buyers, suppliers, and logistics providers in one ecosystem.  
It simplifies selling, buying, and delivering farm produce and agricultural tools.

---

## 🚀 Features

<details>
<summary>Authentication & User Management</summary>

- Farmers, buyers, suppliers, and logistics partners can register
- JWT-based authentication
- Role-based user profiles
</details>

<details>
<summary>Farmer Produce Listings</summary>

- Farmers can list crops with type, quantity, price, and location  
- Buyers can search and filter crops
</details>

<details>
<summary>Supplier Listings</summary>

- Suppliers list farming tools, fertilizers, pesticides, etc.  
- Buyers/farmers can order supplies
</details>

<details>
<summary>Orders & Transactions</summary>

- Buyers order crops directly from farmers  
- Farmers order supplies from suppliers  
- Order tracking and management
</details>

<details>
<summary>Logistics Integration</summary>

- Logistics partners list delivery services  
- Farmers and buyers request delivery  
- Delivery status tracking
</details>

<details>
<summary>Reviews & Ratings</summary>

- Buyers review farmers & logistics services  
- Farmers review suppliers & buyers
</details>

---

## ⚙️ Technology Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django REST Framework / FastAPI |
| Database | PostgreSQL (production) / SQLite (development) |
| Authentication | JWT |
| Payment (optional) | Paystack / Flutterwave |
| Maps / Location | Google Maps API |

---

## 🏗 Project Structure

agrilink_hub/
│── manage.py
│── requirements.txt
│
├── agrilink/
│ ├── settings.py
│ ├── urls.py
│
├── apps/
│ ├── users/
│ ├── produce/
│ ├── suppliers/
│ ├── orders/
│ ├── logistics/
│ ├── reviews/
│
├── tests/
├── docs/
└── scripts/

pgsql
Copy code

---

## 🗓 Development Timeline

| Week | Task |
|------|------|
| 1 | Setup project, environment, database, authentication, role-based profiles |
| 2 | Crop & supplier listings, filtering & search |
| 3 | Orders, logistics services, order & delivery tracking |
| 4 | Reviews, payment integration, Google Maps (optional), API docs & testing |

---

## 🖥 API Endpoints

<details>
<summary>Authentication & Users</summary>

| Method | Endpoint | Description | Auth |
|--------|---------|-------------|------|
| POST   | /api/auth/register | Register new user | No |
| POST   | /api/auth/login    | Login & get JWT | No |
| GET    | /api/users/:id     | Get user profile | Yes |
| PUT    | /api/users/:id     | Update profile | Yes |
| DELETE | /api/users/:id     | Delete account | Yes |
</details>

<details>
<summary>Farmer Produce</summary>

| Method | Endpoint | Description | Auth |
|--------|---------|-------------|------|
| POST   | /api/produce | Create produce listing | Yes (Farmer) |
| GET    | /api/produce | Get all produce | No |
| GET    | /api/produce/:id | Get single produce | No |
| PUT    | /api/produce/:id | Update listing | Yes (Owner) |
| DELETE | /api/produce/:id | Delete listing | Yes (Owner/Admin) |
</details>

<details>
<summary>Supplier Products</summary>

| Method | Endpoint | Description | Auth |
|--------|---------|-------------|------|
| POST   | /api/suppliers/products | Create listing | Yes (Supplier) |
| GET    | /api/suppliers/products | Get all products | No |
| GET    | /api/suppliers/products/:id | Get single product | No |
| PUT    | /api/suppliers/products/:id | Update listing | Yes (Owner) |
| DELETE | /api/suppliers/products/:id | Delete listing | Yes (Owner/Admin) |
</details>

<details>
<summary>Orders</summary>

| Method | Endpoint | Description | Auth |
|--------|---------|-------------|------|
| POST   | /api/orders | Create order | Yes |
| GET    | /api/orders | Get all orders | Yes |
| GET    | /api/orders/:id | Get single order | Yes |
| PUT    | /api/orders/:id | Update status | Yes |
| DELETE | /api/orders/:id | Cancel order | Yes |
</details>

<details>
<summary>Logistics & Reviews</summary>

- **Logistics Services:** POST /api/logistics, GET /api/logistics, PUT/DELETE for owner/admin  
- **Reviews:** POST /api/reviews, GET /api/reviews, PUT/DELETE for owner/admin
</details>

---

## 📌 Author

**Joshua Olayiwola** – Full-Stack (Backend Focus)  
**Date:** 29 August 2025