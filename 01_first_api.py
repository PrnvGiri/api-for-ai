# ====================================================
# File: 01_first_api.py
# Goal: Make your very first API call using Python
# ====================================================

# Step 1: Bring in the requests library
import requests

# Step 2: Set the website link (API endpoint)
# We are using GitHub's free public API here
url = "https://api.github.com/users/octocat"

# Step 3: Send a GET request (asking GitHub for data)
print("Connecting to GitHub API...")
response = requests.get(url)

# Step 4: Check if everything went well (200 means success!)
print("Status code from server:", response.status_code)

# Step 5: Convert the reply into a Python dictionary (JSON)
data = response.json()

# Step 6: Print only the details we want to see
print("\n--- GitHub Profile Details ---")
print("Username :", data["login"])
print("Full Name:", data["name"])
print("Bio      :", data["bio"])
print("Repos    :", data["public_repos"])
print("Followers:", data["followers"])
print("------------------------------")
