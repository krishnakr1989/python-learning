import requests

response = requests.post(
    url,
    json={
        "application": "payment",
        "version": "2.4.1"
    },
    timeout=10
)