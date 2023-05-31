import pyautogui
import pyperclip
from time import sleep
pyautogui.hotkey("ctrl", "t")
sleep(2)
pyperclip.copy("www.gmail.com")
sleep(2)
pyautogui.hotkey("ctrl", "v")
sleep(2)
pyautogui.hotkey("enter")

