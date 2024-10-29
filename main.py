from time import sleep
import keyboard
from PIL import ImageGrab

        
def get_color(cordinat):
    #gets a screenshot
    image = ImageGrab.grab()
    #checks which colour a specific spot of your screen has, by coordinates
    color = image.getpixel(cordinat)
    return color

#fungtion to check if a coller has changed from the given color
def has_color_change(color):
    new_color = get_color((660, 300))
    if  new_color == color:
        print("the color has not change")
        return False
    else:
        print("the color has change")
        return True

#main loop presses enter every 200 ms until a game is joined and the screen changes
while True:
    if keyboard.is_pressed('s'):
        color = get_color((660, 300))
        print(color)
        while not has_color_change(color):
            sleep(0.2)
            keyboard.press_and_release('enter')
            if keyboard.is_pressed('w'):
                print('stoped')
                break
    elif keyboard.is_pressed('e'): #ends the pogram if key is prest out side of loop
        break
