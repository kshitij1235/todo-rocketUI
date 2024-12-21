from Rocket import RELEASE
from threading import Lock
from sys import stdout

log_lock = Lock()

def log(message: str) -> None:
    if not RELEASE:
        with log_lock:
            stdout.write(f"{message}\n")
