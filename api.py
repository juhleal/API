import requests

# Make GET request to an API
url = 'https://api.example.com/data'
response = requests.get(url)

# Process API response
data = response.json()

# Example: Print first 5 items in the response
for item in data[:5]:
    print(item)
