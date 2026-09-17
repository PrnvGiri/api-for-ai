# ====================================================
# File: 05_gemini_chat.py
# Goal: Interactive chat with Google Gemini in your terminal
# ====================================================

import os
import requests
from dotenv import load_dotenv

# Step 1: Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_actual_gemini_api_key_here":
    print("❌ Please add your GEMINI_API_KEY in .env before running this chat app!")
    exit()

# Step 2: Gemini URL
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

print("=" * 55)
print("🤖 GEMINI TERMINAL CHAT")
print("Ask anything you want! Type 'exit' or 'quit' to stop.")
print("=" * 55)

# Step 3: Run an interactive loop
while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["exit", "quit", "q"]:
        print("Thanks for chatting! Have a great day ahead.")
        break

    # Prepare data for Gemini
    payload = {
        "contents": [
            {"parts": [{"text": user_input}]}
        ]
    }

    print("Gemini is thinking...")
    response = requests.post(url, json=payload)
    data = response.json()

    # Get answer
    answer = data["candidates"][0]["content"]["parts"][0]["text"]
    print(f"\nGemini: {answer.strip()}")
