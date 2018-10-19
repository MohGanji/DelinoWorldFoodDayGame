import pyautogui as gui

gui.PAUSE = 0.5
gui.FAILSAFE = True


try:
    width, height = gui.size()
    while True:
        x, y = gui.position()
        x, y = str(x).rjust(4), str(y).rjust(4)
        print (x, y, end='')
        print('\b' * 9, end='', flush=True)
except gui.FailSafeException as e:
    print(e.args[0])
    exit()
except KeyboardInterrupt:
    print('\nDone.')