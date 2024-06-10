from capture import capture_screen
from instructions import interpret_instruction
from actions import perform_action
import numpy as np
import cv2
import tkinter as tk
from tkinter import messagebox

def main(instruction):
    # Capture the screen
    screenshot = capture_screen()
    screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Interpret the instruction
    action_details = interpret_instruction(instruction, screenshot_np)
    if action_details:
        action, x, y = action_details
        perform_action(action, x, y)
    else:
        print("No action found for the given instruction.")

def on_submit():
    instruction = entry.get()
    try:
        main(instruction)
        messagebox.showinfo("Success", "Action performed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    # Setup GUI
    app = tk.Tk()
    app.title("AI Auto Clicker")

    tk.Label(app, text="Enter Instruction:").pack()
    entry = tk.Entry(app, width=50)
    entry.pack()
    tk.Button(app, text="Submit", command=on_submit).pack()

    app.mainloop()

    # Example user instruction (for testing without GUI)
    # user_instruction = "click on File Understanding Assistance"
    # main(user_instruction)
