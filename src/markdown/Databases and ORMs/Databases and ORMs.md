# Databases and ORMs

Databases are central to many applications, and Python provides powerful tools for working with both relational and non-relational data. This document covers core database access, database drivers, and Object-Relational Mappers (ORMs).

---

## 1. Database Access

### Standard Library: `sqlite3`

* Python ships with the `sqlite3` module for working with SQLite.
* Useful for lightweight applications, testing, and prototyping.

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # [(1, 'Alice')]

conn.close()
```

### Other Popular Database Drivers

* **PostgreSQL:** `psycopg2`, `asyncpg`
* **MySQL/MariaDB:** `mysql-connector-python`, `PyMySQL`
* **Oracle:** `cx_Oracle`
* **MongoDB (NoSQL):** `pymongo`

---

## 2. SQLAlchemy Core

* SQLAlchemy provides a flexible database abstraction layer.
* Two main APIs: **SQLAlchemy Core** and **SQLAlchemy ORM**.

```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("sqlite:///:memory:")
metadata = MetaData()

users = Table("users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)

metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(users.insert().values(name="Alice"))
    result = conn.execute(users.select())
    print(result.fetchall())  # [(1, 'Alice')]
```

---

## 3. Object-Relational Mapping (ORM)

### SQLAlchemy ORM

* Provides an abstraction over SQL.
* Map Python classes to database tables.

```python
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create and add new user
new_user = User(name="Alice")
session.add(new_user)
session.commit()

# Query
users = session.query(User).all()
print(users[0].name)  # Alice
```

### Django ORM

* Built into the Django framework.
* Class-based models, migrations, and query API.
* Example:

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
```

### Peewee ORM

* Lightweight ORM for smaller projects.
* Simpler than SQLAlchemy/Django.

---

## 4. Advanced ORM Features

* Lazy loading vs eager loading.
* Relationship mapping (one-to-many, many-to-many).
* Schema migrations (Alembic for SQLAlchemy, Django migrations).
* Custom queries and hybrid properties.

---

## 5. NoSQL ORMs and ODMs

* **MongoEngine** for MongoDB.
* **Pydantic + Beanie** for async MongoDB access.

---

## 6. Common Pitfalls

* N+1 query problem.
* Over-reliance on ORM magic vs explicit queries.
* Balancing raw SQL performance with ORM convenience.

---

## 7. Best Practices

* Use connection pooling for production.
* Always parameterize queries to avoid SQL injection.
* Keep ORM models aligned with database schema.
* Profile queries with logging/debugging tools.

---

## 8. Further Reading

* SQLAlchemy documentation: [https://docs.sqlalchemy.org](https://docs.sqlalchemy.org)
* Django ORM guide: [https://docs.djangoproject.com/en/stable/topics/db/](https://docs.djangoproject.com/en/stable/topics/db/)
* Peewee ORM: [http://docs.peewee-orm.com](http://docs.peewee-orm.com)
