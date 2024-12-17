import time
import pyautogui
import tkinter as tk
import os

# Function to take a screenshot
def screenshot():
    try:
        # Create the directory if it doesn't exist
        save_dir = 'D:/Python/screenshots data/'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Generate a unique name for the screenshot
        name = int(round(time.time() * 1000))
        filepath = f"{save_dir}{name}.png"

        # Take and save the screenshot
        img = pyautogui.screenshot(filepath)
        img.show()  # Display the image
        print(f"Screenshot saved at {filepath}")
    except Exception as e:
        print(f"Error: {e}")

# Set up the tkinter window
root = tk.Tk()
root.title("Screenshot App")
root.geometry("300x100")  # Optional: Set the size of the window

frame = tk.Frame(root)
frame.pack(pady=20)

# Button to take a screenshot
screenshot_button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
screenshot_button.pack(side=tk.LEFT, padx=10)

# Button to quit the application
quit_button = tk.Button(
    frame,
    text="QUIT",
    command=root.destroy  # Use root.destroy to properly exit
)
quit_button.pack(side=tk.LEFT, padx=10)

# Start the tkinter event loop
root.mainloop()
