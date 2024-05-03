# from .func_stopkey import macro_stop


import os
import numpy as np
import cv2
import pyautogui
import pyautogui as pag
import keyboard
import time


class KeyboardMouse:
    def __init__(self):
        # from PIL import ImageGrab
        # from functools import partial
        # ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
        self.pag = pag
        # self.pag.FAILSAFE = False
        self.keyboard = keyboard

    def move(self, x, y):
        self.pag.moveTo(x, y)

    def click(self, x, y):
        self.pag.click(x, y)

    def doubleClick(self, x, y):
        self.pag.doubleClick(x, y)

    def rclick(self, x, y):
        self.pag.rightClick(x, y)

    def scroll(self, wheel):
        self.pag.scroll(wheel)

    def drag(self, x1, y1, x2, y2):
        # self.pag.moveTo(x1, y1)
        # time.sleep(0.01)
        # self.pag.dragTo(x2, y2, duration= 0.2)
        # time.sleep(0.05)
        self.pag.moveTo(x1, y1)
        time.sleep(0.01)
        self.pag.mouseDown()
        time.sleep(0.01)
        self.pag.moveTo(x2, y2)
        time.sleep(0.01)
        self.pag.mouseUp()
        time.sleep(0.01)

    def find_image(self, imgpath, confidence=0.9):
        img_path = os.path.abspath(imgpath)
        try:
            np_img = np.fromfile(img_path, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        except FileNotFoundError:
            print(f'[Error] 이미지 파일을 찾을 수 없습니다. {img_path}')
            return False, False

        try:
            left, top, width, height = self.pag.locateOnScreen(img, confidence=confidence)
            pos_x = int(left + width / 2)
            pos_y = int(top + height / 2)
            return pos_x, pos_y
        except:
            self.pag.move(10,10)
            return False, False
    def for_judge(self, x, y):
        return
    def image(self, command=None, imgfile="", x_offset=0 , y_offset= 0, delay= 0.0, limit = 5):
        # macro_stop()
        img_path = os.path.abspath(imgfile)
        try:
            np_img = np.fromfile(img_path, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        except FileNotFoundError:
            print(f'[Error] 이미지 파일을 찾을 수 없습니다. {img_path}')
            return False, 0, 0

        commands = { '클릭' : self.pag.click,
                     '이동' : self.pag.move,
                     '더블클릭' : self.pag.doubleClick,
                     '우클릭' : self.pag.rightClick,
                     '판단' : self.for_judge}

        count = 0
        x = 0
        y = 0
        judge = False
        retry = 0
        basic_confidence = 0.9
        while True:
            try:
                # print(f'print : {self.pag.locateOnScreen(img, confidence=0.9)}')
                left, top, width, height = self.pag.locateOnScreen(img, confidence=basic_confidence)
                time.sleep(0.1)
                x = left + width / 2
                y = top + height / 2
                if x == 0 and y == 0:
                    judge = False
                else:
                    judge = True
                    try:
                        commands[command](x + x_offset, y + y_offset)
                        time.sleep(delay)
                        break
                    except pyautogui.FailSafeException:
                        if not command == '판단':
                            print(f'\t[Error] FailSafeException / [{basic_confidence}] {imgfile}')
                        try:
                            time.sleep(0.1)
                            self.pag.move(100,100)
                            time.sleep(0.1)
                            self.pag.move(10,10)
                            time.sleep(0.1)
                            self.pag.move(100,100)
                            time.sleep(0.1)
                            self.pag.move(10,10)
                            time.sleep(0.1)
                            self.pag.move(100,100)
                            time.sleep(0.1)
                        except:
                            time.sleep(2)
                            pass
                        continue
            except TypeError:
                if not command == '판단':
                    print(f'\t[Error] TypeError cannot unpack non-interable NoneType object / [{basic_confidence}] {imgfile}')
                retry += 1
                time.sleep(1)
                if retry == limit:
                    judge = False
                    x = 0
                    y = 0
                    break
                else:
                    basic_confidence -= 0.1/limit
                    continue
        if not command == '판단':
            if judge:
                print(f'\t[Image Found] {command}, [{basic_confidence}]Position=({x}, {y}) / {imgfile}')
            else:
                print(f'\t[Image Not Found] {command}, [{basic_confidence}]Position=({x}, {y}) / {imgfile}')
        return judge, x + x_offset, y + y_offset

        # try:
        #     left, top, width, height = self.pag.locateOnScreen(img, confidence=0.9)
        #     x = left + width / 2
        #     y = top + height / 2
        #     if command != "판단":
        #         if x != 0 and y != 0:
        #             break
        #     elif command == "판단":
        #         break
        # except:
        #     time.sleep(0.5)
        #     count += 1
        #     if count == 20:
        #         self.pag.move(100,100)
        #     if count == limit:
        #         break
        #     pass
        # print(f'[ImageSearch] {command}, Position=({x}, {y}), 재시도 횟수={count}')
        # if command != "판단":
        #     commands[command](x+x_offset, y+y_offset)
        #     time.sleep(delay)
        # return x, y

    def img_search(self, command, imgpath, imgfile, x_off, y_off, delay):
        #강제종료
        # macro_stop()

        ima_name = imgfile
        img_path = os.path.abspath(imgfile)
        np_img = np.fromfile(img_path, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        # commands = { '클릭' : self.pag.click,
        #              '이동' : self.pag.move,
        #              '더블클릭' : self.pag.doubleClick,
        #              '우클릭' : self.pag.rightClick}

        if command == '판단':
            try:
                left, top, width, height = self.pag.locateOnScreen(img, confidence=0.9)
                x = left + width / 2
                y = top + height / 2
                self.pag.move(x, y)
                return True
            except:
                return False
        else:
            for i in range(4):
                try:

                    left, top, width, height = self.pag.locateOnScreen(img, confidence=0.9)
                    x = left + width / 2
                    y = top + height / 2


                    print(f'{ima_name} : {x}({x_off}),{y}({y_off})  {command} 후 {delay}s 대기')
                    if command == '클릭':
                        self.click(x + x_off, y + y_off)
                    elif command == '이동':
                        self.move(x + x_off, y + y_off)
                    elif command == '더블클릭':
                        self.doubleClick(x + x_off, y + y_off)
                    elif command == '우클릭':
                        self.rclick(x + x_off, y + y_off)
                    # elif command == '드래그':
                    #     self.km.drag()
                    time.sleep(delay)
                    return x, y
                except:
                    print(f'\r{ima_name} 찾기 실패 재시도 ... {i}', end="")
                    time.sleep(0.5)

    def write(self, keys):
        self.pag.write(keys)


    def position(self):
        return self.pag.position()

    def keys(self, key):
        self.pag.typewrite(key)
        # pag.write()
    def paste(self):
        self.pag.hotkey('ctrl', 'v')

    def copy(self):
        self.pag.hotkey('ctrl', 'c')

    def selectAll(self):
        self.pag.hotkey('ctrl', 'a')

    def delete(self):
        self.pag.hotkey('delete')

    def shift_right(self):
        self.pag.hotkey('shift', 'right')

    def hotkeys(self, keys):
        self.pag.hotkey(keys)

    def key_push(self, key):
        self.keyboard.press(key)
        time.sleep(0.1)
        self.keyboard.release(key)
        time.sleep(0.1)

    def key_press(self, key):
        self.keyboard.press(key)
        time.sleep(0.1)
        self.keyboard.release(key)
        time.sleep(0.1)
        # pag.keyDown(key)
    def key_release(self, key):
        self.pag.keyUp(key)

    def keydown(self, key):
        self.pag.keyDown(key)
    def keyup(self, key):
        self.pag.keyUp(key)

    def test(self,key):
        self.pag.hotkey(key)

# print(3)
# time.sleep(1)
# print(2)
# time.sleep(1)
# print(1)
# time.sleep(1)
# km = KeyboardMouse()
# km.test('up')
# time.sleep(1)
# km.test('up')
# imagepath = 'D:/ProgramData/_project/M_Project/_images/mesmacro/mes/c_mes.png'
# km.image('클릭',imagepath, delay=0.1)
