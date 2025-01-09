import requests

# URL to send the GET request
url = "https://web-production-d0e1f.up.railway.app/update-data/"

try:
    # Sending the GET request
    response = requests.get(url, timeout=30)  # Adding a timeout for safety
    
    # Checking if the request was successful
    if response.status_code == 200:
        print("Request was successful!")
        print("Response Data:", response.text)
    else:
        print(f"Failed with status code: {response.status_code}")
        print("Response:", response.text)
except requests.exceptions.RequestException as e:
    # Catching any request-related errors
    print("An error occurred:", e)
