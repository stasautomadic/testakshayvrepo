import requests
import time

# URL to send the GET request
url = "https://automadic-rss-scraper.up.railway.app/update-data/"

# API key
api_key = "123456"  # Replace with the actual API key

# Parameters to include the API key in the request
params = {
    "api_key": api_key
}

# Number of times to call the API
iterations = 2
interval = 120  # Interval in seconds (2 minutes)

for i in range(iterations):
    try:
        # Sending the GET request with API key as a query parameter
        response = requests.get(url, params=params, timeout=30)  # Adding a timeout for safety

        # Checking if the request was successful
        if response.status_code == 200:
            print(f"Request {i + 1} was successful!")
            print("Response Data:", response.text)
        elif response.status_code == 401:
            print(f"Request {i + 1}: Unauthorized: Invalid API key.")
        else:
            print(f"Request {i + 1} failed with status code: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        # Catching any request-related errors
        print(f"An error occurred during request {i + 1}:", e)

    # Wait for 2 minutes before the next call, except after the last iteration
    if i < iterations - 1:
        print("Waiting for 2 minutes before the next request...")
        time.sleep(interval)

print("All requests completed.")
