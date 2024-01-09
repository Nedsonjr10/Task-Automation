import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=799, y=353)