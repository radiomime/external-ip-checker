import requests
import time


def get_external_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip_info = response.json()
        return ip_info["ip"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


if __name__ == "__main__":
    while True:
        external_ip = get_external_ip()
        print(f"External IP Address: {external_ip}")
        time.sleep(5)
