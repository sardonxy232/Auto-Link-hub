<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AgriLink Hub Documentation</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      background-color: #fdfaf6;
      color: #333;
      margin: 0;
      padding: 0;
    }
    header {
      background-color: #4CAF50;
      color: white;
      padding: 2rem;
      text-align: center;
    }
    main {
      max-width: 1000px;
      margin: 2rem auto;
      padding: 1rem 2rem;
      background-color: #fff;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      border-radius: 8px;
    }
    h1, h2, h3 {
      color: #2e7d32;
    }
    code {
      background-color: #f4f4f4;
      padding: 2px 4px;
      border-radius: 4px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #4CAF50;
      color: white;
    }
    pre {
      background-color: #f4f4f4;
      padding: 1rem;
      overflow-x: auto;
      border-radius: 4px;
    }
    section {
      margin-bottom: 2rem;
    }
  </style>
</head>
<body>
  <header>
    <h1>🌾 AgriLink Hub</h1>
    <p>A farming and food supply chain platform connecting farmers, buyers, suppliers, and logistics providers.</p>
  </header>

  <main>
    <section>
      <h2>Main Features</h2>
      <ul>
        <li><strong>Authentication & User Management:</strong> Farmers, buyers, suppliers, and logistics partners can register with JWT-based authentication and role-based profiles.</li>
        <li><strong>Farmer Produce Listings:</strong> Farmers can list crops (type, quantity, price, location). Buyers can search/filter crops.</li>
        <li><strong>Supplier Listings:</strong> Suppliers list tools, fertilizers, pesticides, etc. Buyers/farmers can order supplies.</li>
        <li><strong>Orders & Transactions:</strong> Buyers can order crops directly from farmers. Farmers can order supplies from suppliers. Order tracking is included.</li>
        <li><strong>Logistics Integration:</strong> Logistics partners list delivery services. Delivery tracking available.</li>
        <li><strong>Reviews & Ratings:</strong> Buyers review farmers & logistics services. Farmers review suppliers & buyers.</li>
      </ul>
    </section>

    <section>
      <h2>Technology Stack</h2>
      <ul>
        <li>Backend Framework: Django REST Framework / FastAPI</li>
        <li>Authentication: JWT</li>
        <li>Database: PostgreSQL (production), SQLite (development)</li>
        <li>Optional APIs: Paystack / Flutterwave for payments, Google Maps API for location-based services</li>
      </ul>
    </section>

    <section>
      <h2>Project Structure</h2>
      <pre>
