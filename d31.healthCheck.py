import argparse
import sys
import time

import requests


def check_health(url, timeout):
    try:
        start_time = time.time()

        response = requests.get(url, timeout=timeout)

        response_time = (time.time() - start_time) * 1000

        print(f"URL          : {url}")
        print(f"HTTP Status  : {response.status_code}")
        print(f"Response Time: {response_time:.2f} ms")

        if response.status_code != 200:
            print("Health Check : FAILED")
            return False

        try:
            data = response.json()

            if data.get("status") == "UP":
                print("Health Check : PASSED")
                return True

            print("Health Check : FAILED")
            print(f"Response     : {data}")
            return False

        except ValueError:
            print("Health Check : FAILED")
            print("Response is not valid JSON")
            return False

    except requests.exceptions.Timeout:
        print("Health Check : FAILED")
        print(f"Request timed out after {timeout} seconds")
        return False

    except requests.exceptions.ConnectionError:
        print("Health Check : FAILED")
        print("Unable to connect to application")
        return False

    except requests.exceptions.RequestException as e:
        print("Health Check : FAILED")
        print(f"Request error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Check application health endpoint"
    )

    parser.add_argument(
        "-u",
        "--url",
        required=True,
        help="Application health endpoint URL"
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=5,
        help="Request timeout in seconds (default: 5)"
    )

    args = parser.parse_args()

    healthy = check_health(args.url, args.timeout)

    # Important for CI/CD and monitoring
    sys.exit(0 if healthy else 1)


if __name__ == "__main__":
    main()


# python .\d31.healthCheck.py --url http://localhost:8080/health
# python .\d31.healthCheck.py --url http://localhost:8080/health -t 10