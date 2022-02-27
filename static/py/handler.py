import pyautogui as pag
import subprocess
import os
from datetime import datetime

from static.py.utilsDB import *

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def getCords():
    return pag.position()

def openLocal(port):
    subprocess.call(f"start http://localhost:{port}/welcome",
        creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)

def mouseClick(bt):
    x = True if bt.x != 'None' else False
    y = True if bt.y != 'None' else False
    if x and y:
        pag.click(x=bt.x, y=bt.y, clicks=bt.clicks,
            interval=bt.interval, button=bt.button)
    else:
        pag.click(clicks=bt.clicks, interval=bt.interval, button=bt.button)


def mouseMove(bt):
    x = True if bt.x != 'None' else False
    y = True if bt.y != 'None' else False
    if x and y:
        events = [[
                lambda: pag.moveTo(bt.x, bt.y, duration=bt.duration),
                lambda: pag.moveRel(bt.x, bt.y, duration=bt.duration)
            ],[
                lambda: pag.dragTo(bt.x, bt.y,
                    duration=bt.duration, button=bt.button),
                lambda: pag.dragRel(bt.x, bt.y,
                    duration=bt.duration, button=bt.button)
            ]]
        events[bt.mode][bt.move]()

def mouseScroll(bt):
    x = True if bt.x != 'None' else False
    y = True if bt.y != 'None' else False
    if x and y:
        pag.scroll(bt.scroll, bt.x, bt.y)
    else:
        pag.scroll(int(bt.scroll))

def keyboard(bt):
    events = [
        lambda: pag.typewrite(bt.text, interval=bt.interval),
        lambda: pag.hotkey(*bt.text.split(' '), interval=bt.interval),
        lambda: pag.press(bt.text, presses=bt.presses, interval=bt.interval),
    ]
    events[bt.mode]()

def cmd(bt):
    subprocess.call(bt.text,
        creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)

def handl(id):
    button = getButton(id)
    events = {
        0: mouseClick,
        1: mouseMove,
        2: mouseScroll,
        3: keyboard,
        4: lambda bt: pag.screenshot(f"{desktop}\{datetime.now().strftime('%m-%d-%Y %H-%M')}.png"),
        5: cmd,
    }
    events[button.type](button)
