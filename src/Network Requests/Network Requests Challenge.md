# Network Requests in Python: Coding Challenges

These challenges will help you practice working with HTTP requests, APIs, and networking libraries in Python.

---

## Challenge 1: Basic GET Request

**Objective:**
Write a script using `requests` to fetch the contents of `https://httpbin.org/get` and print the JSON response.

---

## Challenge 2: Sending Query Parameters

**Objective:**
Send a GET request to `https://httpbin.org/get` with query parameters (e.g., `name=Alice`, `lang=Python`) and print the parsed JSON response.

---

## Challenge 3: POST Request with JSON

**Objective:**
Send a POST request with JSON payload (e.g., `{"task": "learn", "done": false}`) to `https://httpbin.org/post` and display the response.

---

## Challenge 4: Handling Timeouts

**Objective:**
Make a request to `https://httpbin.org/delay/3` with a timeout of 2 seconds and handle the timeout exception gracefully.

---

## Challenge 5: Custom Headers

**Objective:**
Send a request with a custom header (e.g., `X-Course: AdvancedPython`) and print the headers echoed back by `https://httpbin.org/headers`.

---

## Challenge 6: File Download

**Objective:**
Download an image file from `https://httpbin.org/image/png` and save it locally as `test.png`.

---

## Challenge 7: Session Reuse

**Objective:**
Use `requests.Session` to make multiple requests to `https://httpbin.org/cookies` while maintaining cookies across requests.

---

## Challenge 8: Async Requests (Advanced)

**Objective:**
Using `httpx` or `aiohttp`, perform 10 concurrent GET requests to `https://httpbin.org/get` and collect all responses.

---

## Challenge 9: Error Handling

**Objective:**
Send a request to an invalid URL (e.g., `https://httpbin.org/status/404`) and handle HTTP errors using `raise_for_status()`.

---

## Challenge 10: Real-World Mini Project

**Objective:**
Build a small script that:

* Fetches the current weather from a free API (like OpenWeatherMap or WeatherAPI, requires free API key)
* Parses the JSON response
* Displays temperature, condition, and location

