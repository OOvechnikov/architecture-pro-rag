import schedule
import time
import subprocess
import os

from pathlib import Path

def run_update_index():
    script_path = str(Path("./update_index.py"))
    log_path = str(Path("./logs/index_update.log"))

    with open(log_path, "a") as log_file:
        subprocess.run(
            ["python", script_path],
            stdout=log_file,
            stderr=log_file,
            cwd=str(Path.cwd())
        )

schedule.every(1).minutes.do(run_update_index)

print("Планировщик запущен. Нажмите Ctrl+C для остановки.")

while True:
    schedule.run_pending()
    time.sleep(1)