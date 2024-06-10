import pyautogui

def perform_action(action, x, y):
    if action == "click":
        pyautogui.click(x, y)
    elif action == "double_click":
        pyautogui.doubleClick(x, y)
    elif action == "right_click":
        pyautogui.rightClick(x, y)
