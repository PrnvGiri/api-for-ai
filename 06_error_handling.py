# ====================================================
# File: 06_error_handling.py
# Goal: Stop your code from crashing when an API fails
# ====================================================

import requests

# What is try-except?
# It means: "Try to run this code block. If anything goes wrong,
# don't crash the program! Run the except block instead."

# ----------------------------------------------------
# Example 1: What happens with a 404 (Page Not Found)?
# ----------------------------------------------------
bad_url = "https://api.github.com/non_existent_page_12345"

try:
    print("Test 1: Requesting a link that does not exist...")
    response = requests.get(bad_url, timeout=5)
    
    # raise_for_status() checks if the code is 404, 500, etc.
    # If yes, it jumps straight to the except block below!
    response.raise_for_status()
    print("Success!")
except Exception as err:
    print("Handled cleanly without crashing! Error was:", err)

# ----------------------------------------------------
# Example 2: What happens if you lose internet or domain is fake?
# ----------------------------------------------------
fake_domain = "https://this-is-not-a-real-website-abc-xyz-999.com"

try:
    print("\nTest 2: Requesting a fake website domain...")
    response = requests.get(fake_domain, timeout=3)
    response.raise_for_status()
except Exception as err:
    print("Caught connection problem! Program continues running smoothly.")

print("\n🎉 Both tests completed safely! No raw Python traceback crashes.")
