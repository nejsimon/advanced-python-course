# Network Requests

Networking is a fundamental part of many applications. Python provides several built-in and third-party libraries to perform HTTP requests, handle APIs, and manage sockets for low-level networking.

---

## 1. Built-in Libraries for Networking

### `urllib`

* Python’s standard library for HTTP requests.

* Provides modules like `urllib.request`, `urllib.parse`, and `urllib.error`.

* Example:

  ```python
  import urllib.request

  response = urllib.request.urlopen("https://httpbin.org/get")
  print(response.read().decode())
  ```

* **Pros:** No external dependencies, included by default.

* **Cons:** Verbose, less user-friendly compared to modern libraries.

### `http.client`

* Lower-level HTTP library.
* Useful for fine-grained control.
* Example:

  ```python
  import http.client

  conn = http.client.HTTPSConnection("httpbin.org")
  conn.request("GET", "/get")
  response = conn.getresponse()
  print(response.status, response.read().decode())
  ```

---

## 2. `requests` Library (3rd Party)

* De facto standard for HTTP requests in Python.

* Simple, powerful, and widely used.

* Example:

  ```python
  import requests

  response = requests.get("https://httpbin.org/get")
  print(response.json())
  ```

* Supports:

  * GET, POST, PUT, DELETE, PATCH
  * Automatic JSON decoding
  * Session handling
  * Cookies and headers
  * Streaming downloads

---

## 3. Asynchronous Networking

### `aiohttp`

* Async HTTP client/server library.

* Integrates with `asyncio`.

* Example:

  ```python
  import aiohttp
  import asyncio

  async def fetch():
      async with aiohttp.ClientSession() as session:
          async with session.get("https://httpbin.org/get") as response:
              print(await response.json())

  asyncio.run(fetch())
  ```

* **Pros:** Efficient for concurrent requests.

* **Cons:** Requires async/await, more complex for beginners.

### `httpx`

* Alternative to `requests` with sync + async support.
* Example:

  ```python
  import httpx

  response = httpx.get("https://httpbin.org/get")
  print(response.json())
  ```

---

## 4. Low-Level Networking with `socket`

* Provides direct TCP/UDP socket programming.

* Example TCP client:

  ```python
  import socket

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("example.com", 80))
  s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
  data = s.recv(1024)
  print(data.decode())
  s.close()
  ```

* Useful for building custom protocols.

---

## 5. Handling Errors and Timeouts

* Always set timeouts:

  ```python
  requests.get("https://httpbin.org/delay/5", timeout=2)
  ```

* Catch exceptions:

  ```python
  try:
      response = requests.get("https://httpbin.org/status/404")
      response.raise_for_status()
  except requests.exceptions.RequestException as e:
      print("Error:", e)
  ```

---

## 6. Security Considerations

* Verify SSL certificates (enabled by default in `requests`).
* Sanitize inputs when building URLs.
* Be cautious with redirects and authentication tokens.

---

## 7. Advanced Features

* **Streaming Downloads:**

  ```python
  with requests.get("https://example.com/largefile", stream=True) as r:
      for chunk in r.iter_content(chunk_size=8192):
          print(len(chunk))
  ```

* **Authentication:**

  ```python
  response = requests.get("https://api.github.com/user", auth=("user", "pass"))
  ```

* **Sessions:**

  ```python
  session = requests.Session()
  session.get("https://httpbin.org/cookies/set/sessioncookie/123")
  r = session.get("https://httpbin.org/cookies")
  print(r.text)
  ```

---

## 8. When to Use What

* **`requests`** → Most common choice for REST APIs.
* **`aiohttp`/`httpx`** → Best for async & high concurrency.
* **`urllib`/`http.client`** → Use when avoiding dependencies.
* **`socket`** → Custom networking protocols, raw TCP/UDP.

---

## Summary

Python provides multiple ways to handle networking:

* From simple HTTP requests (`requests`) to full async (`aiohttp`, `httpx`).
* For custom protocols, use `socket`.
* Always handle errors, set timeouts, and consider security.

This flexibility allows developers to build everything from quick scripts to large-scale distributed systems.
