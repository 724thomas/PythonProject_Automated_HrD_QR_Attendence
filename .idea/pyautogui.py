import pyautogui
import keyboard
import time

#get mouse position when key pressed



def get_mouse_position():
    print(pyautogui.position())

def get_mouse_position():
    while True:
        if keyboard.is_pressed("q"):
            break
        if keyboard.is_pressed("g"):
            current_position = pyautogui.position()
            print(current_position)
            time.sleep(0.2)

def get_screen_size():
    print(pyautogui.size())

def do_mouse_click(x,y,time=0.5):
    pyautogui.click(x,y)
    pyautogui.sleep(time)

screenshot = pyautogui.screenshot(region=(0,0,300,400))
print(screenshot)