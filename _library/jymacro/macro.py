from _library.functions.func_pyautogui import KeyboardMouse
from _library.functions.func_foldermake import FolderExists
import keyboard
import xml
import xml.etree.ElementTree as ET
import time
from _library.functions.func_pyautogui import KeyboardMouse
from _library.functions.func_foldermake import FolderExists
from _library.functions.func_Excel import *
from _library.functions.func_processcheck import *
from _library.functions.func_hwnd import *
from PyQt5.QtCore import *
import os
import time
import clipboard
import datetime
import win32com.client
import random
# class JY_Macro:
#     def __init__(self):
#         self.km = KeyboardMouse()
#         self.tree = ET.parse('macrofile.xml')
#         self.root = self.tree.getroot()
#         self.categorys ={'키보드':{'text':''},
#                          '마우스':{      'pos_xy':'',
#                                         'pos_offset_xy':'',
#                                         'pos_drag_xy':''},
#                          '이미지서치':{   'imagepath':'',
#                                         'retry':'',
#                                         'return':''},
#                          '작업':{         'wait':0}}
#     def run(self, find_element):
#         for element in self.root.findall(find_element):
#             category = element.find('category').text
#             action = element.find('action').text
#             for c in self.categorys[category]:
#                 elements[c] = element.find(c).text
#             self.decode(category,action,elements)
#     def decode(self, category, action, elements):
#         self.commands = {   '키보드_키입력':self.km.keys,
#                             '키보드_누르기(유지)':self.km.key_press,
#                             '키보드_떼기':self.km.key_release,
#                             '키보드_단축키':self.km.hotkeys,
#                             '마우스_클릭':self.km.click,
#                             '마우스_우클릭':self.km.rclick,
#                             '마우스_이동':self.km.move,
#                             '마우스_드래그':self.km.drag,
#                             '이미지서치':self.km.image,
#                             '작업_대기':time.sleep
#                         }
#
#         action_key = f'{category}_{action}'
#
#
#
#
#         self.commands[action_key]
#
#         # pos_x = int(value.split(',')[0])
#         # pos_y = int(value.split(',')[1])
#         # self.commands[actions](pos_x,pos_y)

class JY_Macro:
    def __init__(self):
        self.km = KeyboardMouse()
        self.tree = ET.parse('macrofile.xml')
        self.root = self.tree.getroot()
        self.command ={
                        "키보드": ["keys"],
                        "마우스":["pos_xy","pos_offset_xy","pos_drag_xy"],
                        "이미지서치":["imagepath","return"],
                        "작업":['True'],
                        "대기":["delay"]
                        }
    def run(self, find_element):
        for element in self.root.findall(find_element):
            category = element.find('category').text
            action = element.find('action').text
            temp_e = []
            for e in self.command[category]:
                temp_e.append(element.find(e).text)
            print(f'{category}_{action} : {temp_e}')
            self.decoding(category,action,temp_e)
    def decoding(self, command, action, action_data):
        command_action = f'{command}_{action}'
        if command == '키보드':
            keys = action_data[0]
            if action == '키입력':
                self.km.keys(keys)
            elif action == '누르기(유지)':
                self.km.key_press(keys)
            elif action == '떼기':
                self.km.key_release(keys)
            elif action == '단축키':
                self.km.hotkeys(keys)

        elif command == '마우스':
            pos_x = int(action_data[0].split(',')[0])
            pos_y = int(action_data[0].split(',')[1])
            pos_offset_x = int(action_data[1].split(',')[0])
            pos_offset_y = int(action_data[1].split(',')[1])
            pos_drag_x = int(action_data[2].split(',')[0])
            pos_drag_y = int(action_data[2].split(',')[1])
            if action == '클릭':
                self.km.click(pos_x+pos_offset_x,pos_y+pos_offset_y)
            elif action == '우클릭':
                self.km.rclick(pos_x + pos_offset_x, pos_y + pos_offset_y)
            elif action == '이동':
                self.km.move(pos_x + pos_offset_x, pos_y + pos_offset_y)
            elif action == '드래그':
                self.km.drag(pos_x, pos_y, pos_drag_x, pos_drag_y)
        elif command == '이미지서치':
            imagepath = action_data[0]
            returntype = action_data[1]
            self.km.image(imagepath)
        elif command == '작업':
            a = action_data[0]
        elif command == '대기':
            delay = action_data[0]

