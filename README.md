# API for AI: The Complete Beginner's Guide 

Welcome! If you have ever wondered how Python programs talk to websites, fetch live data from the internet, and connect with **Google Gemini AI** models to build smart apps — you are in the exact right place.

There is no heavy networking theory or confusing jargon here. Everything is broken down into simple baby steps with clean, standalone Python scripts you can run right away.

---

## Table of Contents
1. [Quick Setup in 2 Minutes](#quick-setup-in-2-minutes)
2. [What is an API? (The Restaurant Story)](#what-is-an-api)
3. [The 4 Words You Must Know](#the-4-words-you-must-know)
4. [GET vs POST & Status Codes](#get-vs-post--status-codes)
5. [Understanding JSON Data](#understanding-json-data)
6. [Why We Need API Keys & The `.env` File](#why-we-need-api-keys--the-env-file)
7. [Calling Google Gemini API](#calling-google-gemini-api)
8. [Error Handling (Don't Let Your Code Crash!)](#error-handling)
9. [Capstone Project: AI Weather & Travel Assistant](#capstone-project-ai-weather--travel-assistant)
10. [File Guide & How to Run](#file-guide--how-to-run)

---

## Quick Setup in 2 Minutes

### 1. Install required packages
Open your terminal inside this folder and run:
```bash
pip install -r requirements.txt
```

### 2. Set up your Gemini API Key (It's free!)
1. Go to **[Google AI Studio](https://aistudio.google.com)**.
2. Sign in with your Google account and click **"Get API key"**.
3. Create a file named `.env` in this folder (or copy from `.env.example`):
 ```bash
 cp .env.example .env
 ```
4. Paste your key inside `.env`:
 ```env
 GEMINI_API_KEY=your_actual_key_here
 ```

---

## What is an API?

**API** stands for **Application Programming Interface**.

Think of it like going to a restaurant:

```text
You (Your Python Code)
 |
 | 1. Order (Request)
 v
Waiter (The API)
 |
 | 2. Passes order to chef
 v
Kitchen (The Server / Database)
 |
 | 3. Prepares food
 v
Waiter (The API)
 |
 | 4. Brings food to table (Response)
 v
You (Your Python Code)
```

1. **You** cannot walk directly into the restaurant kitchen to cook food.
2. You look at the menu, decide what you want, and tell the **Waiter**.
3. The **Waiter** takes your order to the **Kitchen**.
4. The kitchen prepares your dish.
5. The **Waiter** brings your food back to your table.

In software, **the Waiter is the API**! It takes your request to another computer across the internet and brings back the reply.

### Real-life Examples:
* **Weather on your phone:** Your phone app doesn't have weather satellites. It calls a Weather API: *"What is the temperature in Bengaluru today?"*
* **Swiggy / Zomato / Uber:** They don't build satellite map systems from scratch. They call the **Google Maps API**.
* **AI Apps:** Your code calls the **Google Gemini API** to ask questions and get smart responses.

---

## The 4 Words You Must Know

Whenever two applications talk to each other:

1. **Client** = The person or program asking for something (Your Python script).
2. **Server** = The computer on the internet that has the data.
3. **Request** = The message you send across the internet.
4. **Response** = What comes back from the server.

```text
Client (Python) --- 1. Request ---> Server (API)
Client (Python) <-- 2. Response --- Server (API)
```

---

## GET vs POST & Status Codes

### The Two Most Important Actions:

| Action | What it means | Example |
| :--- | :--- | :--- |
| **`GET`** | *"Please give me data"* | Fetching current weather or user profile |
| **`POST`** | *"Here is some data, please process it"* | Submitting a prompt to an AI model |

### Status Codes (What the Server is Telling You):
Every time a server replies, it sends a 3-digit code:

* **`200` = OK (Success!)** Everything went smoothly.
* **`400` = Bad Request.** You sent invalid parameters or wrong syntax.
* **`401` = Unauthorized.** Missing or incorrect API key.
* **`404` = Not Found.** The page or username does not exist (check for typos!).
* **`500` = Server Error.** Something crashed on their end (not your fault).

---

## Understanding JSON Data

When an API responds, the data comes in a format called **JSON** (JavaScript Object Notation). 
In Python, JSON is simply a **Dictionary**:

```python
# This is JSON in Python:
student = {
 "name": "Aarav",
 "age": 21,
 "city": "Mumbai",
 "skills": ["Python", "Machine Learning"]
}

# How to read values:
print(student["name"]) # Output: Aarav
print(student["skills"][0]) # Output: Python
```

---

## Why We Need API Keys & The `.env` File

### What is an API Key?
An API Key is like a unique digital password. It tells Google or GitHub:
> *"Hey, this request is from Rahul. Please let him use the AI model."*

### [Error] Never Hardcode Keys in Python:
```python
# NEVER DO THIS!
api_key = "AIzaSyD-secret-key-12345"
```
If you push this code to GitHub, automated bots can steal your key within seconds!

### The Safe Way: Use `.env` and `.gitignore`
1. Keep your real key in a local file named `.env`:
 ```env
 GEMINI_API_KEY=AIzaSy...
 ```
2. Put `.env` inside `.gitignore` so git never uploads it.
3. Read it inside Python using `python-dotenv`:
 ```python
 import os
 from dotenv import load_dotenv

 load_dotenv()
 api_key = os.getenv("GEMINI_API_KEY")
 ```

---

## Calling Google Gemini API

Normally you go to the Gemini website in your browser and type a prompt. 
With the **Gemini API**, your Python script sends the prompt and gets the answer directly:

```text
Your Python Script ---> Google Gemini API ---> Gemini 1.5 Flash ---> Your Python Script
```

### The 5 Simple Lines:
```python
import requests

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
payload = {"contents": [{"parts": [{"text": "Explain Python in 1 sentence."}]}]}

response = requests.post(url, json=payload)
data = response.json()
print(data["candidates"][0]["content"]["parts"][0]["text"])
```

---

## Error Handling

What happens if your WiFi drops or someone enters an invalid URL? 
Normally, Python throws an ugly error and crashes completely.

With `try` and `except`, your app handles errors gracefully:

```python
import requests

try:
 response = requests.get("https://api.github.com/wrong_link", timeout=5)
 response.raise_for_status() # Throws error if 404, 500, etc.
 print("Success!")
except Exception as error:
 print("Handled cleanly without crashing! Problem was:", error)
```

---

## Capstone Project: AI Weather & Travel Assistant

AI models like Gemini are brilliant, but **they do not know today's live weather** because they don't have sensors outside your window.

### The Solution: API Chaining
We combine two APIs together in a single pipeline:

```text
[ Step 1: User enters city ] --> "Delhi"
 |
 v
[ Step 2: Weather API (wttr.in) ] --> Live data: 32°C, Sunny
 |
 v
[ Step 3: Python builds prompt ] --> "The weather in Delhi is 32°C and Sunny. What should I pack?"
 |
 v
[ Step 4: Google Gemini API ] --> Recommends cotton clothes, sunglasses & water bottle!
 |
 v
[ Step 5: Clean Output to User ]
```

---

## File Guide & How to Run

Every script is completely standalone and ready to execute:

| File | What it does | How to run |
| :--- | :--- | :--- |
| **`01_first_api.py`** | Calls GitHub's public API and prints profile data | `python 01_first_api.py` |
| **`02_find_github_user.py`** | Takes any username input and fetches their info | `python 02_find_github_user.py` |
| **`03_test_env.py`** | Checks if your `.env` and `GEMINI_API_KEY` are working | `python 03_test_env.py` |
| **`04_gemini_api.py`** | Sends a question to Google Gemini and prints its reply | `python 04_gemini_api.py` |
| **`05_gemini_chat.py`** | Interactive terminal chatbot with Gemini | `python 05_gemini_chat.py` |
| **`06_error_handling.py`** | Shows how `try-except` prevents code crashes | `python 06_error_handling.py` |
| **`07_ai_travel_assistant.py`** | Capstone: Live weather + Gemini travel advisor | `python 07_ai_travel_assistant.py` |

---

## Quick Tips
* If you see **Status Code 200**, that means everything worked!
* If you see **404**, check for typos in your URL.
* If you see **401**, check if your API key in `.env` is correct.
* Always check what your JSON looks like before trying to extract nested keys.

Happy coding! 
