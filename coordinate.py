import pyautogui
import time

print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        # Erase the previous line to update in place for a cleaner display
        print('\b' * len(positionStr), end='', flush=True)
        time.sleep(0.01) # Small delay to prevent high CPU usage
except KeyboardInterrupt:
    print('\nDone.')