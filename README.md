# Browser History Manager — DSA Mini Project (Stack Data Structure)

A modern, functional web application that implements and visualizes the **Stack Data Structure (LIFO: Last-In, First-Out)** used in web browser navigation.

---

## 📌 Project Overview
Web browsers use two stacks to manage tab navigation history:
1. **Back Stack (`back_stack`)**: Stores previously visited URLs. When you click **Go Back**, the current page is pushed to the forward stack, and the top of the back stack is popped to become the current page.
2. **Forward Stack (`forward_stack`)**: Stores pages available for forward navigation. When you click **Go Forward**, the current page is pushed to the back stack, and the top of the forward stack is popped to become the current page.
3. **Branching Navigation (Visit Website)**: Whenever a user visits a new URL, the current page is pushed onto the `back_stack`, and the `forward_stack` is **cleared** (`clear()`).

---

## 🛠️ Technology Stack
- **Backend**: Python 3
- **Web Framework & API**: Flask
- **Frontend**: HTML5, Vanilla CSS3 (Custom Dark Theme & Stack Visualizer), JavaScript (Fetch API)
- **Data Exchange**: JSON

---

## 📁 Project Structure
```text
browser-history-manager/
├── app.py                 # Flask server and REST API routes
├── browser_history.py     # Core Python DSA Stack logic (BrowserHistory class)
├── requirements.txt       # Project dependencies (Flask)
├── test_app.py            # Automated Unit and REST API test suite
├── templates/
│   └── index.html         # Web frontend structure
└── static/
    ├── style.css          # Modern dark theme & stack visualization styling
    └── script.js          # Client-side API integration (Fetch API)
```

---

## 🚀 How to Run the Project in VS Code

### Step 1: Open Terminal in VS Code
Open VS Code, press `Ctrl + ~` (or `Terminal` > `New Terminal`), and navigate to the project directory:
```bash
cd "browser-history-manager"
```

### Step 2: Install Dependencies
Install Flask using pip:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Flask Web Application
Start the Flask application:
```bash
python app.py
```
You will see output similar to:
```text
==================================================
  Browser History Manager — Flask Web Server
  Open in browser: http://127.0.0.1:5000
==================================================
 * Running on http://127.0.0.1:5000
```

### Step 4: Open in Your Browser
Open your web browser (Chrome, Edge, Firefox, Brave) and navigate to:
```
http://127.0.0.1:5000
```

---

## 🧪 Testing the Project

### 1. Automated Test Suite
Run the built-in unit tests for both DSA logic and Flask API endpoints:
```bash
python test_app.py
```

### 2. Standalone Terminal Mode (Original CLI)
If your professor asks to see the original terminal program:
```bash
python browser_history.py
```

---

## 📡 REST API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/state` | Returns the current page, back stack, and forward stack |
| `POST` | `/api/visit` | Visits a new website URL (`{"url": "https://..."}`) |
| `POST` | `/api/back` | Navigates back (pops from `back_stack`, pushes to `forward_stack`) |
| `POST` | `/api/forward` | Navigates forward (pops from `forward_stack`, pushes to `back_stack`) |
| `GET` | `/api/history` | Returns complete browsing history (Previous, Current, Forward) |
| `DELETE` | `/api/history` | Clears all browsing history and resets stacks |

### Example API Requests (cURL / PowerShell)

**1. Visit a Website:**
```bash
curl -X POST http://127.0.0.1:5000/api/visit -H "Content-Type: application/json" -d "{\"url\": \"https://www.google.com\"}"
```

**2. Get Current State:**
```bash
curl http://127.0.0.1:5000/api/state
```

**3. Go Back:**
```bash
curl -X POST http://127.0.0.1:5000/api/back
```

**4. Go Forward:**
```bash
curl -X POST http://127.0.0.1:5000/api/forward
```

**5. Clear History:**
```bash
curl -X DELETE http://127.0.0.1:5000/api/history
```

---

## 🎓 College Viva Questions & Answers

**Q1: Which Data Structure is used in Browser History Navigation?**
> **Answer**: The **Stack** data structure (specifically two stacks: `back_stack` and `forward_stack`). A stack operates on the **LIFO (Last-In, First-Out)** principle.

**Q2: What is the Time and Space Complexity?**
> **Answer**:
> - **Time Complexity**: $O(1)$ constant time for all navigation operations (`visit_website`, `go_back`, `go_forward`) because push (`append`) and pop (`pop`) operations on Python lists take $O(1)$ amortized time.
> - **Space Complexity**: $O(N)$ where $N$ is the total number of visited URLs stored across the two stacks.

**Q3: Why is the forward stack cleared when a new website is visited?**
> **Answer**: In real web browsers, if you navigate back a few pages and then type a completely new URL, you create a new browsing branch. Any forward navigation path from your previous session becomes invalid and discarded.

**Q4: How does the website communicate with Python?**
> **Answer**: The frontend uses JavaScript `fetch()` to call the Flask REST API endpoints over HTTP, sending and receiving data serialized in JSON format. The Flask backend maintains separate `BrowserHistory` instances per session so different tabs or users do not interfere with each other.
