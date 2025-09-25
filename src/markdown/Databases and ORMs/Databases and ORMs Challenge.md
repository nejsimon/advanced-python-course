# Coding Challenges: Databases and ORMs

These challenges are designed to help you practice Python database access, SQLAlchemy Core, and ORM features.

---

## Challenge 1: SQLite Basics

1. Create an in-memory SQLite database with `sqlite3`.
2. Define a table `books` with columns `(id INTEGER PRIMARY KEY, title TEXT, author TEXT)`.
3. Insert three books into the table.
4. Query and print all rows.
5. Write a function that returns all books by a given author.

---

## Challenge 2: SQLAlchemy Core

1. Using SQLAlchemy Core, define a `products` table with columns:

   * `id` (integer primary key)
   * `name` (string)
   * `price` (float)
2. Insert multiple products in one call.
3. Select products where the price is greater than a given threshold.
4. Update the price of a product by name.

---

## Challenge 3: SQLAlchemy ORM Basics

1. Define a class `Customer` with fields `id` (int, PK) and `name` (string).
2. Define a class `Order` with fields `id` (int, PK), `item` (string), `customer_id` (foreign key to `Customer`).
3. Create a one-to-many relationship (`Customer.orders`).
4. Insert one customer with two orders.
5. Query the database and print all orders with their customer’s name.

---

## Challenge 4: Advanced ORM Queries

1. Extend the `Customer` and `Order` models with a `status` field for orders.
2. Insert 5 orders with different statuses (e.g., "pending", "shipped", "delivered").
3. Write queries for:

   * All customers with at least one "pending" order.
   * The number of orders per customer.
   * Orders joined with customers, eager-loaded.

---

## Challenge 5: Migrations (Conceptual)

1. Research **Alembic** (for SQLAlchemy) or **Django migrations**.
2. Define a new field `email` for the `Customer` model.
3. Describe how you would apply a migration safely to an existing production database.

---

## Challenge 6: NoSQL Access

1. Install and use `pymongo` or `motor`.
2. Create a collection `users` and insert a few documents.
3. Query for users with a specific field value.
4. Update a user document.

---

## Extra Challenge: ORM Pitfalls

1. Simulate the **N+1 query problem** with SQLAlchemy ORM.
2. Fix it using eager loading (`joinedload` or `selectinload`).

