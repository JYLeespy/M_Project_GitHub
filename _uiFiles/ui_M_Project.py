# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'M_ProjectDAudch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1043, 790)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 40))
        self.frame_top.setMaximumSize(QSize(16777215, 40))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_Topbar = QLabel(self.frame_top)
        self.label_Topbar.setObjectName(u"label_Topbar")
        self.label_Topbar.setMinimumSize(QSize(450, 25))
        self.label_Topbar.setLineWidth(1)
        self.label_Topbar.setTextFormat(Qt.AutoText)
        self.label_Topbar.setWordWrap(False)
        self.label_Topbar.setMargin(0)

        self.horizontalLayout.addWidget(self.label_Topbar)

        self.horizontalSpacer = QSpacerItem(157, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.progressBar = QProgressBar(self.frame_top)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(200, 25))
        self.progressBar.setMaximumSize(QSize(200, 16777215))
        self.progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.progressBar)

        self.btn_version = QPushButton(self.frame_top)
        self.btn_version.setObjectName(u"btn_version")
        self.btn_version.setMinimumSize(QSize(60, 25))
        self.btn_version.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.btn_version)

        self.btn_settings = QPushButton(self.frame_top)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(60, 25))
        self.btn_settings.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.btn_settings)


        self.verticalLayout_3.addWidget(self.frame_top)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line)

        self.frame_24 = QFrame(self.centralwidget)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_24)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(120, 0))
        self.frame_menu.setMaximumSize(QSize(120, 16777215))
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.btn_page_imagecrop = QPushButton(self.frame_menu)
        self.btn_page_imagecrop.setObjectName(u"btn_page_imagecrop")
        self.btn_page_imagecrop.setMinimumSize(QSize(0, 40))
        self.btn_page_imagecrop.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.btn_page_imagecrop)

        self.btn_page_imageinsert = QPushButton(self.frame_menu)
        self.btn_page_imageinsert.setObjectName(u"btn_page_imageinsert")
        self.btn_page_imageinsert.setMinimumSize(QSize(0, 40))
        self.btn_page_imageinsert.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.btn_page_imageinsert)

        self.btn_page_csvmerge = QPushButton(self.frame_menu)
        self.btn_page_csvmerge.setObjectName(u"btn_page_csvmerge")
        self.btn_page_csvmerge.setMinimumSize(QSize(0, 40))
        self.btn_page_csvmerge.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.btn_page_csvmerge)

        self.btn_page_omm = QPushButton(self.frame_menu)
        self.btn_page_omm.setObjectName(u"btn_page_omm")
        self.btn_page_omm.setMinimumSize(QSize(0, 40))
        self.btn_page_omm.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.btn_page_omm)

        self.line_8 = QFrame(self.frame_menu)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_8)

        self.btn_page_oismenu = QPushButton(self.frame_menu)
        self.btn_page_oismenu.setObjectName(u"btn_page_oismenu")
        self.btn_page_oismenu.setMinimumSize(QSize(0, 40))
        self.btn_page_oismenu.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.btn_page_oismenu)

        self.line_12 = QFrame(self.frame_menu)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_12)

        self.btn_page_automouse = QPushButton(self.frame_menu)
        self.btn_page_automouse.setObjectName(u"btn_page_automouse")
        self.btn_page_automouse.setMinimumSize(QSize(0, 40))
        self.btn_page_automouse.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.btn_page_automouse)

        self.verticalSpacer = QSpacerItem(20, 239, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer)

        self.btn_page_settings = QPushButton(self.frame_menu)
        self.btn_page_settings.setObjectName(u"btn_page_settings")
        self.btn_page_settings.setMinimumSize(QSize(0, 40))
        self.btn_page_settings.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.btn_page_settings)

        self.btn_page_exit = QPushButton(self.frame_menu)
        self.btn_page_exit.setObjectName(u"btn_page_exit")
        self.btn_page_exit.setMinimumSize(QSize(0, 40))
        self.btn_page_exit.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.btn_page_exit)


        self.horizontalLayout_28.addWidget(self.frame_menu)

        self.frame_avimenu = QFrame(self.frame_24)
        self.frame_avimenu.setObjectName(u"frame_avimenu")
        self.frame_avimenu.setMaximumSize(QSize(0, 16777215))
        self.frame_avimenu.setFrameShape(QFrame.StyledPanel)
        self.frame_avimenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_avimenu)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.btn_page_avi_avigraph = QPushButton(self.frame_avimenu)
        self.btn_page_avi_avigraph.setObjectName(u"btn_page_avi_avigraph")
        self.btn_page_avi_avigraph.setMinimumSize(QSize(0, 30))

        self.verticalLayout_44.addWidget(self.btn_page_avi_avigraph)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_4)


        self.horizontalLayout_28.addWidget(self.frame_avimenu)

        self.frame_oismenu = QFrame(self.frame_24)
        self.frame_oismenu.setObjectName(u"frame_oismenu")
        self.frame_oismenu.setMinimumSize(QSize(0, 0))
        self.frame_oismenu.setMaximumSize(QSize(0, 16777214))
        self.frame_oismenu.setFrameShape(QFrame.StyledPanel)
        self.frame_oismenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_oismenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_page_ngreport = QPushButton(self.frame_oismenu)
        self.btn_page_ngreport.setObjectName(u"btn_page_ngreport")
        self.btn_page_ngreport.setMinimumSize(QSize(0, 40))
        self.btn_page_ngreport.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.btn_page_ngreport)

        self.btn_page_mes = QPushButton(self.frame_oismenu)
        self.btn_page_mes.setObjectName(u"btn_page_mes")
        self.btn_page_mes.setMinimumSize(QSize(0, 40))
        self.btn_page_mes.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.btn_page_mes)

        self.btn_page_logdownload = QPushButton(self.frame_oismenu)
        self.btn_page_logdownload.setObjectName(u"btn_page_logdownload")
        self.btn_page_logdownload.setMinimumSize(QSize(0, 40))
        self.btn_page_logdownload.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.btn_page_logdownload)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)


        self.horizontalLayout_28.addWidget(self.frame_oismenu)

        self.line_2 = QFrame(self.frame_24)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_28.addWidget(self.line_2)

        self.frame_main = QFrame(self.frame_24)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setMinimumSize(QSize(900, 0))
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_main)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(900, 600))
        self.stackedWidget.setMaximumSize(QSize(16777215, 600))
        self.stackedWidget.setStyleSheet(u"")
        self.page_imagecrop = QWidget()
        self.page_imagecrop.setObjectName(u"page_imagecrop")
        self.page_imagecrop.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.page_imagecrop)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_14 = QLabel(self.page_imagecrop)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_32.addWidget(self.label_14)

        self.frame_26 = QFrame(self.page_imagecrop)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_imagecrop_image = QLabel(self.frame_26)
        self.label_imagecrop_image.setObjectName(u"label_imagecrop_image")
        self.label_imagecrop_image.setMinimumSize(QSize(550, 550))
        self.label_imagecrop_image.setMaximumSize(QSize(550, 550))
        self.label_imagecrop_image.setCursor(QCursor(Qt.CrossCursor))
        self.label_imagecrop_image.setStyleSheet(u"border-color: gray;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 1px;")

        self.horizontalLayout_29.addWidget(self.label_imagecrop_image)

        self.groupBox_23 = QGroupBox(self.frame_26)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.verticalLayout_37 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_28 = QFrame(self.groupBox_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_28)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_30.addWidget(self.label_16)

        self.line_imagecrop_path = QLineEdit(self.frame_28)
        self.line_imagecrop_path.setObjectName(u"line_imagecrop_path")

        self.horizontalLayout_30.addWidget(self.line_imagecrop_path)

        self.btn_imagecrop_path = QPushButton(self.frame_28)
        self.btn_imagecrop_path.setObjectName(u"btn_imagecrop_path")

        self.horizontalLayout_30.addWidget(self.btn_imagecrop_path)


        self.verticalLayout_37.addWidget(self.frame_28)

        self.frame_33 = QFrame(self.groupBox_23)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_37.addWidget(self.frame_33)

        self.list_imagecrop_filelist = QListWidget(self.groupBox_23)
        self.list_imagecrop_filelist.setObjectName(u"list_imagecrop_filelist")

        self.verticalLayout_37.addWidget(self.list_imagecrop_filelist)

        self.label_imagecrop_fileinfo = QLabel(self.groupBox_23)
        self.label_imagecrop_fileinfo.setObjectName(u"label_imagecrop_fileinfo")

        self.verticalLayout_37.addWidget(self.label_imagecrop_fileinfo)

        self.groupBox_29 = QGroupBox(self.groupBox_23)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.horizontalLayout_33 = QHBoxLayout(self.groupBox_29)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.groupBox_24 = QGroupBox(self.groupBox_29)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.horizontalLayout_31 = QHBoxLayout(self.groupBox_24)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_17 = QLabel(self.groupBox_24)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_31.addWidget(self.label_17)

        self.line_imagecrop_x1 = QLineEdit(self.groupBox_24)
        self.line_imagecrop_x1.setObjectName(u"line_imagecrop_x1")

        self.horizontalLayout_31.addWidget(self.line_imagecrop_x1)

        self.label_18 = QLabel(self.groupBox_24)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_31.addWidget(self.label_18)

        self.line_imagecrop_y1 = QLineEdit(self.groupBox_24)
        self.line_imagecrop_y1.setObjectName(u"line_imagecrop_y1")

        self.horizontalLayout_31.addWidget(self.line_imagecrop_y1)


        self.horizontalLayout_33.addWidget(self.groupBox_24)

        self.groupBox_25 = QGroupBox(self.groupBox_29)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.horizontalLayout_32 = QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_19 = QLabel(self.groupBox_25)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_32.addWidget(self.label_19)

        self.line_imagecrop_x2 = QLineEdit(self.groupBox_25)
        self.line_imagecrop_x2.setObjectName(u"line_imagecrop_x2")

        self.horizontalLayout_32.addWidget(self.line_imagecrop_x2)

        self.label_20 = QLabel(self.groupBox_25)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_32.addWidget(self.label_20)

        self.line_imagecrop_y2 = QLineEdit(self.groupBox_25)
        self.line_imagecrop_y2.setObjectName(u"line_imagecrop_y2")

        self.horizontalLayout_32.addWidget(self.line_imagecrop_y2)


        self.horizontalLayout_33.addWidget(self.groupBox_25)


        self.verticalLayout_37.addWidget(self.groupBox_29)

        self.groupBox_30 = QGroupBox(self.groupBox_23)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_30)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.groupBox_26 = QGroupBox(self.groupBox_30)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_36 = QHBoxLayout(self.groupBox_26)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(9, 0, 9, 0)
        self.combo_imagecrop_reciepe = QComboBox(self.groupBox_26)
        self.combo_imagecrop_reciepe.setObjectName(u"combo_imagecrop_reciepe")

        self.horizontalLayout_36.addWidget(self.combo_imagecrop_reciepe)


        self.verticalLayout_34.addWidget(self.groupBox_26)

        self.groupBox_27 = QGroupBox(self.groupBox_30)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setMinimumSize(QSize(0, 0))
        self.verticalLayout_35 = QVBoxLayout(self.groupBox_27)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_30 = QFrame(self.groupBox_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 0))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_30)
        self.verticalLayout_33.setSpacing(3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_32)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_37.addWidget(self.label_21)

        self.line_imagecrop_reciepename = QLineEdit(self.frame_32)
        self.line_imagecrop_reciepename.setObjectName(u"line_imagecrop_reciepename")

        self.horizontalLayout_37.addWidget(self.line_imagecrop_reciepename)


        self.verticalLayout_33.addWidget(self.frame_32)

        self.frame_29 = QFrame(self.frame_30)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.btn_imagecrop_reciepe_add = QPushButton(self.frame_29)
        self.btn_imagecrop_reciepe_add.setObjectName(u"btn_imagecrop_reciepe_add")

        self.horizontalLayout_35.addWidget(self.btn_imagecrop_reciepe_add)

        self.btn_imagecrop_reciepe_delete = QPushButton(self.frame_29)
        self.btn_imagecrop_reciepe_delete.setObjectName(u"btn_imagecrop_reciepe_delete")

        self.horizontalLayout_35.addWidget(self.btn_imagecrop_reciepe_delete)


        self.verticalLayout_33.addWidget(self.frame_29)


        self.verticalLayout_35.addWidget(self.frame_30)


        self.verticalLayout_34.addWidget(self.groupBox_27)


        self.verticalLayout_37.addWidget(self.groupBox_30)

        self.groupBox_28 = QGroupBox(self.groupBox_23)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_28)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.radio_imagecrop_save_result = QRadioButton(self.groupBox_28)
        self.radio_imagecrop_save_result.setObjectName(u"radio_imagecrop_save_result")
        self.radio_imagecrop_save_result.setChecked(True)

        self.verticalLayout_36.addWidget(self.radio_imagecrop_save_result)

        self.radio_imagecrop_save_desktop = QRadioButton(self.groupBox_28)
        self.radio_imagecrop_save_desktop.setObjectName(u"radio_imagecrop_save_desktop")

        self.verticalLayout_36.addWidget(self.radio_imagecrop_save_desktop)


        self.verticalLayout_37.addWidget(self.groupBox_28)

        self.frame_31 = QFrame(self.groupBox_23)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 0, -1, 0)
        self.btn_imagecrop_preview = QPushButton(self.frame_31)
        self.btn_imagecrop_preview.setObjectName(u"btn_imagecrop_preview")
        self.btn_imagecrop_preview.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_34.addWidget(self.btn_imagecrop_preview)

        self.btn_imagecrop_run = QPushButton(self.frame_31)
        self.btn_imagecrop_run.setObjectName(u"btn_imagecrop_run")
        self.btn_imagecrop_run.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_34.addWidget(self.btn_imagecrop_run)


        self.verticalLayout_37.addWidget(self.frame_31)


        self.horizontalLayout_29.addWidget(self.groupBox_23)


        self.verticalLayout_32.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.page_imagecrop)
        self.page_imageinsert = QWidget()
        self.page_imageinsert.setObjectName(u"page_imageinsert")
        self.verticalLayout_38 = QVBoxLayout(self.page_imageinsert)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_15 = QLabel(self.page_imageinsert)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_38.addWidget(self.label_15)

        self.frame_34 = QFrame(self.page_imageinsert)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_34)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_34)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_42)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_41)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.groupBox_31 = QGroupBox(self.frame_41)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setMinimumSize(QSize(0, 0))
        self.groupBox_31.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_40 = QVBoxLayout(self.groupBox_31)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(9, 9, 9, 9)
        self.frame_35 = QFrame(self.groupBox_31)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_35)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_40.addWidget(self.label_22)

        self.line_imageinsert_excelfilepath = QLineEdit(self.frame_35)
        self.line_imageinsert_excelfilepath.setObjectName(u"line_imageinsert_excelfilepath")

        self.horizontalLayout_40.addWidget(self.line_imageinsert_excelfilepath)

        self.btn_imageinsert_load = QPushButton(self.frame_35)
        self.btn_imageinsert_load.setObjectName(u"btn_imageinsert_load")

        self.horizontalLayout_40.addWidget(self.btn_imageinsert_load)


        self.verticalLayout_40.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.groupBox_31)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_36)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_39.addWidget(self.label_23)

        self.combo_imageinsert_sheets = QComboBox(self.frame_36)
        self.combo_imageinsert_sheets.setObjectName(u"combo_imageinsert_sheets")
        self.combo_imageinsert_sheets.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_39.addWidget(self.combo_imageinsert_sheets)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_6)

        self.line_11 = QFrame(self.frame_36)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_39.addWidget(self.line_11)

        self.label_26 = QLabel(self.frame_36)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_39.addWidget(self.label_26)

        self.line_imageinsert_celladdress = QLineEdit(self.frame_36)
        self.line_imageinsert_celladdress.setObjectName(u"line_imageinsert_celladdress")
        self.line_imageinsert_celladdress.setMinimumSize(QSize(50, 0))
        self.line_imageinsert_celladdress.setMaximumSize(QSize(50, 16777215))
        self.line_imageinsert_celladdress.setText(u"A1")
        self.line_imageinsert_celladdress.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.line_imageinsert_celladdress)


        self.verticalLayout_40.addWidget(self.frame_36)


        self.verticalLayout_42.addWidget(self.groupBox_31)

        self.frame_37 = QFrame(self.frame_41)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.groupBox_37 = QGroupBox(self.frame_37)
        self.groupBox_37.setObjectName(u"groupBox_37")
        self.groupBox_37.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_44 = QHBoxLayout(self.groupBox_37)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(9, 9, 9, 9)
        self.radio_imageinsert_dir_right = QRadioButton(self.groupBox_37)
        self.radio_imageinsert_dir_right.setObjectName(u"radio_imageinsert_dir_right")
        self.radio_imageinsert_dir_right.setChecked(False)

        self.horizontalLayout_44.addWidget(self.radio_imageinsert_dir_right)

        self.radio_imageinsert_dir_down = QRadioButton(self.groupBox_37)
        self.radio_imageinsert_dir_down.setObjectName(u"radio_imageinsert_dir_down")

        self.horizontalLayout_44.addWidget(self.radio_imageinsert_dir_down)

        self.line_10 = QFrame(self.groupBox_37)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_44.addWidget(self.line_10)

        self.radio_imageinsert_dir_complex = QRadioButton(self.groupBox_37)
        self.radio_imageinsert_dir_complex.setObjectName(u"radio_imageinsert_dir_complex")
        self.radio_imageinsert_dir_complex.setChecked(True)

        self.horizontalLayout_44.addWidget(self.radio_imageinsert_dir_complex)

        self.label_24 = QLabel(self.groupBox_37)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.label_24)

        self.line_imageinsert_dir_complex = QLineEdit(self.groupBox_37)
        self.line_imageinsert_dir_complex.setObjectName(u"line_imageinsert_dir_complex")
        self.line_imageinsert_dir_complex.setMinimumSize(QSize(40, 0))
        self.line_imageinsert_dir_complex.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_44.addWidget(self.line_imageinsert_dir_complex)


        self.horizontalLayout_46.addWidget(self.groupBox_37)

        self.groupBox_35 = QGroupBox(self.frame_37)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.horizontalLayout_45 = QHBoxLayout(self.groupBox_35)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.check_imageinsert_insertfilename = QCheckBox(self.groupBox_35)
        self.check_imageinsert_insertfilename.setObjectName(u"check_imageinsert_insertfilename")

        self.horizontalLayout_45.addWidget(self.check_imageinsert_insertfilename)


        self.horizontalLayout_46.addWidget(self.groupBox_35)


        self.verticalLayout_42.addWidget(self.frame_37)


        self.horizontalLayout_47.addWidget(self.frame_41)

        self.groupBox_36 = QGroupBox(self.frame_42)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_39 = QVBoxLayout(self.groupBox_36)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.radio_imageinsert_fit_height = QRadioButton(self.groupBox_36)
        self.radio_imageinsert_fit_height.setObjectName(u"radio_imageinsert_fit_height")
        self.radio_imageinsert_fit_height.setChecked(True)

        self.verticalLayout_39.addWidget(self.radio_imageinsert_fit_height)

        self.radio_imageinsert_fit_width = QRadioButton(self.groupBox_36)
        self.radio_imageinsert_fit_width.setObjectName(u"radio_imageinsert_fit_width")

        self.verticalLayout_39.addWidget(self.radio_imageinsert_fit_width)

        self.line_9 = QFrame(self.groupBox_36)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_9)

        self.radio_imageinsert_set_height = QRadioButton(self.groupBox_36)
        self.radio_imageinsert_set_height.setObjectName(u"radio_imageinsert_set_height")

        self.verticalLayout_39.addWidget(self.radio_imageinsert_set_height)

        self.radio_imageinsert_set_width = QRadioButton(self.groupBox_36)
        self.radio_imageinsert_set_width.setObjectName(u"radio_imageinsert_set_width")

        self.verticalLayout_39.addWidget(self.radio_imageinsert_set_width)

        self.line_imageinsert_set_size = QLineEdit(self.groupBox_36)
        self.line_imageinsert_set_size.setObjectName(u"line_imageinsert_set_size")
        self.line_imageinsert_set_size.setMinimumSize(QSize(100, 0))
        self.line_imageinsert_set_size.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_39.addWidget(self.line_imageinsert_set_size)


        self.horizontalLayout_47.addWidget(self.groupBox_36)


        self.verticalLayout_43.addWidget(self.frame_42)

        self.groupBox_32 = QGroupBox(self.frame_34)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.verticalLayout_41 = QVBoxLayout(self.groupBox_32)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_39 = QFrame(self.groupBox_32)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_25 = QLabel(self.frame_39)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_42.addWidget(self.label_25)

        self.line_imageinsert_imagepath = QLineEdit(self.frame_39)
        self.line_imageinsert_imagepath.setObjectName(u"line_imageinsert_imagepath")
        self.line_imageinsert_imagepath.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_42.addWidget(self.line_imageinsert_imagepath)

        self.btn_imageinsert_imagepath_load = QPushButton(self.frame_39)
        self.btn_imageinsert_imagepath_load.setObjectName(u"btn_imageinsert_imagepath_load")

        self.horizontalLayout_42.addWidget(self.btn_imageinsert_imagepath_load)

        self.btn_imageinsert_imagepath_add = QPushButton(self.frame_39)
        self.btn_imageinsert_imagepath_add.setObjectName(u"btn_imageinsert_imagepath_add")

        self.horizontalLayout_42.addWidget(self.btn_imageinsert_imagepath_add)

        self.btn_imageinsert_imagepath_clear = QPushButton(self.frame_39)
        self.btn_imageinsert_imagepath_clear.setObjectName(u"btn_imageinsert_imagepath_clear")

        self.horizontalLayout_42.addWidget(self.btn_imageinsert_imagepath_clear)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_8)

        self.btn_imageinsert_run = QPushButton(self.frame_39)
        self.btn_imageinsert_run.setObjectName(u"btn_imageinsert_run")

        self.horizontalLayout_42.addWidget(self.btn_imageinsert_run)


        self.verticalLayout_41.addWidget(self.frame_39)

        self.line_3 = QFrame(self.groupBox_32)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_41.addWidget(self.line_3)

        self.label_imageinsert_imagepath_load_result = QLabel(self.groupBox_32)
        self.label_imageinsert_imagepath_load_result.setObjectName(u"label_imageinsert_imagepath_load_result")
        self.label_imageinsert_imagepath_load_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.label_imageinsert_imagepath_load_result)

        self.frame_40 = QFrame(self.groupBox_32)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_43.setSpacing(3)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.list_imageinsert_imagepathlist = QListWidget(self.frame_40)
        self.list_imageinsert_imagepathlist.setObjectName(u"list_imageinsert_imagepathlist")

        self.horizontalLayout_43.addWidget(self.list_imageinsert_imagepathlist)

        self.label_imageinsert_image = QLabel(self.frame_40)
        self.label_imageinsert_image.setObjectName(u"label_imageinsert_image")
        self.label_imageinsert_image.setMinimumSize(QSize(300, 300))
        self.label_imageinsert_image.setMaximumSize(QSize(300, 300))
        self.label_imageinsert_image.setStyleSheet(u"border-color: gray;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 1px;")

        self.horizontalLayout_43.addWidget(self.label_imageinsert_image)


        self.verticalLayout_41.addWidget(self.frame_40)


        self.verticalLayout_43.addWidget(self.groupBox_32)


        self.verticalLayout_38.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.page_imageinsert)
        self.page_ngreport = QWidget()
        self.page_ngreport.setObjectName(u"page_ngreport")
        self.verticalLayout_20 = QVBoxLayout(self.page_ngreport)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_9 = QLabel(self.page_ngreport)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_20.addWidget(self.label_9)

        self.groupBox_3 = QGroupBox(self.page_ngreport)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 120))
        self.groupBox_2.setMaximumSize(QSize(16777215, 120))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.check_ngimage_mes = QCheckBox(self.groupBox_2)
        self.check_ngimage_mes.setObjectName(u"check_ngimage_mes")
        self.check_ngimage_mes.setChecked(True)

        self.verticalLayout_2.addWidget(self.check_ngimage_mes)

        self.check_ngimage_las = QCheckBox(self.groupBox_2)
        self.check_ngimage_las.setObjectName(u"check_ngimage_las")
        self.check_ngimage_las.setChecked(True)

        self.verticalLayout_2.addWidget(self.check_ngimage_las)

        self.check_ngimage_excel = QCheckBox(self.groupBox_2)
        self.check_ngimage_excel.setObjectName(u"check_ngimage_excel")
        self.check_ngimage_excel.setChecked(True)

        self.verticalLayout_2.addWidget(self.check_ngimage_excel)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.frame_7 = QFrame(self.groupBox_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 54))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_7)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.line_ngimage_datefrom = QLineEdit(self.groupBox)
        self.line_ngimage_datefrom.setObjectName(u"line_ngimage_datefrom")
        self.line_ngimage_datefrom.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.line_ngimage_datefrom)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.groupBox_7 = QGroupBox(self.frame_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.line_ngimage_dateto = QLineEdit(self.groupBox_7)
        self.line_ngimage_dateto.setObjectName(u"line_ngimage_dateto")
        self.line_ngimage_dateto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.line_ngimage_dateto)


        self.horizontalLayout_8.addWidget(self.groupBox_7)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_3 = QFrame(self.groupBox_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_ngimage_selectall = QPushButton(self.frame_3)
        self.btn_ngimage_selectall.setObjectName(u"btn_ngimage_selectall")

        self.horizontalLayout_4.addWidget(self.btn_ngimage_selectall)

        self.btn_ngimage_run = QPushButton(self.frame_3)
        self.btn_ngimage_run.setObjectName(u"btn_ngimage_run")

        self.horizontalLayout_4.addWidget(self.btn_ngimage_run)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)


        self.verticalLayout_20.addWidget(self.groupBox_3)

        self.stackedWidget.addWidget(self.page_ngreport)
        self.page_mes = QWidget()
        self.page_mes.setObjectName(u"page_mes")
        self.verticalLayout_18 = QVBoxLayout(self.page_mes)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_8 = QLabel(self.page_mes)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 20))
        self.label_8.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_18.addWidget(self.label_8)

        self.groupBox_4 = QGroupBox(self.page_mes)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 120))
        self.groupBox_5.setMaximumSize(QSize(16777215, 120))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.check_mes_outlook = QCheckBox(self.groupBox_5)
        self.check_mes_outlook.setObjectName(u"check_mes_outlook")
        self.check_mes_outlook.setChecked(True)

        self.verticalLayout_6.addWidget(self.check_mes_outlook)

        self.check_mes_mes = QCheckBox(self.groupBox_5)
        self.check_mes_mes.setObjectName(u"check_mes_mes")
        self.check_mes_mes.setChecked(True)

        self.verticalLayout_6.addWidget(self.check_mes_mes)

        self.check_mes_las = QCheckBox(self.groupBox_5)
        self.check_mes_las.setObjectName(u"check_mes_las")
        self.check_mes_las.setChecked(True)

        self.verticalLayout_6.addWidget(self.check_mes_las)

        self.check_mes_excel = QCheckBox(self.groupBox_5)
        self.check_mes_excel.setObjectName(u"check_mes_excel")
        self.check_mes_excel.setChecked(True)

        self.verticalLayout_6.addWidget(self.check_mes_excel)


        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.frame_8 = QFrame(self.groupBox_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 54))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.frame_8)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 0))
        self.groupBox_6.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.line_mes_datefrom = QLineEdit(self.groupBox_6)
        self.line_mes_datefrom.setObjectName(u"line_mes_datefrom")
        self.line_mes_datefrom.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.line_mes_datefrom)


        self.horizontalLayout_10.addWidget(self.groupBox_6)

        self.groupBox_8 = QGroupBox(self.frame_8)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 0))
        self.groupBox_8.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.line_mes_dateto = QLineEdit(self.groupBox_8)
        self.line_mes_dateto.setObjectName(u"line_mes_dateto")
        self.line_mes_dateto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.line_mes_dateto)


        self.horizontalLayout_10.addWidget(self.groupBox_8)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.groupBox_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_mes_selectall = QPushButton(self.frame_6)
        self.btn_mes_selectall.setObjectName(u"btn_mes_selectall")

        self.horizontalLayout_6.addWidget(self.btn_mes_selectall)

        self.btn_mes_run = QPushButton(self.frame_6)
        self.btn_mes_run.setObjectName(u"btn_mes_run")

        self.horizontalLayout_6.addWidget(self.btn_mes_run)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)


        self.verticalLayout_18.addWidget(self.groupBox_4)

        self.stackedWidget.addWidget(self.page_mes)
        self.page_logdownload = QWidget()
        self.page_logdownload.setObjectName(u"page_logdownload")
        self.verticalLayout_25 = QVBoxLayout(self.page_logdownload)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_7 = QLabel(self.page_logdownload)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_25.addWidget(self.label_7)

        self.frame = QFrame(self.page_logdownload)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(470, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(357, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.groupBox_9 = QGroupBox(self.frame_15)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 0))
        self.groupBox_9.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_11 = QFrame(self.groupBox_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 60))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_11)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.check_log_mc1 = QCheckBox(self.frame_9)
        self.check_log_mc1.setObjectName(u"check_log_mc1")

        self.verticalLayout_15.addWidget(self.check_log_mc1)

        self.check_log_mc2 = QCheckBox(self.frame_9)
        self.check_log_mc2.setObjectName(u"check_log_mc2")

        self.verticalLayout_15.addWidget(self.check_log_mc2)

        self.check_log_mc3 = QCheckBox(self.frame_9)
        self.check_log_mc3.setObjectName(u"check_log_mc3")

        self.verticalLayout_15.addWidget(self.check_log_mc3)


        self.horizontalLayout_14.addWidget(self.frame_9)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.check_log_mc4 = QCheckBox(self.frame_12)
        self.check_log_mc4.setObjectName(u"check_log_mc4")

        self.verticalLayout_16.addWidget(self.check_log_mc4)

        self.check_log_mc5 = QCheckBox(self.frame_12)
        self.check_log_mc5.setObjectName(u"check_log_mc5")

        self.verticalLayout_16.addWidget(self.check_log_mc5)

        self.checkBox_18 = QCheckBox(self.frame_12)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.verticalLayout_16.addWidget(self.checkBox_18)


        self.horizontalLayout_14.addWidget(self.frame_12)


        self.verticalLayout_10.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.groupBox_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_log_mc_selectall = QPushButton(self.frame_10)
        self.btn_log_mc_selectall.setObjectName(u"btn_log_mc_selectall")
        self.btn_log_mc_selectall.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_15.addWidget(self.btn_log_mc_selectall)


        self.verticalLayout_10.addWidget(self.frame_10)


        self.verticalLayout_17.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.frame_15)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(0, 160))
        self.groupBox_10.setMaximumSize(QSize(16777215, 160))
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_2 = QFrame(self.groupBox_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.groupBox_12 = QGroupBox(self.frame_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.check_log_secsgem = QCheckBox(self.groupBox_12)
        self.check_log_secsgem.setObjectName(u"check_log_secsgem")

        self.verticalLayout_11.addWidget(self.check_log_secsgem)

        self.check_log_sequence = QCheckBox(self.groupBox_12)
        self.check_log_sequence.setObjectName(u"check_log_sequence")

        self.verticalLayout_11.addWidget(self.check_log_sequence)

        self.check_log_mmi = QCheckBox(self.groupBox_12)
        self.check_log_mmi.setObjectName(u"check_log_mmi")

        self.verticalLayout_11.addWidget(self.check_log_mmi)


        self.horizontalLayout_13.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.frame_2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.check_log_mcinfo = QCheckBox(self.groupBox_13)
        self.check_log_mcinfo.setObjectName(u"check_log_mcinfo")

        self.verticalLayout_12.addWidget(self.check_log_mcinfo)

        self.check_log_fivekey = QCheckBox(self.groupBox_13)
        self.check_log_fivekey.setObjectName(u"check_log_fivekey")

        self.verticalLayout_12.addWidget(self.check_log_fivekey)

        self.check_log_submaterials = QCheckBox(self.groupBox_13)
        self.check_log_submaterials.setObjectName(u"check_log_submaterials")

        self.verticalLayout_12.addWidget(self.check_log_submaterials)


        self.horizontalLayout_13.addWidget(self.groupBox_13)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.groupBox_10)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_log_selectall = QPushButton(self.frame_5)
        self.btn_log_selectall.setObjectName(u"btn_log_selectall")
        self.btn_log_selectall.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.btn_log_selectall)


        self.verticalLayout_14.addWidget(self.frame_5)


        self.verticalLayout_17.addWidget(self.groupBox_10)

        self.groupBox_14 = QGroupBox(self.frame_15)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(170, 110))
        self.groupBox_14.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 9, 9, 9)
        self.frame_4 = QFrame(self.groupBox_14)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.line_log_fromdate = QLineEdit(self.frame_4)
        self.line_log_fromdate.setObjectName(u"line_log_fromdate")
        self.line_log_fromdate.setMinimumSize(QSize(100, 0))
        self.line_log_fromdate.setMaximumSize(QSize(100, 16777215))
        self.line_log_fromdate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.line_log_fromdate)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)


        self.verticalLayout_27.addWidget(self.frame_4)

        self.frame_43 = QFrame(self.groupBox_14)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.check_log_period = QCheckBox(self.frame_43)
        self.check_log_period.setObjectName(u"check_log_period")

        self.horizontalLayout_48.addWidget(self.check_log_period)


        self.verticalLayout_27.addWidget(self.frame_43)

        self.frame_14 = QFrame(self.groupBox_14)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_14)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_3.addWidget(self.label_28)

        self.line_log_enddate = QLineEdit(self.frame_14)
        self.line_log_enddate.setObjectName(u"line_log_enddate")
        self.line_log_enddate.setMinimumSize(QSize(100, 0))
        self.line_log_enddate.setMaximumSize(QSize(100, 16777215))
        self.line_log_enddate.setAlignment(Qt.AlignCenter)
        self.line_log_enddate.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.line_log_enddate)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.verticalLayout_27.addWidget(self.frame_14)

        self.frame_23 = QFrame(self.groupBox_14)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_log_yesterday = QPushButton(self.frame_23)
        self.btn_log_yesterday.setObjectName(u"btn_log_yesterday")
        self.btn_log_yesterday.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.btn_log_yesterday)

        self.btn_log_today = QPushButton(self.frame_23)
        self.btn_log_today.setObjectName(u"btn_log_today")
        self.btn_log_today.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.btn_log_today)


        self.verticalLayout_27.addWidget(self.frame_23)


        self.verticalLayout_17.addWidget(self.groupBox_14)

        self.groupBox_33 = QGroupBox(self.frame_15)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.verticalLayout_45 = QVBoxLayout(self.groupBox_33)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.check_logdownload_openfolder = QCheckBox(self.groupBox_33)
        self.check_logdownload_openfolder.setObjectName(u"check_logdownload_openfolder")
        self.check_logdownload_openfolder.setChecked(True)

        self.verticalLayout_45.addWidget(self.check_logdownload_openfolder)

        self.btn_logdownload_openfolder = QPushButton(self.groupBox_33)
        self.btn_logdownload_openfolder.setObjectName(u"btn_logdownload_openfolder")
        self.btn_logdownload_openfolder.setMinimumSize(QSize(150, 30))
        self.btn_logdownload_openfolder.setMaximumSize(QSize(150, 30))

        self.verticalLayout_45.addWidget(self.btn_logdownload_openfolder)


        self.verticalLayout_17.addWidget(self.groupBox_33)


        self.horizontalLayout_16.addWidget(self.frame_15)

        self.groupBox_15 = QGroupBox(self.frame_13)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.text_log_lotids = QTextEdit(self.groupBox_15)
        self.text_log_lotids.setObjectName(u"text_log_lotids")

        self.horizontalLayout_18.addWidget(self.text_log_lotids)


        self.horizontalLayout_16.addWidget(self.groupBox_15)


        self.horizontalLayout_7.addWidget(self.frame_13)

        self.groupBox_11 = QGroupBox(self.frame)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 9, 9, -1)
        self.check_log_process1 = QCheckBox(self.groupBox_11)
        self.check_log_process1.setObjectName(u"check_log_process1")

        self.verticalLayout_13.addWidget(self.check_log_process1)

        self.check_log_process2 = QCheckBox(self.groupBox_11)
        self.check_log_process2.setObjectName(u"check_log_process2")

        self.verticalLayout_13.addWidget(self.check_log_process2)

        self.check_log_process3 = QCheckBox(self.groupBox_11)
        self.check_log_process3.setObjectName(u"check_log_process3")

        self.verticalLayout_13.addWidget(self.check_log_process3)

        self.check_log_process4 = QCheckBox(self.groupBox_11)
        self.check_log_process4.setObjectName(u"check_log_process4")

        self.verticalLayout_13.addWidget(self.check_log_process4)

        self.check_log_process5 = QCheckBox(self.groupBox_11)
        self.check_log_process5.setObjectName(u"check_log_process5")

        self.verticalLayout_13.addWidget(self.check_log_process5)

        self.check_log_process6 = QCheckBox(self.groupBox_11)
        self.check_log_process6.setObjectName(u"check_log_process6")

        self.verticalLayout_13.addWidget(self.check_log_process6)

        self.check_log_process7 = QCheckBox(self.groupBox_11)
        self.check_log_process7.setObjectName(u"check_log_process7")

        self.verticalLayout_13.addWidget(self.check_log_process7)

        self.check_log_process8 = QCheckBox(self.groupBox_11)
        self.check_log_process8.setObjectName(u"check_log_process8")

        self.verticalLayout_13.addWidget(self.check_log_process8)

        self.check_log_process9 = QCheckBox(self.groupBox_11)
        self.check_log_process9.setObjectName(u"check_log_process9")

        self.verticalLayout_13.addWidget(self.check_log_process9)

        self.check_log_process10 = QCheckBox(self.groupBox_11)
        self.check_log_process10.setObjectName(u"check_log_process10")

        self.verticalLayout_13.addWidget(self.check_log_process10)

        self.check_log_process11 = QCheckBox(self.groupBox_11)
        self.check_log_process11.setObjectName(u"check_log_process11")

        self.verticalLayout_13.addWidget(self.check_log_process11)

        self.btn_log_process_selectall = QPushButton(self.groupBox_11)
        self.btn_log_process_selectall.setObjectName(u"btn_log_process_selectall")
        self.btn_log_process_selectall.setMinimumSize(QSize(0, 30))
        self.btn_log_process_selectall.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_13.addWidget(self.btn_log_process_selectall)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.btn_log_download_run = QPushButton(self.groupBox_11)
        self.btn_log_download_run.setObjectName(u"btn_log_download_run")
        self.btn_log_download_run.setMinimumSize(QSize(0, 50))
        self.btn_log_download_run.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_13.addWidget(self.btn_log_download_run)


        self.horizontalLayout_7.addWidget(self.groupBox_11)


        self.verticalLayout_25.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_logdownload)
        self.page_csvmerge = QWidget()
        self.page_csvmerge.setObjectName(u"page_csvmerge")
        self.verticalLayout_7 = QVBoxLayout(self.page_csvmerge)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.page_csvmerge)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 20))
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.label_6)

        self.groupBox_16 = QGroupBox(self.page_csvmerge)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMinimumSize(QSize(0, 0))
        self.groupBox_16.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_2 = QLabel(self.groupBox_16)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_20.addWidget(self.label_2)

        self.text_merge_paths = QTextEdit(self.groupBox_16)
        self.text_merge_paths.setObjectName(u"text_merge_paths")

        self.horizontalLayout_20.addWidget(self.text_merge_paths)

        self.btn_merge_paths_read = QPushButton(self.groupBox_16)
        self.btn_merge_paths_read.setObjectName(u"btn_merge_paths_read")
        self.btn_merge_paths_read.setMinimumSize(QSize(60, 60))
        self.btn_merge_paths_read.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_20.addWidget(self.btn_merge_paths_read)

        self.line_5 = QFrame(self.groupBox_16)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_5)

        self.groupBox_20 = QGroupBox(self.groupBox_16)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.horizontalLayout_23 = QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_4 = QLabel(self.groupBox_20)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_23.addWidget(self.label_4)

        self.combo_merge_extensions = QComboBox(self.groupBox_20)
        self.combo_merge_extensions.addItem("")
        self.combo_merge_extensions.addItem("")
        self.combo_merge_extensions.addItem("")
        self.combo_merge_extensions.setObjectName(u"combo_merge_extensions")
        self.combo_merge_extensions.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_23.addWidget(self.combo_merge_extensions)


        self.horizontalLayout_20.addWidget(self.groupBox_20)


        self.verticalLayout_7.addWidget(self.groupBox_16)

        self.groupBox_18 = QGroupBox(self.page_csvmerge)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.horizontalLayout_25 = QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_18 = QFrame(self.groupBox_18)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_24.addWidget(self.label_3)

        self.line_merge_savefilename = QLineEdit(self.frame_18)
        self.line_merge_savefilename.setObjectName(u"line_merge_savefilename")
        self.line_merge_savefilename.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.line_merge_savefilename)


        self.horizontalLayout_25.addWidget(self.frame_18)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_7)

        self.line_4 = QFrame(self.groupBox_18)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_4)

        self.frame_19 = QFrame(self.groupBox_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.radio_merge_savepath_default = QRadioButton(self.frame_19)
        self.radio_merge_savepath_default.setObjectName(u"radio_merge_savepath_default")
        self.radio_merge_savepath_default.setChecked(True)

        self.horizontalLayout_22.addWidget(self.radio_merge_savepath_default)

        self.radio_merge_savepath_input = QRadioButton(self.frame_19)
        self.radio_merge_savepath_input.setObjectName(u"radio_merge_savepath_input")

        self.horizontalLayout_22.addWidget(self.radio_merge_savepath_input)

        self.line_merge_savepath = QLineEdit(self.frame_19)
        self.line_merge_savepath.setObjectName(u"line_merge_savepath")

        self.horizontalLayout_22.addWidget(self.line_merge_savepath)


        self.horizontalLayout_25.addWidget(self.frame_19)


        self.verticalLayout_7.addWidget(self.groupBox_18)

        self.groupBox_17 = QGroupBox(self.page_csvmerge)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_21 = QFrame(self.groupBox_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_2)

        self.label_merge_fileqty = QLabel(self.frame_21)
        self.label_merge_fileqty.setObjectName(u"label_merge_fileqty")

        self.horizontalLayout_21.addWidget(self.label_merge_fileqty)


        self.verticalLayout_21.addWidget(self.frame_21)

        self.frame_17 = QFrame(self.groupBox_17)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.list_merge_filelist = QListWidget(self.frame_17)
        self.list_merge_filelist.setObjectName(u"list_merge_filelist")
        self.list_merge_filelist.setDragEnabled(True)
        self.list_merge_filelist.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_merge_filelist.setSelectionRectVisible(True)

        self.horizontalLayout_26.addWidget(self.list_merge_filelist)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_20)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_merge_list_delete = QPushButton(self.frame_20)
        self.btn_merge_list_delete.setObjectName(u"btn_merge_list_delete")
        self.btn_merge_list_delete.setMinimumSize(QSize(0, 40))
        self.btn_merge_list_delete.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_19.addWidget(self.btn_merge_list_delete)

        self.btn_merge_list_clear = QPushButton(self.frame_20)
        self.btn_merge_list_clear.setObjectName(u"btn_merge_list_clear")
        self.btn_merge_list_clear.setMinimumSize(QSize(0, 40))
        self.btn_merge_list_clear.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_19.addWidget(self.btn_merge_list_clear)

        self.line_6 = QFrame(self.frame_20)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_6)

        self.btn_merge_run = QPushButton(self.frame_20)
        self.btn_merge_run.setObjectName(u"btn_merge_run")
        self.btn_merge_run.setMinimumSize(QSize(0, 40))

        self.verticalLayout_19.addWidget(self.btn_merge_run)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_3)


        self.horizontalLayout_26.addWidget(self.frame_20)


        self.verticalLayout_21.addWidget(self.frame_17)


        self.verticalLayout_7.addWidget(self.groupBox_17)

        self.stackedWidget.addWidget(self.page_csvmerge)
        self.page_ommmerge = QWidget()
        self.page_ommmerge.setObjectName(u"page_ommmerge")
        self.verticalLayout_28 = QVBoxLayout(self.page_ommmerge)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_11 = QLabel(self.page_ommmerge)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 20))
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_28.addWidget(self.label_11)

        self.frame_16 = QFrame(self.page_ommmerge)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_16)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.groupBox_22 = QGroupBox(self.frame_16)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_25 = QFrame(self.groupBox_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.frame_25)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_17.addWidget(self.label_12)

        self.line_omm_path = QLineEdit(self.frame_25)
        self.line_omm_path.setObjectName(u"line_omm_path")

        self.horizontalLayout_17.addWidget(self.line_omm_path)

        self.btn_omm_load = QPushButton(self.frame_25)
        self.btn_omm_load.setObjectName(u"btn_omm_load")

        self.horizontalLayout_17.addWidget(self.btn_omm_load)


        self.verticalLayout_30.addWidget(self.frame_25)

        self.frame_27 = QFrame(self.groupBox_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_13 = QLabel(self.frame_27)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_19.addWidget(self.label_13)

        self.line_omm_savefilename = QLineEdit(self.frame_27)
        self.line_omm_savefilename.setObjectName(u"line_omm_savefilename")
        self.line_omm_savefilename.setMinimumSize(QSize(150, 0))
        self.line_omm_savefilename.setMaximumSize(QSize(150, 11111111))

        self.horizontalLayout_19.addWidget(self.line_omm_savefilename)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_5)

        self.check_omm_openfolder = QCheckBox(self.frame_27)
        self.check_omm_openfolder.setObjectName(u"check_omm_openfolder")
        self.check_omm_openfolder.setChecked(True)

        self.horizontalLayout_19.addWidget(self.check_omm_openfolder)


        self.verticalLayout_30.addWidget(self.frame_27)


        self.verticalLayout_31.addWidget(self.groupBox_22)

        self.groupBox_21 = QGroupBox(self.frame_16)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_omm_fileinfo = QLabel(self.groupBox_21)
        self.label_omm_fileinfo.setObjectName(u"label_omm_fileinfo")
        self.label_omm_fileinfo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.label_omm_fileinfo)

        self.list_omm_filelist = QListWidget(self.groupBox_21)
        self.list_omm_filelist.setObjectName(u"list_omm_filelist")

        self.verticalLayout_29.addWidget(self.list_omm_filelist)

        self.btn_omm_run = QPushButton(self.groupBox_21)
        self.btn_omm_run.setObjectName(u"btn_omm_run")
        self.btn_omm_run.setMinimumSize(QSize(0, 30))

        self.verticalLayout_29.addWidget(self.btn_omm_run)


        self.verticalLayout_31.addWidget(self.groupBox_21)


        self.verticalLayout_28.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.page_ommmerge)
        self.page_automouse = QWidget()
        self.page_automouse.setObjectName(u"page_automouse")
        self.verticalLayout_46 = QVBoxLayout(self.page_automouse)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_29 = QLabel(self.page_automouse)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 20))
        self.label_29.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_46.addWidget(self.label_29)

        self.frame_44 = QFrame(self.page_automouse)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_44)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_49)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.groupBox_34 = QGroupBox(self.frame_49)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setMinimumSize(QSize(0, 50))
        self.groupBox_34.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_50 = QHBoxLayout(self.groupBox_34)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_43 = QLabel(self.groupBox_34)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_43)

        self.combo_macro_action = QComboBox(self.groupBox_34)
        self.combo_macro_action.addItem("")
        self.combo_macro_action.setObjectName(u"combo_macro_action")
        self.combo_macro_action.setMinimumSize(QSize(0, 0))
        self.combo_macro_action.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_50.addWidget(self.combo_macro_action)

        self.line_18 = QFrame(self.groupBox_34)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_50.addWidget(self.line_18)

        self.label_44 = QLabel(self.groupBox_34)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_44)

        self.combo_macro_action_items = QComboBox(self.groupBox_34)
        self.combo_macro_action_items.addItem("")
        self.combo_macro_action_items.setObjectName(u"combo_macro_action_items")
        self.combo_macro_action_items.setMinimumSize(QSize(150, 0))
        self.combo_macro_action_items.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_50.addWidget(self.combo_macro_action_items)


        self.verticalLayout_47.addWidget(self.groupBox_34)

        self.line_19 = QFrame(self.frame_49)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_19)

        self.groupBox_macro_mouse = QGroupBox(self.frame_49)
        self.groupBox_macro_mouse.setObjectName(u"groupBox_macro_mouse")
        self.groupBox_macro_mouse.setMinimumSize(QSize(0, 0))
        self.groupBox_macro_mouse.setMaximumSize(QSize(16777215, 12))
        self.verticalLayout_50 = QVBoxLayout(self.groupBox_macro_mouse)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.line_17 = QFrame(self.groupBox_macro_mouse)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_50.addWidget(self.line_17)

        self.frame_51 = QFrame(self.groupBox_macro_mouse)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_63.setSpacing(6)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_51)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_63.addWidget(self.label_68)

        self.label_66 = QLabel(self.frame_51)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_63.addWidget(self.label_66)

        self.label_macro_mouse_nowpos_x = QLabel(self.frame_51)
        self.label_macro_mouse_nowpos_x.setObjectName(u"label_macro_mouse_nowpos_x")

        self.horizontalLayout_63.addWidget(self.label_macro_mouse_nowpos_x)

        self.label_71 = QLabel(self.frame_51)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_63.addWidget(self.label_71)

        self.label_69 = QLabel(self.frame_51)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_63.addWidget(self.label_69)

        self.label_macro_mouse_nowpos_y = QLabel(self.frame_51)
        self.label_macro_mouse_nowpos_y.setObjectName(u"label_macro_mouse_nowpos_y")

        self.horizontalLayout_63.addWidget(self.label_macro_mouse_nowpos_y)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_14)


        self.verticalLayout_50.addWidget(self.frame_51)

        self.label_37 = QLabel(self.groupBox_macro_mouse)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_50.addWidget(self.label_37)

        self.frame_46 = QFrame(self.groupBox_macro_mouse)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_31 = QLabel(self.frame_46)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_54.addWidget(self.label_31)

        self.line_macro_mouse_posx = QLineEdit(self.frame_46)
        self.line_macro_mouse_posx.setObjectName(u"line_macro_mouse_posx")

        self.horizontalLayout_54.addWidget(self.line_macro_mouse_posx)

        self.label_32 = QLabel(self.frame_46)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_54.addWidget(self.label_32)

        self.line_macro_mouse_posy = QLineEdit(self.frame_46)
        self.line_macro_mouse_posy.setObjectName(u"line_macro_mouse_posy")

        self.horizontalLayout_54.addWidget(self.line_macro_mouse_posy)


        self.verticalLayout_50.addWidget(self.frame_46)

        self.line_13 = QFrame(self.groupBox_macro_mouse)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_50.addWidget(self.line_13)

        self.label_38 = QLabel(self.groupBox_macro_mouse)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_50.addWidget(self.label_38)

        self.frame_50 = QFrame(self.groupBox_macro_mouse)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_34 = QLabel(self.frame_50)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_55.addWidget(self.label_34)

        self.line_macro_mouse_offset_x = QLineEdit(self.frame_50)
        self.line_macro_mouse_offset_x.setObjectName(u"line_macro_mouse_offset_x")

        self.horizontalLayout_55.addWidget(self.line_macro_mouse_offset_x)

        self.label_33 = QLabel(self.frame_50)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_55.addWidget(self.label_33)

        self.line_macro_mouse_offset_y = QLineEdit(self.frame_50)
        self.line_macro_mouse_offset_y.setObjectName(u"line_macro_mouse_offset_y")

        self.horizontalLayout_55.addWidget(self.line_macro_mouse_offset_y)


        self.verticalLayout_50.addWidget(self.frame_50)

        self.line_14 = QFrame(self.groupBox_macro_mouse)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_50.addWidget(self.line_14)

        self.label_39 = QLabel(self.groupBox_macro_mouse)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_50.addWidget(self.label_39)

        self.frame_48 = QFrame(self.groupBox_macro_mouse)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_36 = QLabel(self.frame_48)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_56.addWidget(self.label_36)

        self.line_macro_mouse_posx2 = QLineEdit(self.frame_48)
        self.line_macro_mouse_posx2.setObjectName(u"line_macro_mouse_posx2")

        self.horizontalLayout_56.addWidget(self.line_macro_mouse_posx2)

        self.label_35 = QLabel(self.frame_48)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_56.addWidget(self.label_35)

        self.line_macro_mouse_posy2 = QLineEdit(self.frame_48)
        self.line_macro_mouse_posy2.setObjectName(u"line_macro_mouse_posy2")

        self.horizontalLayout_56.addWidget(self.line_macro_mouse_posy2)


        self.verticalLayout_50.addWidget(self.frame_48)

        self.line_16 = QFrame(self.groupBox_macro_mouse)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_50.addWidget(self.line_16)

        self.label_40 = QLabel(self.groupBox_macro_mouse)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_50.addWidget(self.label_40)

        self.label_41 = QLabel(self.groupBox_macro_mouse)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_50.addWidget(self.label_41)

        self.label_42 = QLabel(self.groupBox_macro_mouse)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_50.addWidget(self.label_42)


        self.verticalLayout_47.addWidget(self.groupBox_macro_mouse)

        self.groupBox_macro_keyboard = QGroupBox(self.frame_49)
        self.groupBox_macro_keyboard.setObjectName(u"groupBox_macro_keyboard")
        self.groupBox_macro_keyboard.setMinimumSize(QSize(0, 350))
        self.groupBox_macro_keyboard.setMaximumSize(QSize(16777215, 350))
        self.verticalLayout_52 = QVBoxLayout(self.groupBox_macro_keyboard)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_45 = QLabel(self.groupBox_macro_keyboard)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_52.addWidget(self.label_45)

        self.frame_55 = QFrame(self.groupBox_macro_keyboard)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.groupBox_55 = QGroupBox(self.frame_55)
        self.groupBox_55.setObjectName(u"groupBox_55")
        self.horizontalLayout_74 = QHBoxLayout(self.groupBox_55)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.line_macro_keyboard_keys = QLineEdit(self.groupBox_55)
        self.line_macro_keyboard_keys.setObjectName(u"line_macro_keyboard_keys")
        self.line_macro_keyboard_keys.setMaximumSize(QSize(16777215, 19))

        self.horizontalLayout_74.addWidget(self.line_macro_keyboard_keys)


        self.horizontalLayout_73.addWidget(self.groupBox_55)

        self.groupBox_56 = QGroupBox(self.frame_55)
        self.groupBox_56.setObjectName(u"groupBox_56")
        self.groupBox_56.setMinimumSize(QSize(60, 0))
        self.groupBox_56.setMaximumSize(QSize(60, 16777215))
        self.horizontalLayout_75 = QHBoxLayout(self.groupBox_56)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.line_macro_keyboard_key = QLineEdit(self.groupBox_56)
        self.line_macro_keyboard_key.setObjectName(u"line_macro_keyboard_key")
        self.line_macro_keyboard_key.setMinimumSize(QSize(40, 0))
        self.line_macro_keyboard_key.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_75.addWidget(self.line_macro_keyboard_key)


        self.horizontalLayout_73.addWidget(self.groupBox_56)


        self.verticalLayout_52.addWidget(self.frame_55)

        self.line_21 = QFrame(self.groupBox_macro_keyboard)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_21)

        self.label_46 = QLabel(self.groupBox_macro_keyboard)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_52.addWidget(self.label_46)

        self.frame_54 = QFrame(self.groupBox_macro_keyboard)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.groupBox_57 = QGroupBox(self.frame_54)
        self.groupBox_57.setObjectName(u"groupBox_57")
        self.verticalLayout_55 = QVBoxLayout(self.groupBox_57)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(4, 4, 4, 4)
        self.list_macro_keyboard_category = QListWidget(self.groupBox_57)
        self.list_macro_keyboard_category.setObjectName(u"list_macro_keyboard_category")

        self.verticalLayout_55.addWidget(self.list_macro_keyboard_category)


        self.horizontalLayout_72.addWidget(self.groupBox_57)

        self.groupBox_58 = QGroupBox(self.frame_54)
        self.groupBox_58.setObjectName(u"groupBox_58")
        self.verticalLayout_57 = QVBoxLayout(self.groupBox_58)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(4, 4, 4, 4)
        self.list_macro_keyboard_commands = QListWidget(self.groupBox_58)
        self.list_macro_keyboard_commands.setObjectName(u"list_macro_keyboard_commands")

        self.verticalLayout_57.addWidget(self.list_macro_keyboard_commands)


        self.horizontalLayout_72.addWidget(self.groupBox_58)


        self.verticalLayout_52.addWidget(self.frame_54)

        self.label_macro_keyboard_description = QLabel(self.groupBox_macro_keyboard)
        self.label_macro_keyboard_description.setObjectName(u"label_macro_keyboard_description")
        self.label_macro_keyboard_description.setMinimumSize(QSize(0, 80))
        self.label_macro_keyboard_description.setMaximumSize(QSize(16777215, 80))
        self.label_macro_keyboard_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_52.addWidget(self.label_macro_keyboard_description)


        self.verticalLayout_47.addWidget(self.groupBox_macro_keyboard)

        self.groupBox_macro_imagesearch = QGroupBox(self.frame_49)
        self.groupBox_macro_imagesearch.setObjectName(u"groupBox_macro_imagesearch")
        self.groupBox_macro_imagesearch.setMinimumSize(QSize(0, 0))
        self.groupBox_macro_imagesearch.setMaximumSize(QSize(16777215, 12))
        self.verticalLayout_53 = QVBoxLayout(self.groupBox_macro_imagesearch)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.groupBox_47 = QGroupBox(self.groupBox_macro_imagesearch)
        self.groupBox_47.setObjectName(u"groupBox_47")
        self.horizontalLayout_57 = QHBoxLayout(self.groupBox_47)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_55 = QLabel(self.groupBox_47)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_57.addWidget(self.label_55)

        self.line_macro_imagesearch_path = QLineEdit(self.groupBox_47)
        self.line_macro_imagesearch_path.setObjectName(u"line_macro_imagesearch_path")

        self.horizontalLayout_57.addWidget(self.line_macro_imagesearch_path)

        self.btn_macro_imagesearch_test = QPushButton(self.groupBox_47)
        self.btn_macro_imagesearch_test.setObjectName(u"btn_macro_imagesearch_test")

        self.horizontalLayout_57.addWidget(self.btn_macro_imagesearch_test)


        self.verticalLayout_53.addWidget(self.groupBox_47)

        self.groupBox_48 = QGroupBox(self.groupBox_macro_imagesearch)
        self.groupBox_48.setObjectName(u"groupBox_48")
        self.horizontalLayout_59 = QHBoxLayout(self.groupBox_48)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.line_macro_imagesearch_confidence = QLineEdit(self.groupBox_48)
        self.line_macro_imagesearch_confidence.setObjectName(u"line_macro_imagesearch_confidence")
        self.line_macro_imagesearch_confidence.setMinimumSize(QSize(50, 0))
        self.line_macro_imagesearch_confidence.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_59.addWidget(self.line_macro_imagesearch_confidence)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_11)


        self.verticalLayout_53.addWidget(self.groupBox_48)

        self.groupBox_49 = QGroupBox(self.groupBox_macro_imagesearch)
        self.groupBox_49.setObjectName(u"groupBox_49")
        self.horizontalLayout_58 = QHBoxLayout(self.groupBox_49)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.check_macro_imagesearch_variable = QCheckBox(self.groupBox_49)
        self.check_macro_imagesearch_variable.setObjectName(u"check_macro_imagesearch_variable")

        self.horizontalLayout_58.addWidget(self.check_macro_imagesearch_variable)

        self.line_macro_imagesearch_variable = QLineEdit(self.groupBox_49)
        self.line_macro_imagesearch_variable.setObjectName(u"line_macro_imagesearch_variable")

        self.horizontalLayout_58.addWidget(self.line_macro_imagesearch_variable)


        self.verticalLayout_53.addWidget(self.groupBox_49)

        self.label_65 = QLabel(self.groupBox_macro_imagesearch)
        self.label_65.setObjectName(u"label_65")

        self.verticalLayout_53.addWidget(self.label_65)

        self.label_64 = QLabel(self.groupBox_macro_imagesearch)
        self.label_64.setObjectName(u"label_64")

        self.verticalLayout_53.addWidget(self.label_64)

        self.label_61 = QLabel(self.groupBox_macro_imagesearch)
        self.label_61.setObjectName(u"label_61")

        self.verticalLayout_53.addWidget(self.label_61)

        self.label_60 = QLabel(self.groupBox_macro_imagesearch)
        self.label_60.setObjectName(u"label_60")

        self.verticalLayout_53.addWidget(self.label_60)

        self.label_59 = QLabel(self.groupBox_macro_imagesearch)
        self.label_59.setObjectName(u"label_59")

        self.verticalLayout_53.addWidget(self.label_59)

        self.label_58 = QLabel(self.groupBox_macro_imagesearch)
        self.label_58.setObjectName(u"label_58")

        self.verticalLayout_53.addWidget(self.label_58)

        self.label_57 = QLabel(self.groupBox_macro_imagesearch)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_53.addWidget(self.label_57)

        self.label_56 = QLabel(self.groupBox_macro_imagesearch)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(0, 0))
        self.label_56.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_53.addWidget(self.label_56)


        self.verticalLayout_47.addWidget(self.groupBox_macro_imagesearch)

        self.groupBox_macro_delay = QGroupBox(self.frame_49)
        self.groupBox_macro_delay.setObjectName(u"groupBox_macro_delay")
        self.groupBox_macro_delay.setMinimumSize(QSize(0, 0))
        self.groupBox_macro_delay.setMaximumSize(QSize(16777215, 12))
        self.verticalLayout_48 = QVBoxLayout(self.groupBox_macro_delay)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_47 = QFrame(self.groupBox_macro_delay)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_62 = QLabel(self.frame_47)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_61.addWidget(self.label_62)

        self.line_macro_delay = QLineEdit(self.frame_47)
        self.line_macro_delay.setObjectName(u"line_macro_delay")
        self.line_macro_delay.setMinimumSize(QSize(150, 0))
        self.line_macro_delay.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_61.addWidget(self.line_macro_delay)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_13)


        self.verticalLayout_48.addWidget(self.frame_47)

        self.label_63 = QLabel(self.groupBox_macro_delay)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_48.addWidget(self.label_63)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_10)


        self.verticalLayout_47.addWidget(self.groupBox_macro_delay)

        self.groupBox_macro_plugin = QGroupBox(self.frame_49)
        self.groupBox_macro_plugin.setObjectName(u"groupBox_macro_plugin")
        self.groupBox_macro_plugin.setMinimumSize(QSize(0, 0))
        self.groupBox_macro_plugin.setMaximumSize(QSize(16777215, 12))
        self.verticalLayout_54 = QVBoxLayout(self.groupBox_macro_plugin)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_53 = QFrame(self.groupBox_macro_plugin)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.groupBox_38 = QGroupBox(self.frame_53)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.horizontalLayout_53 = QHBoxLayout(self.groupBox_38)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_70 = QLabel(self.groupBox_38)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_53.addWidget(self.label_70)

        self.lineEdit = QLineEdit(self.groupBox_38)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_53.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.groupBox_38)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_53.addWidget(self.pushButton)


        self.horizontalLayout_65.addWidget(self.groupBox_38)


        self.verticalLayout_54.addWidget(self.frame_53)

        self.groupBox_42 = QGroupBox(self.groupBox_macro_plugin)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.horizontalLayout_66 = QHBoxLayout(self.groupBox_42)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.tabWidget = QTabWidget(self.groupBox_42)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_56 = QVBoxLayout(self.tab)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.groupBox_43 = QGroupBox(self.tab)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.horizontalLayout_68 = QHBoxLayout(self.groupBox_43)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.lineEdit_2 = QLineEdit(self.groupBox_43)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_68.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.groupBox_43)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_68.addWidget(self.pushButton_2)


        self.verticalLayout_56.addWidget(self.groupBox_43)

        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_56.addWidget(self.listWidget)

        self.groupBox_44 = QGroupBox(self.tab)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.horizontalLayout_67 = QHBoxLayout(self.groupBox_44)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_72 = QLabel(self.groupBox_44)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_67.addWidget(self.label_72)

        self.lineEdit_4 = QLineEdit(self.groupBox_44)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_67.addWidget(self.lineEdit_4)

        self.label_73 = QLabel(self.groupBox_44)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_67.addWidget(self.label_73)

        self.lineEdit_5 = QLineEdit(self.groupBox_44)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_67.addWidget(self.lineEdit_5)

        self.line_24 = QFrame(self.groupBox_44)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.VLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_67.addWidget(self.line_24)

        self.label_75 = QLabel(self.groupBox_44)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_67.addWidget(self.label_75)

        self.lineEdit_7 = QLineEdit(self.groupBox_44)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_67.addWidget(self.lineEdit_7)

        self.label_74 = QLabel(self.groupBox_44)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_67.addWidget(self.label_74)

        self.lineEdit_6 = QLineEdit(self.groupBox_44)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_67.addWidget(self.lineEdit_6)


        self.verticalLayout_56.addWidget(self.groupBox_44)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_12)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_52 = QGroupBox(self.tab_2)
        self.groupBox_52.setObjectName(u"groupBox_52")
        self.groupBox_52.setGeometry(QRect(9, 9, 234, 55))
        self.horizontalLayout_70 = QHBoxLayout(self.groupBox_52)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.lineEdit_3 = QLineEdit(self.groupBox_52)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_70.addWidget(self.lineEdit_3)

        self.pushButton_3 = QPushButton(self.groupBox_52)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_70.addWidget(self.pushButton_3)

        self.groupBox_53 = QGroupBox(self.tab_2)
        self.groupBox_53.setObjectName(u"groupBox_53")
        self.groupBox_53.setGeometry(QRect(10, 70, 234, 55))
        self.horizontalLayout_71 = QHBoxLayout(self.groupBox_53)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.lineEdit_12 = QLineEdit(self.groupBox_53)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_71.addWidget(self.lineEdit_12)

        self.pushButton_4 = QPushButton(self.groupBox_53)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_71.addWidget(self.pushButton_4)

        self.groupBox_51 = QGroupBox(self.tab_2)
        self.groupBox_51.setObjectName(u"groupBox_51")
        self.groupBox_51.setGeometry(QRect(20, 130, 221, 61))
        self.label_76 = QLabel(self.groupBox_51)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(10, 30, 54, 12))
        self.lineEdit_8 = QLineEdit(self.groupBox_51)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(70, 30, 51, 20))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.groupBox_54 = QGroupBox(self.tab_3)
        self.groupBox_54.setObjectName(u"groupBox_54")
        self.groupBox_54.setGeometry(QRect(10, 10, 347, 55))
        self.horizontalLayout_69 = QHBoxLayout(self.groupBox_54)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.lineEdit_9 = QLineEdit(self.groupBox_54)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_69.addWidget(self.lineEdit_9)

        self.pushButton_5 = QPushButton(self.groupBox_54)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_69.addWidget(self.pushButton_5)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout_66.addWidget(self.tabWidget)


        self.verticalLayout_54.addWidget(self.groupBox_42)


        self.verticalLayout_47.addWidget(self.groupBox_macro_plugin)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_47.addItem(self.verticalSpacer_5)

        self.groupBox_45 = QGroupBox(self.frame_49)
        self.groupBox_45.setObjectName(u"groupBox_45")
        self.groupBox_45.setMinimumSize(QSize(0, 50))
        self.groupBox_45.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_60 = QHBoxLayout(self.groupBox_45)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(-1, 0, -1, 0)
        self.line_macro_command = QLineEdit(self.groupBox_45)
        self.line_macro_command.setObjectName(u"line_macro_command")

        self.horizontalLayout_60.addWidget(self.line_macro_command)

        self.btn_macro_command_edit = QPushButton(self.groupBox_45)
        self.btn_macro_command_edit.setObjectName(u"btn_macro_command_edit")
        self.btn_macro_command_edit.setMinimumSize(QSize(50, 30))
        self.btn_macro_command_edit.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_60.addWidget(self.btn_macro_command_edit)

        self.btn_macro_command_insert = QPushButton(self.groupBox_45)
        self.btn_macro_command_insert.setObjectName(u"btn_macro_command_insert")
        self.btn_macro_command_insert.setMinimumSize(QSize(50, 30))
        self.btn_macro_command_insert.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_60.addWidget(self.btn_macro_command_insert)


        self.verticalLayout_47.addWidget(self.groupBox_45)


        self.horizontalLayout_52.addWidget(self.frame_49)

        self.line_22 = QFrame(self.frame_44)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.VLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_52.addWidget(self.line_22)

        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_45)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_40 = QGroupBox(self.frame_45)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.horizontalLayout_51 = QHBoxLayout(self.groupBox_40)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.groupBox_41 = QGroupBox(self.groupBox_40)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.line_macro_forcestop = QLineEdit(self.groupBox_41)
        self.line_macro_forcestop.setObjectName(u"line_macro_forcestop")
        self.line_macro_forcestop.setGeometry(QRect(10, 20, 41, 20))

        self.horizontalLayout_51.addWidget(self.groupBox_41)

        self.groupBox_39 = QGroupBox(self.groupBox_40)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.horizontalLayout_49 = QHBoxLayout(self.groupBox_39)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_30 = QLabel(self.groupBox_39)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_49.addWidget(self.label_30)

        self.line_macro_repeat = QLineEdit(self.groupBox_39)
        self.line_macro_repeat.setObjectName(u"line_macro_repeat")
        self.line_macro_repeat.setMinimumSize(QSize(50, 0))
        self.line_macro_repeat.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_49.addWidget(self.line_macro_repeat)


        self.horizontalLayout_51.addWidget(self.groupBox_39)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_12)

        self.btn_macro_run = QPushButton(self.groupBox_40)
        self.btn_macro_run.setObjectName(u"btn_macro_run")
        self.btn_macro_run.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_51.addWidget(self.btn_macro_run)


        self.verticalLayout_49.addWidget(self.groupBox_40)

        self.groupBox_50 = QGroupBox(self.frame_45)
        self.groupBox_50.setObjectName(u"groupBox_50")
        self.horizontalLayout_62 = QHBoxLayout(self.groupBox_50)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.combo_macro_reciepe_load = QComboBox(self.groupBox_50)
        self.combo_macro_reciepe_load.setObjectName(u"combo_macro_reciepe_load")
        self.combo_macro_reciepe_load.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_62.addWidget(self.combo_macro_reciepe_load)

        self.btn_macro_reciepe_load = QPushButton(self.groupBox_50)
        self.btn_macro_reciepe_load.setObjectName(u"btn_macro_reciepe_load")

        self.horizontalLayout_62.addWidget(self.btn_macro_reciepe_load)

        self.line_23 = QFrame(self.groupBox_50)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.VLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_62.addWidget(self.line_23)

        self.label_67 = QLabel(self.groupBox_50)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_62.addWidget(self.label_67)

        self.line_macro_reciepe_name = QLineEdit(self.groupBox_50)
        self.line_macro_reciepe_name.setObjectName(u"line_macro_reciepe_name")
        self.line_macro_reciepe_name.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_62.addWidget(self.line_macro_reciepe_name)

        self.btn_macro_reciepe_save = QPushButton(self.groupBox_50)
        self.btn_macro_reciepe_save.setObjectName(u"btn_macro_reciepe_save")

        self.horizontalLayout_62.addWidget(self.btn_macro_reciepe_save)


        self.verticalLayout_49.addWidget(self.groupBox_50)

        self.groupBox_46 = QGroupBox(self.frame_45)
        self.groupBox_46.setObjectName(u"groupBox_46")
        self.horizontalLayout_64 = QHBoxLayout(self.groupBox_46)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(-1, 9, -1, 6)
        self.frame_52 = QFrame(self.groupBox_46)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(65, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_52)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.btn_macro_list_up = QPushButton(self.frame_52)
        self.btn_macro_list_up.setObjectName(u"btn_macro_list_up")
        self.btn_macro_list_up.setMinimumSize(QSize(0, 30))

        self.verticalLayout_51.addWidget(self.btn_macro_list_up)

        self.btn_macro_list_down = QPushButton(self.frame_52)
        self.btn_macro_list_down.setObjectName(u"btn_macro_list_down")
        self.btn_macro_list_down.setMinimumSize(QSize(0, 30))

        self.verticalLayout_51.addWidget(self.btn_macro_list_down)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacer_11)

        self.btn_macro_list_clear = QPushButton(self.frame_52)
        self.btn_macro_list_clear.setObjectName(u"btn_macro_list_clear")
        self.btn_macro_list_clear.setMinimumSize(QSize(0, 30))

        self.verticalLayout_51.addWidget(self.btn_macro_list_clear)

        self.btn_macro_list_copy = QPushButton(self.frame_52)
        self.btn_macro_list_copy.setObjectName(u"btn_macro_list_copy")
        self.btn_macro_list_copy.setMinimumSize(QSize(0, 30))

        self.verticalLayout_51.addWidget(self.btn_macro_list_copy)

        self.btn_macro_list_delete = QPushButton(self.frame_52)
        self.btn_macro_list_delete.setObjectName(u"btn_macro_list_delete")
        self.btn_macro_list_delete.setMinimumSize(QSize(0, 30))

        self.verticalLayout_51.addWidget(self.btn_macro_list_delete)


        self.horizontalLayout_64.addWidget(self.frame_52)

        self.list_macros = QListWidget(self.groupBox_46)
        self.list_macros.setObjectName(u"list_macros")

        self.horizontalLayout_64.addWidget(self.list_macros)


        self.verticalLayout_49.addWidget(self.groupBox_46)


        self.horizontalLayout_52.addWidget(self.frame_45)


        self.verticalLayout_46.addWidget(self.frame_44)

        self.stackedWidget.addWidget(self.page_automouse)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_24 = QVBoxLayout(self.page_setting)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_10 = QLabel(self.page_setting)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 20))
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_24.addWidget(self.label_10)

        self.groupBox_19 = QGroupBox(self.page_setting)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_22 = QFrame(self.groupBox_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 50))
        self.frame_22.setMaximumSize(QSize(16777215, 50))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_5 = QLabel(self.frame_22)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(250, 0))
        self.label_5.setMaximumSize(QSize(250, 16777215))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.label_5)

        self.bnt_settings_openjson = QPushButton(self.frame_22)
        self.bnt_settings_openjson.setObjectName(u"bnt_settings_openjson")
        self.bnt_settings_openjson.setMinimumSize(QSize(0, 0))
        self.bnt_settings_openjson.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_27.addWidget(self.bnt_settings_openjson)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_3)


        self.verticalLayout_22.addWidget(self.frame_22)

        self.line_7 = QFrame(self.groupBox_19)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_7)

        self.frame_38 = QFrame(self.groupBox_19)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 50))
        self.frame_38.setMaximumSize(QSize(16777215, 50))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_27 = QLabel(self.frame_38)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(250, 0))
        self.label_27.setMaximumSize(QSize(250, 16777215))
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_27)

        self.radio_setting_lightmode = QRadioButton(self.frame_38)
        self.radio_setting_lightmode.setObjectName(u"radio_setting_lightmode")

        self.horizontalLayout_41.addWidget(self.radio_setting_lightmode)

        self.radio_setting_drakmode = QRadioButton(self.frame_38)
        self.radio_setting_drakmode.setObjectName(u"radio_setting_drakmode")
        self.radio_setting_drakmode.setChecked(True)

        self.horizontalLayout_41.addWidget(self.radio_setting_drakmode)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_4)


        self.verticalLayout_22.addWidget(self.frame_38)

        self.line_15 = QFrame(self.groupBox_19)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_15)


        self.verticalLayout_24.addWidget(self.groupBox_19)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_setting)

        self.verticalLayout_23.addWidget(self.stackedWidget)

        self.list_RunningMessage = QListWidget(self.frame_main)
        self.list_RunningMessage.setObjectName(u"list_RunningMessage")
        self.list_RunningMessage.setMinimumSize(QSize(0, 100))
        self.list_RunningMessage.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_23.addWidget(self.list_RunningMessage)


        self.horizontalLayout_28.addWidget(self.frame_main)


        self.verticalLayout_3.addWidget(self.frame_24)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.check_ngimage_mes, self.check_ngimage_las)
        QWidget.setTabOrder(self.check_ngimage_las, self.check_ngimage_excel)
        QWidget.setTabOrder(self.check_ngimage_excel, self.line_ngimage_datefrom)
        QWidget.setTabOrder(self.line_ngimage_datefrom, self.line_ngimage_dateto)
        QWidget.setTabOrder(self.line_ngimage_dateto, self.btn_ngimage_selectall)
        QWidget.setTabOrder(self.btn_ngimage_selectall, self.btn_ngimage_run)
        QWidget.setTabOrder(self.btn_ngimage_run, self.check_mes_outlook)
        QWidget.setTabOrder(self.check_mes_outlook, self.check_mes_mes)
        QWidget.setTabOrder(self.check_mes_mes, self.check_mes_las)
        QWidget.setTabOrder(self.check_mes_las, self.check_mes_excel)
        QWidget.setTabOrder(self.check_mes_excel, self.line_mes_datefrom)
        QWidget.setTabOrder(self.line_mes_datefrom, self.line_mes_dateto)
        QWidget.setTabOrder(self.line_mes_dateto, self.btn_mes_selectall)
        QWidget.setTabOrder(self.btn_mes_selectall, self.btn_mes_run)
        QWidget.setTabOrder(self.btn_mes_run, self.check_log_process1)
        QWidget.setTabOrder(self.check_log_process1, self.check_log_process2)
        QWidget.setTabOrder(self.check_log_process2, self.check_log_process3)
        QWidget.setTabOrder(self.check_log_process3, self.check_log_process4)
        QWidget.setTabOrder(self.check_log_process4, self.check_log_process5)
        QWidget.setTabOrder(self.check_log_process5, self.check_log_process6)
        QWidget.setTabOrder(self.check_log_process6, self.check_log_process7)
        QWidget.setTabOrder(self.check_log_process7, self.check_log_process8)
        QWidget.setTabOrder(self.check_log_process8, self.check_log_process9)
        QWidget.setTabOrder(self.check_log_process9, self.check_log_process10)
        QWidget.setTabOrder(self.check_log_process10, self.check_log_process11)
        QWidget.setTabOrder(self.check_log_process11, self.btn_log_process_selectall)
        QWidget.setTabOrder(self.btn_log_process_selectall, self.text_merge_paths)
        QWidget.setTabOrder(self.text_merge_paths, self.btn_merge_paths_read)
        QWidget.setTabOrder(self.btn_merge_paths_read, self.line_merge_savefilename)
        QWidget.setTabOrder(self.line_merge_savefilename, self.radio_merge_savepath_default)
        QWidget.setTabOrder(self.radio_merge_savepath_default, self.combo_merge_extensions)
        QWidget.setTabOrder(self.combo_merge_extensions, self.list_RunningMessage)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Topbar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">\ub9e4\ud06c\ub85c</span></p></body></html>", None))
        self.btn_version.setText(QCoreApplication.translate("MainWindow", u"\ubc84\uc804", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.btn_page_imagecrop.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc790\ub974\uae30", None))
        self.btn_page_imageinsert.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc0bd\uc785", None))
        self.btn_page_csvmerge.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \ud569\uce58\uae30", None))
        self.btn_page_omm.setText(QCoreApplication.translate("MainWindow", u"OMM \ud569\uce58\uae30", None))
        self.btn_page_oismenu.setText(QCoreApplication.translate("MainWindow", u"OIS Assy \uc804\uc6a9", None))
        self.btn_page_automouse.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c", None))
        self.btn_page_settings.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc2a4\ud15c \uc124\uc815", None))
        self.btn_page_exit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        self.btn_page_avi_avigraph.setText(QCoreApplication.translate("MainWindow", u"4\uc2dc\uac04 \uadf8\ub798\ud504", None))
        self.btn_page_ngreport.setText(QCoreApplication.translate("MainWindow", u"NG Report", None))
        self.btn_page_mes.setText(QCoreApplication.translate("MainWindow", u"MES \ub204\ub77d\ucc3e\uae30", None))
        self.btn_page_logdownload.setText(QCoreApplication.translate("MainWindow", u"Log Downlaod", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">\uc774\ubbf8\uc9c0 \uc790\ub974\uae30</span></p></body></html>", None))
        self.label_imagecrop_image.setText("")
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uacbd\ub85c", None))
        self.btn_imagecrop_path.setText(QCoreApplication.translate("MainWindow", u"\uc9c1\uc811\uc801\uc6a9", None))
        self.label_imagecrop_fileinfo.setText("")
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"\uc88c\ud45c", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"\uc88c\ud45c1 (\uc88c\ud074\ub9ad)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"\uc88c\ud45c2 (\uc6b0\ud074\ub9ad)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", u"\ub808\uc2dc\ud53c", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"\ucd94\uac00(\uc218\uc815) / \uc0ad\uc81c", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\ub808\uc2dc\ud53c\uc774\ub984", None))
        self.btn_imagecrop_reciepe_add.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00/\uc218\uc815", None))
        self.btn_imagecrop_reciepe_delete.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0\uc800\uc7a5 \uc124\uc815", None))
        self.radio_imagecrop_save_result.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5\uacbd\ub85c : \uc774\ubbf8\uc9c0\uac00 \uc788\ub294 \ud3f4\ub354 \ub0b4 Result \ud3f4\ub354", None))
        self.radio_imagecrop_save_desktop.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5\uacbd\ub85c : \ubc14\ud0d5\ud654\uba74(\uc774\ubbf8\uc9c0 \uc6a9\ub7c9 \ud074 \ub54c)", None))
        self.btn_imagecrop_preview.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\ub9ac\ubcf4\uae30", None))
        self.btn_imagecrop_run.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc800\uc7a5 \ud558\uae30", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">\uc774\ubbf8\uc9c0 \uc0bd\uc785</span></p></body></html>", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140 \ud30c\uc77c \uc124\uc815", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140 \ud30c\uc77c \uacbd\ub85c", None))
        self.btn_imageinsert_load.setText(QCoreApplication.translate("MainWindow", u"\uc801\uc6a9", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140 \ud30c\uc77c \uc2dc\ud2b8\uba85", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc0bd\uc785 \uc140 \uc8fc\uc18c", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc0bd\uc785 \ubc29\ud5a5", None))
        self.radio_imageinsert_dir_right.setText(QCoreApplication.translate("MainWindow", u"\uc6b0\uce21 \ubc29\ud5a5", None))
        self.radio_imageinsert_dir_down.setText(QCoreApplication.translate("MainWindow", u"\uc544\ub798 \ubc29\ud5a5", None))
        self.radio_imageinsert_dir_complex.setText(QCoreApplication.translate("MainWindow", u"\uc6b0\uce21 n\uce78 \uc0bd\uc785 \ud6c4 \uc544\ub798 \ubc29\ud5a5", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"n : ", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("MainWindow", u"\ucd94\uac00\uae30\ub2a5", None))
        self.check_imageinsert_insertfilename.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc0bd\uc785 \uc2dc \uc774\ubbf8\uc9c0 \ud30c\uc77c \uba85 \uc785\ub825", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ub123\uae30 \uc635\uc158", None))
        self.radio_imageinsert_fit_height.setText(QCoreApplication.translate("MainWindow", u"\uc140 \ub192\uc774\uc5d0 \ub9de\ucda4", None))
        self.radio_imageinsert_fit_width.setText(QCoreApplication.translate("MainWindow", u"\uc140 \ub108\ube44\uc5d0 \ub9de\ucda4", None))
        self.radio_imageinsert_set_height.setText(QCoreApplication.translate("MainWindow", u"\uc140 \ub192\uc774 \uc9c0\uc815", None))
        self.radio_imageinsert_set_width.setText(QCoreApplication.translate("MainWindow", u"\uc140 \ub108\ube44 \uc9c0\uc815", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ud30c\uc77c \uc124\uc815", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ud30c\uc77c \uacbd\ub85c", None))
        self.btn_imageinsert_imagepath_load.setText(QCoreApplication.translate("MainWindow", u"\uc801\uc6a9", None))
        self.btn_imageinsert_imagepath_add.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00", None))
        self.btn_imageinsert_imagepath_clear.setText(QCoreApplication.translate("MainWindow", u"\ub9ac\uc14b", None))
        self.btn_imageinsert_run.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589", None))
        self.label_imageinsert_imagepath_load_result.setText("")
        self.label_imageinsert_image.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">NG Report</span></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589 (NG Image Report \uc0dd\uc131)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\uc2dc\ud000\uc2a4 \uc120\ud0dd", None))
        self.check_ngimage_mes.setText(QCoreApplication.translate("MainWindow", u"1. \ubd88\ub7c9\ub370\uc774\ud130\uc870\ud68c(MES)", None))
        self.check_ngimage_las.setText(QCoreApplication.translate("MainWindow", u"2. \ubd88\ub7c9\uc774\ubbf8\uc9c0\ub2e4\uc6b4(LAS)", None))
        self.check_ngimage_excel.setText(QCoreApplication.translate("MainWindow", u"3. \ub9ac\ud3ec\ud2b8\uc0dd\uc131(EXCEL)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\uc77c(yyyy-mm-dd)", None))
        self.line_ngimage_datefrom.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc\uc77c(yyyy-mm-dd)", None))
        self.btn_ngimage_selectall.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4\uc120\ud0dd/\ud574\uc81c", None))
        self.btn_ngimage_run.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">MES \ub204\ub77d \ucc3e\uae30</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589 (MES \ub204\ub77d \ucc3e\uae30)", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\uc2dc\ud000\uc2a4 \uc120\ud0dd", None))
        self.check_mes_outlook.setText(QCoreApplication.translate("MainWindow", u"1. Outlook", None))
        self.check_mes_mes.setText(QCoreApplication.translate("MainWindow", u"2. MES", None))
        self.check_mes_las.setText(QCoreApplication.translate("MainWindow", u"3. LAS", None))
        self.check_mes_excel.setText(QCoreApplication.translate("MainWindow", u"4. \ub370\uc774\ud130 \uc885\ud569", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\uc77c(yyyy-mm-dd)", None))
        self.line_mes_datefrom.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc\uc77c(yyyy-mm-dd)", None))
        self.btn_mes_selectall.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4\uc120\ud0dd/\ud574\uc81c", None))
        self.btn_mes_run.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Log Download</span></p></body></html>", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\ube44 \ud638\uae30", None))
        self.check_log_mc1.setText(QCoreApplication.translate("MainWindow", u"MC#1", None))
        self.check_log_mc2.setText(QCoreApplication.translate("MainWindow", u"MC#2", None))
        self.check_log_mc3.setText(QCoreApplication.translate("MainWindow", u"MC#3", None))
        self.check_log_mc4.setText(QCoreApplication.translate("MainWindow", u"MC#4", None))
        self.check_log_mc5.setText(QCoreApplication.translate("MainWindow", u"MC#5", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_log_mc_selectall.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4\uc120\ud0dd/\ud574\uc81c", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8 \uc120\ud0dd", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\ub0a0\uc9dc \ub2e8\uc704", None))
        self.check_log_secsgem.setText(QCoreApplication.translate("MainWindow", u"SECSGEM", None))
        self.check_log_sequence.setText(QCoreApplication.translate("MainWindow", u"Sequence", None))
        self.check_log_mmi.setText(QCoreApplication.translate("MainWindow", u"MMI Log", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\ub0a0\uc9dc+LotID \ub2e8\uc704", None))
        self.check_log_mcinfo.setText(QCoreApplication.translate("MainWindow", u"MachineInfo", None))
        self.check_log_fivekey.setText(QCoreApplication.translate("MainWindow", u"FiveKey Log", None))
        self.check_log_submaterials.setText(QCoreApplication.translate("MainWindow", u"Submaterial", None))
        self.btn_log_selectall.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4\uc120\ud0dd/\ud574\uc81c", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\ub0a0\uc9dc\uc120\ud0dd(yyyy-mm-dd)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\ub0a0\uc9dc", None))
        self.line_log_fromdate.setText(QCoreApplication.translate("MainWindow", u"2024-04-29", None))
        self.check_log_period.setText(QCoreApplication.translate("MainWindow", u"\uae30\uac04", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc\ub0a0\uc9dc", None))
        self.btn_log_yesterday.setText(QCoreApplication.translate("MainWindow", u"\uc5b4\uc81c", None))
        self.btn_log_today.setText(QCoreApplication.translate("MainWindow", u"\uc624\ub298", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5\ud3f4\ub354", None))
        self.check_logdownload_openfolder.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc \ud6c4 \uc800\uc7a5\ud3f4\ub354 \uc790\ub3d9 \uc5f4\uae30", None))
        self.btn_logdownload_openfolder.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \ud3f4\ub354 \uc5f4\uae30", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Lot ID List (\ubd99\uc5ec\ub123\uae30, \ud55c \uc904\uc529 \uad6c\ubd84)", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\ube44 \uacf5\uc815 \uc120\ud0dd", None))
        self.check_log_process1.setText(QCoreApplication.translate("MainWindow", u"Handler (SECSGEM)", None))
        self.check_log_process2.setText(QCoreApplication.translate("MainWindow", u"Grease Disp#1", None))
        self.check_log_process3.setText(QCoreApplication.translate("MainWindow", u"Ball Attach #1", None))
        self.check_log_process4.setText(QCoreApplication.translate("MainWindow", u"X Stage Attach", None))
        self.check_log_process5.setText(QCoreApplication.translate("MainWindow", u"Grease Disp#2", None))
        self.check_log_process6.setText(QCoreApplication.translate("MainWindow", u"Ball Attach #2", None))
        self.check_log_process7.setText(QCoreApplication.translate("MainWindow", u"Y Stage Attach", None))
        self.check_log_process8.setText(QCoreApplication.translate("MainWindow", u"Z-Stopper Attach", None))
        self.check_log_process9.setText(QCoreApplication.translate("MainWindow", u"Epoxy Disp#1", None))
        self.check_log_process10.setText(QCoreApplication.translate("MainWindow", u"Epoxy Disp#2", None))
        self.check_log_process11.setText(QCoreApplication.translate("MainWindow", u"UV Inspection", None))
        self.btn_log_process_selectall.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4\uc120\ud0dd/\ud574\uc81c", None))
        self.btn_log_download_run.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc \uc2e4\ud589", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">CSV Merge</span></p></body></html>", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"\ud569\uce60 \ud30c\uc77c\ub4e4\uc774 \uc788\ub294 \uacbd\ub85c(\uc5ec\ub7ec \uacbd\ub85c \uc785\ub825 \uac00\ub2a5, \uc904\ubc14\uafc8\uc73c\ub85c \uad6c\ubd84)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uacbd\ub85c", None))
        self.btn_merge_paths_read.setText(QCoreApplication.translate("MainWindow", u"\uc5f4\uae30", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"\ud655\uc7a5\uc790 \ud544\ud130\ub9c1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc7a5\uc790", None))
        self.combo_merge_extensions.setItemText(0, QCoreApplication.translate("MainWindow", u".csv", None))
        self.combo_merge_extensions.setItemText(1, QCoreApplication.translate("MainWindow", u".txt", None))
        self.combo_merge_extensions.setItemText(2, QCoreApplication.translate("MainWindow", u".log", None))

        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \uc124\uc815", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uba85(\uc800\uc7a5)", None))
        self.line_merge_savefilename.setText(QCoreApplication.translate("MainWindow", u"merge.csv", None))
        self.radio_merge_savepath_default.setText(QCoreApplication.translate("MainWindow", u"\uae30\ubcf8 \uacbd\ub85c(\uc785\ub825 \uacbd\ub85c \ub0b4)", None))
        self.radio_merge_savepath_input.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc815 \uacbd\ub85c(\uc785\ub825)", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc628 \ud30c\uc77c \ubaa9\ub85d", None))
        self.label_merge_fileqty.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc218 : / \ud30c\uc77c \ud06c\uae30 : ", None))
        self.btn_merge_list_delete.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\uc81c\uac70", None))
        self.btn_merge_list_clear.setText(QCoreApplication.translate("MainWindow", u"\ubaa9\ub85d\ucd08\uae30\ud654", None))
        self.btn_merge_run.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uc2e4\ud589", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">OMM Merge</span></p></body></html>", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354\uacbd\ub85c", None))
        self.btn_omm_load.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5\ud30c\uc77c\uba85", None))
        self.line_omm_savefilename.setText(QCoreApplication.translate("MainWindow", u"merge.csv", None))
        self.check_omm_openfolder.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc \ud6c4 \ud3f4\ub354 \uc5f4\uae30", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc628 \ud30c\uc77c\ubaa9\ub85d", None))
        self.label_omm_fileinfo.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc218 : / \ud30c\uc77c \ud06c\uae30 :", None))
        self.btn_omm_run.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Macro \ub9cc\ub4e4\uae30</span></p></body></html>", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"\uba85\ub839\uc5b4 \ubd84\ub958", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\uba85\ub839\uc5b4 \ubd84\ub9581", None))
        self.combo_macro_action.setItemText(0, QCoreApplication.translate("MainWindow", u"-\uc120\ud0dd-", None))

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\uba85\ub839\uc5b4 \ubd84\ub9582", None))
        self.combo_macro_action_items.setItemText(0, QCoreApplication.translate("MainWindow", u"-\uc120\ud0dd-", None))

        self.groupBox_macro_mouse.setTitle(QCoreApplication.translate("MainWindow", u"\u25b6 \ub9c8\uc6b0\uc2a4", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"[\ud604\uc7ac \ub9c8\uc6b0\uc2a4 \uc88c\ud45c]", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_macro_mouse_nowpos_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_71.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_macro_mouse_nowpos_y.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u203b \uae30\ubcf8 \uc88c\ud45c \uc785\ub825", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"X \uc88c\ud45c", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Y \uc88c\ud45c", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u203b \uae30\ubcf8 \uc88c\ud45c\uc758 \ubcf4\uc815 \uac12 \u2192 \uc774\ubbf8\uc9c0\uc11c\uce58 \ud6c4 \ubcf4\uc815\ud558\ub294 \ub370 \uc0ac\uc6a9(\uae30\ubcf8 \uac12 : 0)", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"X Offset", None))
        self.line_macro_mouse_offset_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Y Offset", None))
        self.line_macro_mouse_offset_y.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u203b \ub4dc\ub798\uadf8 \ubaa8\ub4dc \uc2dc \ubaa9\ud45c \uc9c0\uc810 \uc88c\ud45c", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"X \uc88c\ud45c2", None))
        self.line_macro_mouse_posx2.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Y \uc88c\ud45c2", None))
        self.line_macro_mouse_posy2.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u2605\uc774\ubbf8\uc9c0 \uc11c\uce58 \uacb0\uacfc \uc88c\ud45c\uac12\uc744 \uc785\ub825\ud558\ub824\uba74 <span style=\" text-decoration: underline;\">%\ubcc0\uc218\uba85</span> \uc744 \uc785\ub825\ud558\uba74 \ub41c\ub2e4.</p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc2dc) \uc774\ubbf8\uc9c0 \uc11c\uce58 \ubcc0\uc218\uba85(x,y) = ok_button_x, ok_button_y", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"          \uc77c \ub54c, X \uc88c\ud45c (%ok_button_x)    Y \uc88c\ud45c (%ok_button_y)", None))
        self.groupBox_macro_keyboard.setTitle(QCoreApplication.translate("MainWindow", u"\u25b6 \ud0a4\ubcf4\ub4dc", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\uae30\ubcf8 : \ubb38\uc7a5, \uba85\ub839\uc5b4 \uc785\ub825 \uac00\ub2a5 / \ub2e8\uc77c\ud0a4 : \ud558\ub098\uc758 \ud0a4\ub9cc \uc785\ub825 \uac00\ub2a5", None))
        self.groupBox_55.setTitle(QCoreApplication.translate("MainWindow", u"\ud0a4\uc785\ub825", None))
        self.groupBox_56.setTitle(QCoreApplication.translate("MainWindow", u"\ub2e8\uc77c\ud0a4", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd", None))
        self.groupBox_57.setTitle(QCoreApplication.translate("MainWindow", u"\u25bc \uba85\ub839\uc5b4 \ubd84\ub958", None))
        self.groupBox_58.setTitle(QCoreApplication.translate("MainWindow", u"\u25bc \uba85\ub839\uc5b4", None))
        self.label_macro_keyboard_description.setText("")
        self.groupBox_macro_imagesearch.setTitle(QCoreApplication.translate("MainWindow", u"\u25b6 \uc774\ubbf8\uc9c0\uc11c\uce58", None))
        self.groupBox_47.setTitle(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0\ud30c\uc77c", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uba85", None))
        self.btn_macro_imagesearch_test.setText(QCoreApplication.translate("MainWindow", u"\ud14c\uc2a4\ud2b8", None))
        self.groupBox_48.setTitle(QCoreApplication.translate("MainWindow", u"\uc815\ud655\ub3c4(\uae30\ubcf8\uac12 0.9)", None))
        self.line_macro_imagesearch_confidence.setText(QCoreApplication.translate("MainWindow", u"0.9", None))
        self.groupBox_49.setTitle(QCoreApplication.translate("MainWindow", u"\uc11c\uce58 \uacb0\uacfc", None))
        self.check_macro_imagesearch_variable.setText(QCoreApplication.translate("MainWindow", u"\ubcc0\uc218\uba85\uc73c\ub85c \uc800\uc7a5", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"1. \ud654\uba74 \ub0b4\uc5d0\uc11c \uc774\ubbf8\uc9c0 \ud30c\uc77c\uc744 \ucc3e\ub294\ub2e4.", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"2. \uacb0\uacfc\uac12\uc740 x\uc88c\ud45c, y\uc88c\ud45c\ub85c \ucd9c\ub825\ub41c\ub2e4.", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"3. \ubcc0\uc218\uba85\uc73c\ub85c \uc800\uc7a5\ud558\uba74 \ud574\ub2f9 \uc88c\ud45c\uba85\uc5d0 x\uc88c\ud45c, y\uc88c\ud45c\uac00 \uc800\uc7a5\ub41c\ub2e4.", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"4. \ubcc0\uc218\uba85\uc73c\ub85c \uc800\uc7a5\ud55c x\uc88c\ud45c y\uc88c\ud45c\ub97c \ub9c8\uc6b0\uc2a4 \ud0ed\uc5d0\uc11c \uc785\ub825\uac12\uc73c\ub85c \uc0ac\uc6a9\uac00\ub2a5", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc2dc) \uac80\uc0c9\ubc84\ud2bc.png \ud30c\uc77c\uc744 \uac80\uc0c9\ubc84\ud2bc \uc774\ub77c\ub294 \ubcc0\uc218\uba85\uc73c\ub85c \uc800\uc7a5,", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"        \uac80\uc0c9\ubc84\ud2bc.png\uc640 90%\uc77c\uce58\ud558\ub294 \uc7a5\uba74\uc744 \ub0b4 \ud654\uba74 \ub0b4\uc5d0\uc11c \ucc3e\uc558\uc744 \uacbd\uc6b0", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"        \uac80\uc0c9\ubc84\ud2bc_x, \uac80\uc0c9\ubc84\ud2bc_y\ub77c\ub294 \ubcc0\uc218\ub85c \uc800\uc7a5\ub428", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"  \ub9c8\uc6b0\uc2a4-\ud074\ub9ad \uc88c\ud45c X : %\uac80\uc0c9\ubc84\ud2bc_x    \uc88c\ud45c Y : %\uac80\uc0c9\ubc84\ud2bc_y", None))
        self.groupBox_macro_delay.setTitle(QCoreApplication.translate("MainWindow", u"\u25b6 \ub300\uae30", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\ub300\uae30(ms)", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"1000ms = 1s", None))
        self.groupBox_macro_plugin.setTitle(QCoreApplication.translate("MainWindow", u"\u25b6 \ucd94\uac00\uae30\ub2a5", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uc2e4\ud589\ud558\uae30", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8\uba85", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ud14c\uc2a4\ud2b8\uc2e4\ud589", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c \uae30\ub2a5 \uc0ac\uc6a9\ud558\uae30 (\uac1c\ubc1c \uc911)", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uacbd\ub85c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("MainWindow", u"\uc790\ub974\uae30 \uc88c\ud45c", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"X1", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Y1", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"X2", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Y2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc790\ub974\uae30", None))
        self.groupBox_52.setTitle(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ud30c\uc77c \uacbd\ub85c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.groupBox_53.setTitle(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140 \ud30c\uc77c \uacbd\ub85c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.groupBox_51.setTitle(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc0bd\uc785 \uc140 \uc8fc\uc18c \ubc0f \ubc29\ud5a5", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\uc140\uc8fc\uc18c", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc0bd\uc785", None))
        self.groupBox_54.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uacbd\ub85c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \ud569\uce58\uae30", None))
        self.groupBox_45.setTitle(QCoreApplication.translate("MainWindow", u"\uba85\ub839\uc5b4 (1) \uba85\ub839\uc5b4 \uc9c1\uc811 \uc218\uc815 \uac00\ub2a5 (2) \uba54\ubaa8,\uc8fc\uc11d(\"#\") : #\ub0b4\uc6a9\ud14d\uc2a4\ud2b8 )", None))
        self.btn_macro_command_edit.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.btn_macro_command_insert.setText(QCoreApplication.translate("MainWindow", u"\uc0bd\uc785", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791 \uc124\uc815", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("MainWindow", u"\uac15\uc81c\uc885\ub8cc", None))
        self.line_macro_forcestop.setText(QCoreApplication.translate("MainWindow", u"F12", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("MainWindow", u"\ubc18\ubcf5 \ud69f\uc218", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\ubc18\ubcf5(\ubb34\ud55c=0)", None))
        self.line_macro_repeat.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_macro_run.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c \uc2dc\uc791", None))
        self.groupBox_50.setTitle(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c \ubd88\ub7ec\uc624\uae30 \ub0b4\ubcf4\ub0b4\uae30", None))
        self.btn_macro_reciepe_load.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uba85", None))
        self.btn_macro_reciepe_save.setText(QCoreApplication.translate("MainWindow", u"\ub0b4\ubcf4\ub0b4\uae30", None))
        self.groupBox_46.setTitle(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c", None))
        self.btn_macro_list_up.setText(QCoreApplication.translate("MainWindow", u"\uc704\ub85c", None))
        self.btn_macro_list_down.setText(QCoreApplication.translate("MainWindow", u"\uc544\ub798\ub85c", None))
        self.btn_macro_list_clear.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.btn_macro_list_copy.setText(QCoreApplication.translate("MainWindow", u"\ubcf5\uc0ac", None))
        self.btn_macro_list_delete.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">\uc2dc\uc2a4\ud15c \uc124\uc815</span></p></body></html>", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"UI \uc124\uc815", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc2a4\ud15c \uc2dc\uc791 \uc2dc UI \uc124\uc815", None))
        self.bnt_settings_openjson.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815\ud30c\uc77c\uc5f4\uae30", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc2a4\ud15c \ud14c\ub9c8", None))
        self.radio_setting_lightmode.setText(QCoreApplication.translate("MainWindow", u"\ub77c\uc774\ud2b8 \ubaa8\ub4dc", None))
        self.radio_setting_drakmode.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\ud06c \ubaa8\ub4dc", None))
    # retranslateUi

