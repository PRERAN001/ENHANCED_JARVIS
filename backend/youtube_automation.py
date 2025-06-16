from AppOpener import open
import webbrowser
import pyautogui
import time
def youtube_sasta_automation(channel):
    webbrowser.open("https://youtube.com")
    time.sleep(5)
    pyautogui.click(x=950, y=150)  
    time.sleep(1)
    pyautogui.write(channel,interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=600, y=550)  


