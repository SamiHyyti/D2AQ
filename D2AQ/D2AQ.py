from python_imagesearch.imagesearch import *
from pyautogui import*
import pyautogui
import keyboard
import time

bb = False
pb = False
rb = False
while not keyboard.is_pressed('esc'):
    if pyautogui.locateOnScreen('play.png', region=(1482, 1114,379,60), confidence=0.8) or pyautogui.locateOnScreen('playdire.png', region=(1482, 1114,379,60), confidence=0.8):
        pos = pyautogui.locateOnScreen('play.png',region=(1482, 1114,379,60), confidence=0.8)
        if pos != None:
            print("play position : ", pos[0], pos[1])
            click_image("play.png", pos, "left",0.25, offset=5)
        else:
            print("Play not found")
        pos = pyautogui.locateOnScreen('playdire.png',region=(1482, 1114,379,60), confidence=0.8)
        if pos != None:
            print("Playdiretide position : ", pos[0], pos[1])
            click_image("playdire.png", pos, "left",0.25, offset=5)
        else:
            print("Playdiretide not found")

    if pyautogui.locateOnScreen('accept.png',region=(541, 414,826,259), confidence=0.8):
            pos = pyautogui.locateOnScreen('accept.png',region=(541, 414,826,259), confidence=0.8)
            if pos != None:
                click_image("accept.png", pos, "left",0.25, offset=5)

    if pyautogui.locateOnScreen('random.png', confidence=0.8):
        pos = pyautogui.locateOnScreen('random.png', confidence=0.8)
        if pos != None:
            click_image("random.png", pos, "left",0.25, offset=5)

    if pyautogui.locateOnScreen('hpbars.png',region=(735, 1124,74,71),confidence=0.5):
        print("InGame")

        if not pyautogui.locateOnScreen('shopopen.png',region=(1474,64,445,904),confidence=0.8):
            keyboard.press_and_release('b')
        if not pyautogui.locateOnScreen('shoptab.png',region=(1474,64,445,904),confidence=0.8):
            upg = pyautogui.locateOnScreen('upgrades.png',region=(1474,64,445,904),confidence=0.8)
            if upg != None:
                click_image('upgrades.png',upg,"left",0.25,offset=3)

        if not (pyautogui.locateOnScreen('bm.png',region=(1100,1039,222,111),confidence=0.7) or pyautogui.locateOnScreen('bmst.png',region=(1625,967,294,121),confidence=0.7)):
            print("No Blademail Found in Inventory")
            if not pyautogui.locateOnScreen('bms.png',region=(1474,64,445,904),confidence=0.9):
                print("no bm in shop?")
            else:
                if not bb:
                    click_image('bms.png',pyautogui.locateOnScreen('bms.png',region=(1474,64,445,904),confidence=0.9),"right",0.25,offset=3)
                    bb = True
                else:
                    print("Blademail allready bought RETARD!")
        if not (pyautogui.locateOnScreen('phase.png',region=(1100,1039,222,111),confidence=0.7) or pyautogui.locateOnScreen('phasest.png',region=(1625,967,294,121),confidence=0.5)or pyautogui.locateOnScreen('phasestun.png',region=(1625,967,294,121),confidence=0.5)or pyautogui.locateOnScreen('phasestun2.png',region=(1625,967,294,121),confidence=0.5)):
            print("No Phaseboots Found in Inventory")
            if not pyautogui.locateOnScreen('phases.png',region=(1474,64,445,904),confidence=0.9):
               print("no phaseboots in shop?")
            else:
                if not pb:
                    click_image('phases.png',pyautogui.locateOnScreen('phases.png',region=(1474,64,445,904),confidence=0.9),"right",0.25,offset=3)
                    pb = True
                else:
                    print("Phaseboots allready bought RETARD!")
        if not (pyautogui.locateOnScreen('radi.png',region=(1100,1039,222,111),confidence=0.7) or pyautogui.locateOnScreen('radist.png',region=(1625,967,294,121),confidence=0.7)):
            print("No Radiance Found in Inventory")
            if not pyautogui.locateOnScreen('radis.png',region=(1474,64,445,904),confidence=0.95):
               print("no radiance in shop?")
            else:
                if not rb:
                    click_image('radis.png',pyautogui.locateOnScreen('radis.png',region=(1474,64,445,904),confidence=0.9),"right",0.25,offset=3)
                    rb = True
                else:
                    print("Radiance allready bought RETARD!")
        if pyautogui.locateOnScreen('grab.png',region=(1584,972,153,34),confidence=0.9):
            if pyautogui.locateOnScreen('bmst.png',region=(1625,967,294,121),confidence=0.7) or pyautogui.locateOnScreen('phasest.png',region=(1625,967,294,121),confidence=0.7) or pyautogui.locateOnScreen('radist.png',region=(1625,967,294,121),confidence=0.7):
                click_image('grab.png',pyautogui.locateOnScreen('grab.png',region=(1584,972,153,34),confidence=0.9),"left",0.25,offset=3)

        pos = pyautogui.locateOnScreen('continue.png', confidence=0.8)
        if pos != None:
            print("Continue position : ", pos[0], pos[1])
            click_image("continue.png", pos, "left",0.25, offset=5)
        else:
            print("Continue not found... attacking!")
            well = pyautogui.locateOnScreen('well.png', confidence=0.8)
            if well != None:
                keyboard.press_and_release('a')
                click_image("well.png", well, "left",0.25, offset=5)
    if pyautogui.locateOnScreen('continue.png',grayscale=True, confidence=0.8):
         click_image("continue.png", pyautogui.locateOnScreen('continue.png',grayscale=True, confidence=0.8), "left",0.25, offset=5)
         bb = False
         pb = False
         rb = False
    time.sleep(0.05)