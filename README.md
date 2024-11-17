# Keylogger
Keylogger Script
This is a basic keylogger written in Python that captures and logs keystrokes to a text file. IMPORTANT: This script is for educational purposes only. Always use it ethically and with explicit permission from the device owner.
Prerequisites:
Before running the keylogger, ensure you have Python installed on your system. You will also need to install the pynput library.
How to Use
Download or clone this repository to your local machine.
Locate the script file and open it in your favorite IDE or text editor.
Edit the file path if needed. By default, keystrokes are saved to keystrokes.txt in the current directory.
Run the script:
python keylogger.py
Script Explanation:
The script uses the pynput library to listen for keyboard events.
Keystrokes are logged in the keystrokes.txt file. Special keys like space, enter, and backspace are handled separately to maintain readability.
Handling Special Keys
Space: Logged as a space character.
Enter: Logged as a new line.
Backspace: Logged as [BACKSPACE].
Other special keys are logged in square brackets (e.g., [shift], [ctrl]).
Disclaimer:
Warning: This keylogger is provided for educational purposes only. The use of keylogging software without proper authorization is illegal and a violation of privacy. Ensure you have explicit permission from the device owner before running this software. Misuse of this script could result in legal consequences.
