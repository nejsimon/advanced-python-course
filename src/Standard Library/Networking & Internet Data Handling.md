# Python Standard Library — Networking & Internet Data Handling

Python’s standard library includes powerful tools for working with networking protocols, data formats, and internet services. This cluster covers essential modules for sockets, HTTP requests, parsing URLs, and handling common internet data representations.

---

## 1. Low-Level Networking: `socket`

- Provides access to BSD-style socket interfaces.
- Supports TCP, UDP, raw sockets, IPv4, IPv6.
- Useful for creating servers and clients at the protocol level.

**Example: Simple TCP Echo Server**
```python
import socket

HOST, PORT = "127.0.0.1", 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while data := conn.recv(1024):
            conn.sendall(data)
2. URL Parsing: urllib.parse
Splits URLs into components (scheme, netloc, path, query, etc.).

Can also construct and encode query parameters.

Example:

```python
from urllib.parse import urlparse, urlencode

url = "https://example.com/search?q=python&lang=en"
parsed = urlparse(url)
print(parsed.query)

params = {"q": "advanced python", "lang": "en"}
print(urlencode(params))
```

3. HTTP Clients: http.client and urllib.request
http.client provides low-level access to HTTP requests.

urllib.request is a higher-level interface for fetching URLs.

Example:

```python
from urllib.request import urlopen

with urlopen("https://httpbin.org/get") as response:
    print(response.read().decode())
```

4. Email Handling: smtplib, imaplib, email
smtplib: send emails using SMTP.

imaplib: access emails from an IMAP server.

email: build and parse MIME email messages.

Example: Sending a Simple Email

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello, World!")
msg["Subject"] = "Test"
msg["From"] = "me@example.com"
msg["To"] = "you@example.com"

with smtplib.SMTP("localhost") as server:
    server.send_message(msg)
```

5. Internet Data Formats: html, xml, json, mailbox
html.parser: simple HTML parsing.

xml.etree.ElementTree: basic XML parsing.

json: parse and serialize JSON data.

mailbox: handle Unix mailbox (mbox) formats.

6. Higher-Level Networking: ftplib, poplib, nntplib
ftplib: connect to FTP servers.

poplib: retrieve mail using POP3.

nntplib: access Usenet newsgroups.

7. asyncio Networking
asyncio integrates networking with coroutines and event loops.

Can build async servers and clients efficiently.

Example: Asyncio Echo Server

```python
import asyncio

async def handle(reader, writer):
    data = await reader.read(100)
    writer.write(data)
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle, "127.0.0.1", 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
```

8. Quirks and Pitfalls
urllib.request is simple but limited compared to requests.

http.client is verbose but useful for debugging.

socket programming requires careful resource cleanup.

Always handle timeouts and exceptions when dealing with real networks.

Summary
This cluster covers everything from raw socket programming to high-level modules for HTTP, email, and internet data. Combined with Python’s async features, these modules let you build networking tools without third-party libraries.