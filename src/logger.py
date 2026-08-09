"""Simple logging helper for the machine learning project.

Think of this file as a diary for the program.
Every time the project runs, it creates a new log file inside the logs folder.
The log file saves messages like 'started', 'dataset loaded', or 'training finished',
so we can read what happened step by step later.

This is useful because if the program has a problem, we can open the log file
and understand what happened before the error.
"""

import logging
import os
from datetime import datetime

# Create a new log file name using the current date and time.
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
# Put the log file inside the logs folder in the project root.
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

LOG_FILE_PATH = os.path.join(os.path.dirname(log_path), LOG_FILE)

# Configure Python logging so messages are written into the log file.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started.")