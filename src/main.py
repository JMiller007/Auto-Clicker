from capture import capture_screen
from instructions import interpret_instruction
from actions import perform_action
import numpy as np
import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import win32gui
import win32con
import time
import threading
from pynput import keyboard

# Global variable to control the autoclicker
running = False
instructions = []

def minimize_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

def restore_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

def perform_actions(instructions):
    for instruction in instructions:
        # Capture the screen
        screenshot = capture_screen()
        screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Interpret the instruction
        action_details_list = interpret_instruction(instruction, screenshot_np)
        for action_details in action_details_list:
            action, x, y = action_details
            perform_action(action, x, y)

def autoclicker(interval, repeat):
    global running
    count = 0
    hwnd = win32gui.GetForegroundWindow()
    minimize_window(hwnd)
    while running and (repeat == 0 or count < repeat):
        perform_actions(instructions)
        time.sleep(interval)
        count += 1
    restore_window(hwnd)

def start_autoclicker():
    global running
    running = True
    
    # Calculate interval in seconds
    hours = int(hours_entry.get() or 0)
    minutes = int(minutes_entry.get() or 0)
    seconds = int(seconds_entry.get() or 0)
    milliseconds = int(milliseconds_entry.get() or 100)
    interval = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000.0

    # Get repeat count
    repeat = int(repeat_entry.get() or 0) if repeat_var.get() == 1 else 0

    autoclicker_thread = threading.Thread(target=autoclicker, args=(interval, repeat))
    autoclicker_thread.start()
    messagebox.showinfo("Started", "Autoclicker started.")

def stop_autoclicker():
    global running
    running = False
    messagebox.showinfo("Stopped", "Autoclicker stopped.")

def add_instruction():
    instruction = new_instruction_entry.get()
    if instruction:
        instructions.append(instruction)
        instructions_listbox.insert(tk.END, instruction)
        new_instruction_entry.delete(0, tk.END)

def remove_selected_instruction():
    selected_idx = instructions_listbox.curselection()
    if selected_idx:
        instructions_listbox.delete(selected_idx)
        del instructions[selected_idx[0]]

def on_press(key):
    if key == keyboard.Key.f6:
        if running:
            stop_autoclicker()
        else:
            start_autoclicker()

if __name__ == "__main__":
    # Setup GUI
    app = tk.Tk()
    app.title("AI Auto Clicker")

    # Configure grid layout
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.columnconfigure(2, weight=1)
    app.columnconfigure(3, weight=1)
    app.columnconfigure(4, weight=1)
    app.columnconfigure(5, weight=1)
    app.columnconfigure(6, weight=1)
    app.columnconfigure(7, weight=1)

    # Instructions
    tk.Label(app, text="Enter Instruction:").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    new_instruction_entry = tk.Entry(app, width=50)
    new_instruction_entry.grid(row=0, column=2, columnspan=4, padx=5, pady=5, sticky="ew")
    tk.Button(app, text="Add", command=add_instruction).grid(row=0, column=6, padx=5, pady=5)
    tk.Button(app, text="Remove Selected", command=remove_selected_instruction).grid(row=0, column=7, padx=5, pady=5)

    instructions_listbox = tk.Listbox(app, height=10)
    instructions_listbox.grid(row=1, column=0, columnspan=8, padx=5, pady=5, sticky="ew")

    # Click Interval
    tk.Label(app, text="Click Interval").grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky="w")
    tk.Label(app, text="Hours").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    hours_entry = tk.Entry(app, width=5)
    hours_entry.insert(0, "0")
    hours_entry.grid(row=3, column=1, padx=5, pady=5)
    tk.Label(app, text="Minutes").grid(row=3, column=2, padx=5, pady=5, sticky="w")
    minutes_entry = tk.Entry(app, width=5)
    minutes_entry.insert(0, "0")
    minutes_entry.grid(row=3, column=3, padx=5, pady=5)
    tk.Label(app, text="Seconds").grid(row=3, column=4, padx=5, pady=5, sticky="w")
    seconds_entry = tk.Entry(app, width=5)
    seconds_entry.insert(0, "0")
    seconds_entry.grid(row=3, column=5, padx=5, pady=5)
    tk.Label(app, text="Milliseconds").grid(row=3, column=6, padx=5, pady=5, sticky="w")
    milliseconds_entry = tk.Entry(app, width=5)
    milliseconds_entry.insert(0, "100")
    milliseconds_entry.grid(row=3, column=7, padx=5, pady=5)

    # Click Options
    tk.Label(app, text="Click Options").grid(row=4, column=0, columnspan=8, padx=5, pady=5, sticky="w")
    tk.Label(app, text="Mouse Button:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
    mouse_button = ttk.Combobox(app, values=["Left", "Right", "Middle"], width=10)
    mouse_button.grid(row=5, column=1, padx=5, pady=5)
    mouse_button.current(0)

    tk.Label(app, text="Click Type:").grid(row=5, column=2, padx=5, pady=5, sticky="w")
    click_type = ttk.Combobox(app, values=["Single", "Double"], width=10)
    click_type.grid(row=5, column=3, padx=5, pady=5)
    click_type.current(0)

    # Click Repeat
    tk.Label(app, text="Click Repeat").grid(row=6, column=0, columnspan=8, padx=5, pady=5, sticky="w")
    repeat_var = tk.IntVar(value=1)
    tk.Radiobutton(app, text="Repeat", variable=repeat_var, value=1).grid(row=7, column=0, padx=5, pady=5, sticky="w")
    repeat_entry = tk.Entry(app, width=5)
    repeat_entry.insert(0, "0")
    repeat_entry.grid(row=7, column=1, padx=5, pady=5)
    tk.Radiobutton(app, text="Repeat until stopped", variable=repeat_var, value=0).grid(row=7, column=2, columnspan=2, padx=5, pady=5, sticky="w")

    # Hotkey Setting
    tk.Label(app, text="Hotkey Setting").grid(row=8, column=0, columnspan=8, padx=5, pady=5, sticky="w")
    tk.Label(app, text="Start / Stop").grid(row=9, column=0, padx=5, pady=5, sticky="w")
    hotkey_label = tk.Label(app, text="F6")
    hotkey_label.grid(row=9, column=1, padx=5, pady=5)

    # Start and Stop Buttons
    tk.Button(app, text="Start", command=start_autoclicker).grid(row=10, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(app, text="Stop", command=stop_autoclicker).grid(row=10, column=1, padx=5, pady=5, sticky="ew")

    # Start hotkey listener in a separate thread
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Make the GUI adaptive to window size
    for i in range(11):
        app.rowconfigure(i, weight=1)
    for i in range(8):
        app.columnconfigure(i, weight=1)

    app.mainloop()
