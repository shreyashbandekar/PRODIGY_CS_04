# PRODIGY_CS_04
# Keylogger Script
This Python script uses the pynput library to log keystrokes into a text file. It captures key presses and saves them to a file called key_log.txt. This can be useful for debugging or educational purposes to understand how keystrokes can be captured programmatically.
## Requirements
- **Python 3.x**
- **pynput library**
## Installation
To get started, you'll need to install the pynput library if you haven't already. You can install it using pip:
```bash
pip install pynput
```
## Script Overview 
### Functionality
- **Key Logging:** The script logs every key press into a file called key_log.txt.
- **File Handling:** The script handles file operations safely, appending each keystroke to the log file.
- **Special Keys:** It logs special keys like space, enter, and others in a readable format.
- **Exit:** The script stops logging when the Esc key is pressed.
## How It Works
1. **Imports:** The script imports the necessary components from the pynput library.
2. **File Path:** The log_file variable defines the path of the file where keystrokes will be saved.
3. **Key Logging Functions:**
   - **write_to_file(key):** Writes the pressed key to the log file.
   - **on_press(key):** Calls write_to_file when a key is pressed.
   - **on_release(key):** Stops the listener when the Esc key is pressed.
4. **Listener Setup:** The script sets up a pynput listener to monitor key events.
## Usage
1. **Run the Script:** Execute the script using Python. Ensure that you have the necessary permissions to write to the file.
    ```bash
   python keylogger.py
2. **Monitor the Log:** Open `key_log.txt` to view the captured keystrokes.
3. **Stop Logging:** `Press the Esc key` to stop the script.
   
## Security Warning
Please use this script responsibly. Unauthorized keylogging can be illegal and unethical. Ensure you have permission before capturing keystrokes on any system.
