import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = '/home/eaglestorm/Desktop/Python 20+ projects/screenshots/().png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()


