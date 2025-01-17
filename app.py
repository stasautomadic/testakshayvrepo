import requests

# URL to send the GET request
# url = "https://web-production-d0e1f.up.railway.app/update-data/"
url = "https://automadic-rss-scraper.up.railway.app/update-data/"

api_key = "123456"  # Replace with the actual API key

# Parameters to include the API key in the request
params = {
    "api_key": api_key
}

try:
    # Sending the GET request with API key as a query parameter
    response = requests.get(url, params=params, timeout=30)  # Adding a timeout for safety
    
    # Checking if the request was successful
    if response.status_code == 200:
        print("Request was successful!")
        print("Response Data:", response.text)
    elif response.status_code == 401:
        print("Unauthorized: Invalid API key.")
    else:
        print(f"Failed with status code: {response.status_code}")
        print("Response:", response.text)
except requests.exceptions.RequestException as e:
    # Catching any request-related errors
    print("An error occurred:", e)
