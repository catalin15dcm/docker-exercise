import time
import urllib.request
import datetime

SERVER_URL = "http://server:9000/api/ping"

def ping():
    try:
        with urllib.request.urlopen(SERVER_URL) as response:
            body = response.read().decode()
            timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
            print(f"[{timestamp}] Received: {body}", flush=True)
    except Exception as e:
        print(f"Error: {e}")

def run():
    while True:
        ping()
        time.sleep(5)

if __name__ == "__main__":
    run()
