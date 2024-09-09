from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile position:
#x:  492 Y:  840 RGB: ( 78,  81, 115)
#X:  548 Y:  840 RGB: ( 77,  80, 115)
#X:  609 Y:  840 RGB: ( 78,  81, 115)
#X:  661 Y:  840 RGB: ( 83,  85, 116)


#way to perform a click

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)  #This pause the script for 0.02 secounds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q')==False:

    if pyautogui.pixel(536, 400) == (0, 0, 0):
        click(536, 400)
    if pyautogui.pixel(635, 400) == (0, 0, 0):
        click(635, 400)
    if pyautogui.pixel(727, 400) == (0, 0, 0):
        click(727, 400)
    if pyautogui.pixel(813, 400) == (0, 0, 0):
        click(813, 400)
    time.sleep(0.01)

    
    
     
