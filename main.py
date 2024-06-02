import requests
import time


def get_external_ip():
    try:
        start_time = time.time()

        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip_info = response.json()

        end_time = time.time()
        duration = end_time - start_time

        return ip_info["ip"], duration
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("Starting External IP Address checker...")
    while True:
        external_ip, duration = get_external_ip()
        print(f"External IP Address: {external_ip} (Latency: {duration:.2f} seconds)")
        time.sleep(5)
