from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os
import sys
import time

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, process_ref):
        self.process_ref = process_ref

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Detected change in {event.src_path}. Restarting app...")
            self.process_ref.terminate()
            self.process_ref = subprocess.Popen([sys.executable, "main.py"])

def hot_reload_app():
    app_process = subprocess.Popen([sys.executable, "main.py"])

    event_handler = ReloadHandler(app_process)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        app_process.terminate()
    observer.join()
