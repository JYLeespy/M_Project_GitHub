import os
from pathlib import Path
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = 933120000

from PyQt5.QtCore import *


class ImageCrop(QObject):
    prog = pyqtSignal(bool, int)
    msg = pyqtSignal(str)
    flag = pyqtSignal(bool)
    def __init__(self, filepaths, savepath, x1, y1, x2, y2, mode=False):
        super().__init__()
        self.filepaths = filepaths
        self.savepath = savepath
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.mode = mode
        self.msg.emit(f'이미지 자르기 - Parameters x1:{x1},y1:{y1},x2:{x2},y2:{y2},savepath:{savepath}')
    def run(self):
        count = 0
        self.prog.emit(True, len(self.filepaths))
        if self.x1 != "" and self.y1 != "" and self.x2 != "" and self.y2 != "":
            x1 = int(self.x1)
            y1 = int(self.y1)
            x2 = int(self.x2)
            y2 = int(self.y2)
            for filepath in self.filepaths:

                self.dirpath = os.path.dirname(filepath)
                self.filename = os.path.basename(filepath)
                self.extension = filepath[-3:]
                self.img = Image.open(filepath)
                x_left, x_right, y_up, y_down = self.conv(x1,x2,y1,y2)
                print(f'({x1},{y1}) ({x2},{y2})  {x_left}, {x_right}, {y_up}, {y_down}')
                self.img_crop = self.img.crop((x_left, y_up, x_right, y_down))
                if self.mode: # Preview
                    self.img_crop.show()
                    self.flag.emit(True)
                    self.prog.emit(False, 1)
                    return
                else:
                    if self.savepath == "":
                        self.save_as = f'{self.dirpath}/result/'
                    else:
                        self.save_as = f'./_imageCrop/'
                    Path(self.save_as).mkdir(parents=True, exist_ok=True)
                    self.save_as += self.filename
                    self.img_crop.save(self.save_as)
                count+=1
                self.msg.emit(f'이미지 자르기({count}/{len(self.filepaths)}) - {filepath}')
                self.prog.emit(False, count)

            return
    def conv(self, x1, x2, y1, y2):
        if x1 > x2:
            x_left = x2
            x_right = x1
        elif x1 < x2:
            x_left = x1
            x_right = x2
        else:
            x_left = x1
            x_right = x2

        if y1 > y2:
            y_up = y2
            y_down = y1
        elif y1 < y2:
            y_up = y1
            y_down = y2
        else:
            y_up = y1
            y_down = y2
        return x_left, x_right, y_up, y_down

    def savepath(self):
        return self.save_path


    def show(self):
        self.img_crop.show()
