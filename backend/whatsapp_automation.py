from AppOpener import open
import pyautogui
import time
def whatsapp_sasta_automation(to,message):
    open("whatsapp")
    time.sleep(5)
    pyautogui.click(x=200, y=150)  
    time.sleep(1)
    pyautogui.write(f"{to}", interval=0.1)
    time.sleep(1)
    pyautogui.click(x=200, y=200)  
    time.sleep(1)
    pyautogui.write(f"{message}", interval=0.1)
    pyautogui.press("enter")
