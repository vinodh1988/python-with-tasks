import schedule
import time

def job():
    print("Running scheduled job...")
    print("Current time:", time.strftime("%Y-%m-%d %H:%M:%S"))

# Schedule the job every 10 minutes
schedule.every(0.5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
   