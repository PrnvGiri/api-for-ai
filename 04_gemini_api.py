# ====================================================
# File: 04_gemini_api.py
# Goal: Send a prompt to Google Gemini and print its reply
# ====================================================

import os
import requests
from dotenv import load_dotenv

# Step 1: Load secret key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_actual_gemini_api_key_here":
    print("[Error] Please add your GEMINI_API_KEY inside the .env file first!")
    exit()

# Step 2: Google Gemini endpoint URL with your API key
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

# Step 3: What do you want to ask Gemini?
prompt = "Explain Machine Learning in 2 simple sentences for a school student."

# Gemini expects the prompt inside this exact structure
payload = {
    "contents": [
        {"parts": [{"text": prompt}]}
    ]
}

# Step 4: Send the request to Google (POST request because we are sending data)
print("Sending question to Google Gemini...")
response = requests.post(url, json=payload)
data = response.json()

# Step 5: Read the generated text from Gemini's reply
answer = data["candidates"][0]["content"]["parts"][0]["text"]

# Step 6: Print the answer nicely
print("\n--- Google Gemini Reply ---")
print(answer)
print("---------------------------")
