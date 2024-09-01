import pyautogui as p


def send():
    while True:
        p.hotkey("ctrl", "v")
        p.hotkey("enter")


send()
