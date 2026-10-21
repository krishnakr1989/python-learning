import requests

try:
    response = requests.get(
        "https://api.github.com",
        timeout=5
    )
    print("status_code", response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("Success!")
    else:
        print("status_code", response.status_code)

except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
except requests.exceptions.Timeout:
    print("Request timedout")
except Exception as e:
    print(f"Error: {e}")