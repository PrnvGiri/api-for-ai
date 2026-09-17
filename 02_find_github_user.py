# ====================================================
# File: 02_find_github_user.py
# Goal: Ask the user for any username and fetch their details
# ====================================================

import requests

# Step 1: Take username from the user
username = input("Enter any GitHub username: ").strip()

# Step 2: Build the dynamic URL using f-string
url = f"https://api.github.com/users/{username}"

# Step 3: Send the request to GitHub
print(f"Fetching details for '{username}'...")
response = requests.get(url)

# Step 4: Check if user exists (200) or does not exist (404)
if response.status_code == 200:
    data = response.json()
    print("\n✅ User Found!")
    print("Username :", data["login"])
    print("Name     :", data["name"])
    print("Bio      :", data["bio"])
    print("Company  :", data["company"])
    print("Location :", data["location"])
    print("Repos    :", data["public_repos"])
    print("Followers:", data["followers"])
elif response.status_code == 404:
    print(f"\n❌ User '{username}' was not found. Please double check the spelling!")
else:
    print(f"\n⚠️ Something else went wrong. Status code: {response.status_code}")