class AutoMouse(QThread):
    flag = pyqtSignal(bool)
    msg = pyqtSignal(str)
    def __init__(self, commands=[], repeats=1, stopkey='F12', delimiter='+'):
        super().__init__()
        self.km = KeyboardMouse()
        self.commands = commands
        self.repeats = repeats
        self.stopkey = stopkey
        self.delimiter= delimiter
        self.imagesearch_dict = {}

    def decord(self, command, delimiter):
        if command[0] == '#':
            return
        action = command.split(delimiter)[1]
        action_item = command.split(delimiter)[2]

        if action == '마우스':
            x = command.split(delimiter)[3]
            y = command.split(delimiter)[4]
            x_offset = command.split(delimiter)[5]
            y_offset = command.split(delimiter)[6]
            x2 = command.split(delimiter)[7]
            y2 = command.split(delimiter)[8]
            self.msg.emit(f'[{action}-{action_item}] (x,y):({x+x_offset},{y+y_offset})  (x2,y2):({x2},{y2})')
            self.action_mouse(action_item, x, y, x_offset, y_offset, x2, y2)
        elif action == '키보드':
            keys = command.split(delimiter)[3]
            self.msg.emit(f'[{action}-{action_item}] keys:{keys}')
            self.action_keyboard(action_item, keys)
        elif action == '이미지서치':
            variable = command.split(delimiter)[3]
            confidence = command.split(delimiter)[4]
            imagepath = command.split(delimiter)[5]
            self.msg.emit(f'[{action}] 결과 좌표 변수명:%{variable}  파일주소:{imagepath}')
            self.action_imageSearch(action_item, variable, confidence, imagepath)
        elif action == '대기':
            delay = command.split(delimiter)[3]
            self.msg.emit(f'[{action}] {delay}ms')
            self.action_delay(action_item, delay)
        elif action == '추가기능':
            self.action_plugin(action_item)
        else:
            return

    def run(self):
        repeat_count = 0
        while repeat_count < self.repeats:
            for command in self.commands:
                if keyboard.is_pressed(self.stopkey):
                    self.msg.emit('강제종료')
                    self.flag.emit(True)
                    return
                self.decord(command=command, delimiter=self.delimiter)
            if self.repeats != 0:
                repeat_count += 1
        self.flag.emit(True)

    def action_mouse(self, action, x, y, x_offset, y_offset, x2, y2):
        if type(x) == str:
            if x.find('%') != -1:
                x = self.imagesearch_dict[x.replace('%', '')]['x']
            elif x != 'None' and x.find('%') == -1:
                x = int(x)
        if type(y) == str:
            if y.find('%') != -1:
                y = self.imagesearch_dict[y.replace('%','')]['y']
            elif y != 'None' and y.find('%') == -1:
                y = int(y)
        if x_offset != 'None':
            x_offset = int(x_offset)
        if y_offset != 'None':
            y_offset = int(y_offset)
        if x2 != 'None':
            x2 = int(x2)
        if y2 != 'None':
            y2 = int(y2)

        if action == '좌클릭':
            self.km.click(x+x_offset,y+y_offset)
        if action == '우클릭':
            self.km.rclick(x+x_offset,y+y_offset)
        if action == '드래그':
            self.km.drag(x+x_offset,y+y_offset, x2+x_offset, y2+y_offset)
        if action == '더블클릭':
            self.km.doubleClick(x+x_offset,y+y_offset)
        if action == '이동':
            self.km.move(x+x_offset,y+y_offset)

    def command_shortcuts(self, keys):
        keys = keys.replace("%S_","")
        print(keys)
        self.km.pag.hotkey(keys.split('*')[0], keys.split('*')[1])
        # print(keys)
        # if keys == "COPY":
        #     self.km.pag.hotkey('ctrl','c')
        # if keys == "PASTE":
        #     self.km.pag.hotkey('ctrl','v')
        # if keys == "UndoCOMMAND":
        #     self.km.pag.hotkey('ctrl','z')
        # if keys == "SELECTALL":
        #     self.km.pag.hotkey('ctrl','a')
        # if keys == "EXIT":
        #     self.km.pag.hotkey('alt','f4')
    def command_functions(self, keys):
        func_num = keys[keys.find("(")+1:keys.find(")")]
        self.km.pag.hotkey(f'f{func_num}')

    def command_datetime(self, keys):
        variable = keys[keys.find("(")+1:keys.find(")")]
        if keys.find("TODAY") != -1 or keys.find("YESTERDAY") != -1:
            if keys.find("TODAY") != -1:
                date = datetime.datetime.today().strftime('%Y-%m-%d')
            else:
                date = datetime.datetime.today() - datetime.timedelta(days=1)
                date = date.strftime('%Y-%m-%d')
            print(date, variable)
            yyyy = date.split('-')[0]
            mm =  date.split('-')[1]
            dd =  date.split('-')[2]
            yy = yyyy[-2:]
            if int(mm) >= 10:
                m = mm
            else:
                m = mm[-1]
            if int(dd) >= 10:
                d = dd
            else:
                d = dd[-1]

            if variable.find('yyyy') != -1:
                variable = variable.replace('yyyy',yyyy)
            elif variable.find('yy') != -1:
                variable = variable.replace('yy', yy)
            if variable.find('mm') != -1:
                variable = variable.replace('mm', mm)
            elif variable.find('m') != -1:
                variable = variable.replace('m', m)
            if variable.find('dd') != -1:
                variable = variable.replace('dd', dd)
            elif variable.find('d') != -1:
                variable = variable.replace('d', d)
        elif keys.find("TIME") != -1:
            nowtime = datetime.datetime.now().strftime('%H:%M:%S')
            h = nowtime.split(':')[0]
            m =  nowtime.split(':')[1]
            s =  nowtime.split(':')[2]
            h_type = 'H'
            m_type = 'M'
            s_type = 'S'
            if variable.find(h_type) != -1:
                variable = variable.replace('H',h)
            if variable.find(m_type) != -1:
                variable = variable.replace('M',m)
            if variable.find(s_type) != -1:
                variable = variable.replace('S',s)
        self.command_clipboard(f'({variable})')

    def command_clipboard(self, keys):
        clipboard.copy('>_<')
        copydata = keys[keys.find("(")+1:keys.find(")")]
        clipboard.copy(copydata)
        while True:
            temp = clipboard.paste()
            if temp == '>_<':
                time.sleep(0.01)
            else:
                break
        self.msg.emit(f'CLIPBOARD에 COPY 완료 {copydata}')
    def action_keyboard(self, action, keys):
        # print('action_keyboard')
        if action == '키입력':
            # print(f'len(keys):{len(keys)}')
            if len(keys) >= 2:
                # print(f'keys[0:2]:{keys[0:2]}')
                if keys[0:2] == '%S':
                    self.command_shortcuts(keys)
                elif keys[0:2] == '%K' or keys[0:2] == '%D':
                    input_key = keys[3:]
                    self.km.pag.hotkey(input_key)
                elif keys[0:2] == '%F':
                    self.command_functions(keys)
                elif keys[0:2] == '%T':
                    self.command_datetime(keys)
                elif keys[0:2] == '%C':
                    self.command_clipboard(keys)
                else:
                    keyboard.write(keys)




        # if action == '키누르기(유지)':
        #     self.km.key_press(keys)
        # if action == '키떼기':
        #     self.km.key_release(keys)
        pass
    def action_imageSearch(self, action, variable, confidence, imagepath):
        confidence = float(confidence)
        for i in range(5):
            print(imagepath)
            x, y = self.km.find_image(imgpath=imagepath, confidence=confidence)
            if type(x) != bool and type(y) != bool:
                break
            else:
                time.sleep(0.1)
        if variable != 'None':
            var = variable.replace('%','')
            self.imagesearch_dict[var] = {'x':x, 'y':y}
        self.msg.emit(f'ImageSearch : {x}, {y}')

    def action_delay(self, action, delay):
        if delay != 'None':
            delay = int(delay)/1000
        time.sleep(delay)
        pass
    def action_plugin(self, action):
        pass

# jy = JY_Macro()
# jy.run('Profile')


# import xml.etree.ElementTree as ET
# tree = ET.parse('macrofile.xml')
# root = tree.getroot()
#
# print(root.tag)
# print(root.attrib)
# for child in root:
#     print(child.tag, child.text)
#
