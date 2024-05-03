from _library.functions.func_Excel import *
from PyQt5.QtCore import *


class ImageInsert(QObject):
    prog = pyqtSignal(bool, int)
    msg = pyqtSignal(str)
    flag = pyqtSignal(bool)
    def __init__(self, sheetname="", excelfilepath="", imagefilelist=[], inputcell="A1", cellsize=[], inputdir=[], inputfilename=True):
        super().__init__()
        self.excel = ExcelWings(excelfilepath)
        self.sheetnames = self.excel.sheetnames()
        self.sheetname = sheetname
        print(f'ImageInsert Init  self.excel : {self.excel}, sheetname :{self.sheetname}')

        self.imagefilelist = imagefilelist
        row = ''
        col = ''
        for i in inputcell:
            try:
                int(i)
                row += i
            except:
                col += i
        self.excelfilepath = excelfilepath
        self.col = self.excel.reverse_cols(col)
        self.row = int(row)
        self.cellsize = cellsize    #['h', '0']
        self.inputdir = inputdir    #['r', '0']
        self.inputfilename = inputfilename #True
    def run(self):
        self.msg.emit('Image Insert Start...')
        self.excel = ExcelWings(self.excelfilepath)
        count = 0
        insertdir = self.inputdir[0]
        insertcount = self.inputdir[1]
        self.prog.emit(True, len(self.imagefilelist))
        insert_col = 0
        if insertdir == 'c':
            insert_col = self.col
        for imagefile in self.imagefilelist:
            if insertdir == 'd':
                self.row += 1
            if insertdir == 'r':
                self.col += 1
            if insertdir == 'c':
                col_num = count%insertcount
                self.col = insert_col + col_num
                if col_num == 0:
                    self.row += 1
            self.excel.image_insert(img_file=imagefile, sheetname=self.sheetname, col=self.excel.convert_cols(self.col-1), row=self.row-1, resize=self.cellsize)
            count += 1
            self.msg.emit(f'({count}/{len(self.imagefilelist)})sheetname:{self.sheetname} / cell:{self.excel.convert_cols(self.col)}{self.row} / file:{imagefile}')
            self.prog.emit(False,count)
        self.flag.emit(True)