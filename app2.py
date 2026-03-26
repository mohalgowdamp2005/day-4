import os
import sys
import socket
from datetime import datetime

# 1. Display current date & time
print("Current Date & Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 2. Show system hostname
print("Hostname:", socket.gethostname())

# 3. Print Python version
print("Python Version:", sys.version)

# 4. Show list of files in current directory
print("\nFiles in Current Directory:")
for item in os.listdir("."):
    print(f"  - {item}")