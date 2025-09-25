# Coding Challenge — Python Standard Library: Networking & Internet Data Handling

This set of challenges will exercise your ability to work with sockets, URLs, HTTP requests, and common internet protocols using Python’s standard library.

---

## Challenge 1: Simple TCP Echo Server and Client

1. Write a **TCP server** that:
   - Listens on `localhost:9000`.
   - Accepts multiple client connections (use threads or `asyncio`).
   - Echoes back every message received.

2. Write a **TCP client** that:
   - Connects to the server.
   - Sends three messages (`"Hello"`, `"Advanced"`, `"Python"`).
   - Prints the responses.

*Bonus*: Extend the server to log the number of messages per client.

---

## Challenge 2: URL Parsing and Building

- Given the URL:

https://example.org/products/view?id=123&sort=asc

- Write a function that:
- Extracts the `id` and `sort` parameters.
- Modifies the URL to add a new parameter: `user=42`.
- Returns the modified URL.

---

## Challenge 3: Fetch a Web Page

- Use `urllib.request` to:
- Fetch `https://httpbin.org/get`.
- Parse the response as JSON (hint: use `json.loads`).
- Print out the `"origin"` (IP address) and `"headers"` fields.

*Bonus*: Handle exceptions and print a friendly error if the network is unavailable.

---

## Challenge 4: Send an Email (Simulation)

- Build an email message with:
- Subject: `"Advanced Python Test"`.
- From: `"me@example.com"`.
- To: `"you@example.com"`.
- Body: `"This is a test email sent from Python."`

- Instead of sending it, write the **full MIME message** to a file named `test_email.eml`.

*Bonus*: Parse the same `.eml` file back into a `Message` object and print the subject and body.

---

## Challenge 5: Simple Asyncio Chat Server

- Use `asyncio` to implement a simple **chat server**:
- Multiple clients can connect.
- When one client sends a message, broadcast it to all others.
- Ensure proper closing of connections.

*Bonus*: Add a command `/quit` that disconnects the client cleanly.

---

## Challenge 6: FTP Directory Listing (Optional)

- Use `ftplib` to:
- Connect to an **anonymous FTP server** (try `ftp.debian.org`).
- List the files in the `/debian` directory.
- Print the first 10 file/directory names.

---

## Deliverables

- `echo_server.py` — TCP server
- `echo_client.py` — TCP client
- `url_tools.py` — URL parsing utility
- `fetch_page.py` — fetch and parse JSON response
- `email_builder.py` — build/save MIME email
- `chat_server.py` — asyncio chat server
- `ftp_list.py` — FTP listing script (optional)