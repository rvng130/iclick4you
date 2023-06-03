import time
from datetime import datetime

import pyscreenshot as ImageGrab
import schedule

from pytesseract import pytesseract
from PIL import Image

import pyautogui

def take_screenshot():
    print("Taking screenshot...")

    image_name = f"screenshot-{str(datetime.now())}"
    screenshot = ImageGrab.grab(bbox=(210,115,360,160))

    filepath = f"./screenshots/{image_name}.png"

    screenshot.save(filepath)

    print("Screenshot taken...")

    return filepath

def compare_screenshots():
    path_to_tesseract = r'/usr/local/Cellar/tesseract/5.2.0/bin/tesseract'

    path_to_image = take_screenshot()

    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)
    #Extract text from image
    text = (pytesseract.image_to_string(img)).strip()
    print(text)


    #change these answers accordingly (monday and wednesday)    
    if(text == "Question 1"):
        autoclick_B()
    if(text == "Question 2"):
        autoclick_D()
    if(text == "Question 3"):
        autoclick_D()
    if(text == "Question 4"):
        autoclick_C()
    if(text == "Question 5"):
        autoclick_A()
    if(text == "Question 6"):
        autoclick_C()
    if(text == "Question 7"):
        autoclick_C()
    if(text == "Question 8"):
        autoclick_D()
    if(text == "Question 9"):
        autoclick_A()
    if(text == "Question 10"):
        autoclick_A()
    if(text == "Question 11"):
        autoclick_A()
    
def autoclick_A():
    print ("clicking A")
    pyautogui.moveTo(65, 605, duration = 1)
    pyautogui.click(65,605)

def autoclick_B(): #works
    print ("clicking B")
    pyautogui.moveTo(175, 605, duration = 1)
    pyautogui.click(175,605)

def autoclick_C(): #works
    print ("clicking C")
    pyautogui.moveTo(285, 605, duration = 1)
    pyautogui.click(285,605)

def autoclick_D():
    print ("clicking D")
    pyautogui.moveTo(385, 605, duration = 1)
    pyautogui.click(385,605)

def autoclick_E():
    print ("clicking E")
    pyautogui.moveTo(505, 607, duration = 1)
    pyautogui.click(505, 605)

def main(): 
    schedule.every(30).seconds.do(compare_screenshots)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    print("starting!")
    main()