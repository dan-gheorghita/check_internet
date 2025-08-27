import sys
import socket
import time
from datetime import datetime

def check_internet():
    try:
        # Try to connect to a reliable host (Google's DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

attempt = 1
# Wait for internet connection
while not check_internet():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Attempt {attempt}: No internet connection. Retrying in 60 seconds...")
    time.sleep(60)  # Wait for 60 seconds before retrying
    attempt += 1

# Once internet is available, run the main script
sys.exit(0)
