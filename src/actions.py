import pyautogui

def perform_action(action, x, y):
    if action == "click":
        pyautogui.click(x, y)
    elif action == "double_click":
        pyautogui.doubleClick(x, y)
    elif action == "right_click":
        pyautogui.rightClick(x, y)
    else:
        print(f"Unknown action: {action}")

# Example usage (for testing purposes)
if __name__ == "__main__":
    perform_action("click", 100, 100)
    perform_action("double_click", 200, 200)
    perform_action("right_click", 300, 300)
