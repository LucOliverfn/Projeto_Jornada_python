from pynput.mouse import Button, Controller
from time import sleep
import pyautogui
import pyperclip
mouse = Controller()
mouse.position = (612, 1058)
mouse.click(Button.right)
mouse.position = (600, 889)
sleep(2.5)
mouse.click(Button.left)
sleep(2)
pyperclip.copy("https://web.whatsapp.com/")
sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
sleep(7)
pyautogui.click(x=295, y=493)
pyperclip.copy("OLHA O QUE EU APRENDI A FAZER PQPPPPPPPPP SOU FODAAAAA")
pyautogui.hotkey('ctrl', 'v')
sleep(1)
pyautogui.hotkey('enter')