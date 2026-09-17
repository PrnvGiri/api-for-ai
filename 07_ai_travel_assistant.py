# ====================================================
# File: 07_ai_travel_assistant.py
# Goal: Capstone Mini Project — Live Weather + Gemini AI
# ====================================================

import os
import requests
from dotenv import load_dotenv

# Step 0: Load secret Gemini API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 60)
print("AI TRAVEL & WEATHER ASSISTANT")
print("=" * 60)

# ----------------------------------------------------
# Step 1: Ask user for city name
# ----------------------------------------------------
city = input("Enter any city name (e.g. Mumbai, Delhi, London, Tokyo): ").strip()

if not city:
    print("City name cannot be empty. Please run again!")
    exit()

# ----------------------------------------------------
# Step 2: Fetch live weather from free Weather API (wttr.in)
# ----------------------------------------------------
print(f"\n[1/3] Getting live weather for {city}...")
weather_url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(weather_url, timeout=10)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print(f"[Error] Could not fetch weather: {e}")
    exit()

# ----------------------------------------------------
# Step 3: Extract temperature & condition from JSON
# ----------------------------------------------------
temperature = data["current_condition"][0]["temp_C"]
condition = data["current_condition"][0]["weatherDesc"][0]["value"]

print(f"[2/3] Current Weather: {temperature}°C with {condition}")

# ----------------------------------------------------
# Step 4: Craft our custom prompt for Gemini
# ----------------------------------------------------
prompt = f"""
The current weather in {city} is {temperature} degrees Celsius and {condition}.
You are a helpful travel assistant. Please tell me:
1. What kind of clothes should I wear today?
2. What items should I carry in my bag (e.g., umbrella, water bottle, jacket)?
3. One quick advice for going outside in this weather.

Keep the advice short, clear, and in simple bullet points.
"""

# ----------------------------------------------------
# Step 5: Send prompt to Google Gemini API
# ----------------------------------------------------
print("[3/3] Asking Google Gemini for personalized travel tips...")

if not api_key or api_key == "your_actual_gemini_api_key_here":
    print("\n[Warning] Note: GEMINI_API_KEY is not configured in your .env file yet.")
    print(f"Quick advice: Since it is {temperature}°C with {condition} in {city}, dress comfortably and plan accordingly!")
    print("Tip: Add your Gemini key to .env to see live AI responses!")
else:
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        ai_response = requests.post(gemini_url, json=payload, timeout=15)
        ai_response.raise_for_status()
        ai_data = ai_response.json()

        # ----------------------------------------------------
        # Step 6: Display the AI advice
        # ----------------------------------------------------
        advice = ai_data["candidates"][0]["content"]["parts"][0]["text"]
        print("\n" + "=" * 60)
        print(f"AI TRAVEL ADVICE FOR {city.upper()}:")
        print("=" * 60)
        print(advice.strip())
        print("=" * 60)

    except Exception as e:
        print(f"[Error] Error talking to Gemini: {e}")
