

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
d = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print(d)


from .ui_M_Project import Ui_MainWindow

class MainWindow_Style(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_style()
    def ui_style(self):
        print('load style')
        thema = 'dark' # 'white' u"background: rgb(255, 192, 203)"
        r = 60
        g = 63
        b = 65

        rgb = f'rgb({r}, {g}, {b}'
        # color1 = u"background: rgb(60, 63, 65)"
        # color2 = u"background: rgb(43, 43, 43)"
        # color3 = u"background: rgb(89, 91, 93)"
        self.ui.centralwidget.setStyleSheet(u'''
        QFrame{
            background-color: black;
            color : rgb(43, 43, 43);
        }
        QPushButton{
            color: red;
            background-color: red;
            border-radius: 10px;
        }
        ''')

        #
        #
        # self.ui.centralwidget.setStyleSheet(color)
        # for ui in self.ui.centralwidget.children():
        #     try:
        #         ui.setStyleSheet(color)
        #     except:
        #         pass

