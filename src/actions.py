import pyautogui

def perform_action(action, *coords):
    if action == "click":
        x, y = coords
        pyautogui.click(x, y)
    elif action == "double_click":
        x, y = coords
        pyautogui.doubleClick(x, y)
    elif action == "right_click":
        x, y = coords
        pyautogui.rightClick(x, y)
    elif action == "drag_and_drop":
        x1, y1, x2, y2 = coords
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, duration=1)
    elif action == "scroll":
        x, y = coords
        pyautogui.scroll(500, x, y)  # Example scroll value, adjust as needed
    else:
        print(f"Unknown action: {action}")

# Example usage (for testing purposes)
if __name__ == "__main__":
    perform_action("click", 100, 100)
    perform_action("double_click", 200, 200)
    perform_action("right_click", 300, 300)
    perform_action("drag_and_drop", 400, 400, 500, 500)
    perform_action("scroll", 600, 600)
