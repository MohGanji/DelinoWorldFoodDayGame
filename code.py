import pyautogui as gui
import time
from PIL import Image




gui.PAUSE = 0.04
gui.FAILSAFE = True

steakColor = (29,3,1)


try:
    width, height = gui.size()
    # while True:
    # time.sleep(3)
    img = Image.open('steak-33percentZoomOut.png')
    while True:

        r= None 
        while r is None:
             # this region is for 33% zoom out and chrome taking only left half of screen
            r=gui.locateCenterOnScreen(img,grayscale=True, confidence =.60, region = (230,162,453,345))
        # print(r)
        x, y = r
        # gui.moveTo(x, y, duration=0.1)
        gui.click( x, y )
    # place = gui.locateOnScreen('steak.png')
    # print(place)
    # im = gui.screenshot()
    # print(im.getpixel((0, 0)))
except gui.FailSafeException as e:
    print(e.args[0])
    exit()
except KeyboardInterrupt:
    print('\nDone.')
