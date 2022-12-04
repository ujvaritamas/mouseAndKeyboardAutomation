import pyautogui
import time
import random


def print_mouse_position():
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    print("mouse position: x={} y={}".format(currentMouseX, currentMouseY))

def moving_the_mouse():
    screenWidth, screenHeight = pyautogui.size()
    x = random.randint(0,screenWidth-1)
    y = random.randint(0,screenWidth-1)
    pyautogui.moveTo(x, y, 2) # Move the mouse to XY coordinates.

    


screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print("screen size: {}x{}".format(screenWidth, screenHeight))


#while True:
#    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#    print("mouse position: x={} y={}".format(currentMouseX, currentMouseY))
#    time.sleep(0.1)
#pyautogui.alert(text='', title='', button='OK')

while True:
    moving_the_mouse()



pyautogui.moveTo(100, 150, 4) # Move the mouse to XY coordinates.
pyautogui.click()

print_mouse_position()