# ====================================================
# File: 03_test_env.py
# Goal: Make sure our secret API key is loading properly
# ====================================================

import os
from dotenv import load_dotenv

# Step 1: Read the hidden .env file
load_dotenv()

# Step 2: Grab the secret key
api_key = os.getenv("GEMINI_API_KEY")

# Step 3: Check if it's there
print("=" * 50)
print("CHECKING YOUR .env SETUP")
print("=" * 50)

if not api_key or api_key == "your_actual_gemini_api_key_here":
 print("[Error] No API key found yet!")
 print("\nQuick fix:")
 print("1. Create a file named '.env' in this same folder.")
 print("2. Add this line inside it:")
 print(" GEMINI_API_KEY=your_real_key_from_google_ai_studio")
 print("3. Run this script again!")
else:
 # Just show first few and last few characters for safety
 masked_key = api_key[:6] + "..." + api_key[-4:]
 print("[OK] Success! Gemini API key is loaded properly.")
 print(f"Key preview: {masked_key}")

print("=" * 50)
