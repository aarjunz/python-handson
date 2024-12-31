import logging
from logging.handlers import RotatingFileHandler
import os

# Define log directory and file
LOG_DIR = "logs"
LOG_FILE = "app.log"

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to the log file
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Default log level (can be overridden)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log format
    handlers=[
        logging.StreamHandler(),  # Log to console
        RotatingFileHandler(LOG_PATH, maxBytes=5 * 1024 * 1024, backupCount=5),  # Log to file with rotation
    ],
)

# Get a logger instance
def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger instance for the given name.
    
    :param name: Name of the logger, typically `__name__`.
    :return: Configured logger instance.
    """
    return logging.getLogger(name)
