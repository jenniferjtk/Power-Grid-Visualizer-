import schedule
import time
import subprocess

def fetch_api_every_10():
    subprocess.run(["python3", "fetchAPI.py"])

# Schedule to run every 10 minutes
schedule.every(10).minutes.do(fetch_api_every_10)

while True:
    schedule.run_pending()
    time.sleep(20)