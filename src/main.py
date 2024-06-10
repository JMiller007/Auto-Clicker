from capture import capture_screen
from instructions import interpret_instruction
from actions import perform_action
import numpy as np
import cv2
import tkinter as tk
from tkinter import messagebox
import win32gui
import win32con
import time

def minimize_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

def restore_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

def main(instruction):
    start_time = time.time()
    hwnd = win32gui.GetForegroundWindow()
    minimize_window(hwnd)

    try:
        # Capture the screen
        screenshot = capture_screen()
        screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Interpret the instruction
        action_details_list = interpret_instruction(instruction, screenshot_np)
        for action_details in action_details_list:
            action, x, y = action_details
            perform_action(action, x, y)
    finally:
        restore_window(hwnd)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")

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
    # user_instruction = "click on File Understanding Assistance then click on Add Team workspace"
    # main(user_instruction)
