# Python Frameworks and Important Libraries: Coding Challenges

These challenges are designed to give hands-on experience with popular Python frameworks and libraries. Each task focuses on real-world usage patterns to reinforce practical understanding.

---

## Challenge 1: Flask API

**Objective**: Create a minimal Flask REST API with one GET and one POST endpoint.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

data = []

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(data)

@app.route("/items", methods=["POST"])
def add_item():
    item = request.json.get("item")
    data.append(item)
    return {"message": "Added"}, 201

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Challenge 2: Django Model and Admin

**Objective**: Define a `Book` model and register it in Django admin.

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published = models.DateField()
```

```python
# admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

---

## Challenge 3: FastAPI with Pydantic

**Objective**: Build a FastAPI app that uses a Pydantic model for validation.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
async def create_user(user: User):
    return {"received": user.dict()}
```

---

## Challenge 4: NumPy Array Operations

**Objective**: Create a 2D array and apply vectorized math.

```python
import numpy as np

a = np.arange(9).reshape(3, 3)
b = a * 2
assert b[0, 0] == 0
assert b[1, 1] == 8
```

---

## Challenge 5: pandas DataFrame Filtering

**Objective**: Load data and filter rows based on a condition.

```python
import pandas as pd

df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
older = df[df.age > 26]
assert older.iloc[0]["name"] == "Bob"
```

---

## Challenge 6: scikit-learn Model Training

**Objective**: Train a simple classifier.

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = RandomForestClassifier().fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
assert 0 <= accuracy <= 1
```

---

## Challenge 7: Click CLI Command

**Objective**: Create a CLI tool that accepts a name and prints a greeting.

```python
import click

@click.command()
@click.argument("name")
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    greet()
```

---

## Challenge 8: Docker Control with SDK

**Objective**: List Docker containers using Python.

```python
import docker

client = docker.from_env()
containers = client.containers.list()
print([c.name for c in containers])
```

---

## Challenge 9: requests HTTP Call

**Objective**: Fetch JSON from an API.

```python
import requests

resp = requests.get("https://api.github.com")
data = resp.json()
assert "current_user_url" in data
```

---

## Challenge 10: matplotlib Plot

**Objective**: Create a basic line plot.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("plot.png")
```