agrilink_hub/
│── manage.py
│── requirements.txt
│
├── agrilink/                
│   ├── settings.py
│   ├── urls.py
│
├── apps/
│   ├── users/               
│   ├── produce/             
│   ├── suppliers/           
│   ├── orders/              
│   ├── logistics/           
│   ├── reviews/             
│
├── tests/                   
├── docs/                    
└── scripts/                 
      </pre>
    </section>

    <section>
      <h2>Development Timeline</h2>
      <ul>
        <li><strong>Week 1:</strong> Setup, database, authentication, role-based profiles</li>
        <li><strong>Week 2:</strong> Crop & supplier listings, search & filters</li>
        <li><strong>Week 3:</strong> Orders, logistics services, tracking</li>
        <li><strong>Week 4:</strong> Reviews, payments, Google Maps, API docs & testing</li>
      </ul>
    </section>

    <section>
      <h2>Entity Relationship Overview</h2>
      <ul>
        <li>Users: Farmers, Buyers, Suppliers, Logistics Partners</li>
        <li>Produce: Belongs to Farmer</li>
        <li>Supplier Products: Belongs to Supplier</li>
        <li>Orders: Linked to Buyers, Produce, or Supplier Products</li>
        <li>Logistics Services: Linked to Orders for delivery</li>
        <li>Reviews: Linked to Users, Produce, Supplier Products, or Logistics Services</li>
      </ul>
    </section>

    <section>
      <h2>API Endpoints</h2>

      <h3>Authentication & User Management</h3>
      <table>
        <tr>
          <th>Method</th><th>Endpoint</th><th>Description</th><th>Auth Required</th>
        </tr>
        <tr><td>POST</td><td>/api/auth/register</td><td>Register new user</td><td>No</td></tr>
        <tr><td>POST</td><td>/api/auth/login</td><td>Login and get JWT token</td><td>No</td></tr>
        <tr><td>GET</td><td>/api/users/:id</td><td>Get user profile</td><td>Yes</td></tr>
        <tr><td>PUT</td><td>/api/users/:id</td><td>Update profile</td><td>Yes</td></tr>
        <tr><td>DELETE</td><td>/api/users/:id</td><td>Delete account</td><td>Yes</td></tr>
      </table>

      <h3>Farmer Produce Listings</h3>
      <table>
        <tr>
          <th>Method</th><th>Endpoint</th><th>Description</th><th>Auth Required</th>
        </tr>
        <tr><td>POST</td><td>/api/produce</td><td>Create produce listing</td><td>Yes (Farmer)</td></tr>
        <tr><td>GET</td><td>/api/produce</td><td>Get all produce</td><td>No</td></tr>
        <tr><td>GET</td><td>/api/produce/:id</td><td>Get single produce listing</td><td>No</td></tr>
        <tr><td>PUT</td><td>/api/produce/:id</td><td>Update listing</td><td>Yes (Owner)</td></tr>
        <tr><td>DELETE</td><td>/api/produce/:id</td><td>Delete listing</td><td>Yes (Owner/Admin)</td></tr>
      </table>

      <h3>Supplier Listings</h3>
      <table>
        <tr>
          <th>Method</th><th>Endpoint</th><th>Description</th><th>Auth Required</th>
        </tr>
        <tr><td>POST</td><td>/api/suppliers/products</td><td>Create product listing</td><td>Yes (Supplier)</td></tr>
        <tr><td>GET</td><td>/api/suppliers/products</td><td>Get all products</td><td>No</td></tr>
        <tr><td>GET</td><td>/api/suppliers/products/:id</td><td>Get single product</td><td>No</td></tr>
        <tr><td>PUT</td><td>/api/suppliers/products/:id</td><td>Update listing</td><td>Yes (Owner)</td></tr>
        <tr><td>DELETE</td><td>/api/suppliers/products/:id</td><td>Delete listing</td><td>Yes (Owner/Admin)</td></tr>
      </table>

      <h3>Orders</h3>
      <table>
        <tr>
          <th>Method</th><th>Endpoint</th><th>Description</th><th>Auth Required</th>
        </tr>
        <tr><td>POST</td><td>/api/orders</td><td>Create order</td><td>Yes</td></tr>
        <tr><td>GET</td><td>/api/orders</td><td>Get all orders for user</td><td>Yes</td></tr>
        <tr><td>GET</td><td>/api/orders/:id</td><td>Get single order</td><td>Yes</td></tr>
        <tr><td>PUT</td><td>/api/orders/:id</td><td>Update order status</td><td>Yes</td></tr>
        <tr><td>DELETE</td><td>/api/orders/:id</td><td>Cancel order</td><td>Yes</td></tr>
      </table>

      <h3>Logistics Services</h3>
      <table>
        <tr>
          <th>Method</th><th>Endpoint</th><th>Description</th><th>Auth Required</th>
        </tr>
        <tr><td>POST</td><td>/api/logistics</td><td>Create service listing</td><td>Yes (Partner)</td></tr>
        <tr><td>GET</td><td>/api/logistics</td><td>Get all services</td><td>No</td></tr>
        <tr><td>GET</td><td>/api/logistics/:id</td><td>Get service details</td><td>No</td></tr>
        <tr><td>PUT</td><td>/api/logistics/:id</td><td>Update service</td><td>Yes (Owner)</td></tr>
        <tr><td>DELETE</td><td>/api/logistics/:id</td><td>Delete service</td><td>Yes (Owner/Admin)</td></tr>
      </table>

      <h3>Reviews</h3>
      <table>
        <tr>
          <th>Method</th><th>Endpoint</th><th>Description</th><th>Auth Required</th>
        </tr>
        <tr><td>POST</td><td>/api/reviews</td><td>Post a review</td><td>Yes</td></tr>
        <tr><td>GET</td><td>/api/reviews</td><td>Get all reviews</td><td>No</td></tr>
        <tr><td>PUT</td><td>/api/reviews/:id</td><td>Update review</td><td>Yes (Owner)</td></tr>
        <tr><td>DELETE</td><td>/api/reviews/:id</td><td>Delete review</td><td>Yes (Owner/Admin)</td></tr>
      </table>
    </section>

    <section>
      <h2>Author</h2>
      <p><strong>Joshua Olayiwola</strong> – Full-Stack (Backend Focus)<br>Date: 29 August 2025</p>
    </section>
  </main>
</body>
</html>