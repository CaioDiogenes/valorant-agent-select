import pyautogui
import gc
import sys

def action(champ):
    champ_location = pyautogui.locateOnScreen(champ, confidence=0.6)
    if champ_location is not None:
        x, y = pyautogui.center(champ_location)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        return True
    return False

def select_lock_in():
    select_button = pyautogui.locateOnScreen("lock in.png", confidence=0.8)
    if select_button is not None:
        a, b = pyautogui.center(select_button)
        pyautogui.moveTo(a, b)
        pyautogui.click()
        sys.exit()

def wait_for_text_and_click(champ_name):
    print(f'agent chosen: {champ_name}')
    while True:
        try:
            if action(f"valorant/{champ_name}.png"):
                select_lock_in()

        except pyautogui.ImageNotFoundException:
            pass

        gc.collect()
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python agent select.py <championName>")
        sys.exit(1)

    champion_name = sys.argv[1]
    wait_for_text_and_click(champion_name)
