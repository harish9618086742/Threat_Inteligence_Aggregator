import time

def run_forever(task, interval=300):
    while True:
        task()
        time.sleep(interval)
