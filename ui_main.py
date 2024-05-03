from _library.functions.func_nowdirectory import get_now_dir
from _library.functions.func_foldermake import FolderExists
from _library.functions.func_json import read_json
from _library.functions.func_userinfo import USER

# MES 누락 Macro 관련 Import
from _library.mesmacro.mesmacro_outlook import Outlook
from _library.mesmacro.mesmacro_check import Process
from _library.mesmacro.mesmacro_MES import MES
from _library.mesmacro.mesmacro_LAS import LAS
from _library.mesmacro.mesmacro_find import EMPTY

# MES 누락 Macro 관련 Import
from _library.ng_image.ngimage import NG_Image
# from _library.ng_image.ngimage_MES import NID_MES
# from _library.ng_image.ngimage_LAS import NID_LAS
# from _library.ng_image.ngimage_Excel_Report import NID_REPORT

# Log 다운로드 관련 Import
from _library.Logfiles.LogfileDownload import LogDownload

# CSV Merge 관련 Import
from _library.functions.func_csvMerge import CSV_Merge

# Image Crop 관련 Import
from _library.ImageCrop.imageCrop import ImageCrop

# Image Insert 관련 Import
from _library.ImageExcelInsert.ImageInsert import ImageInsert

# AVI Graph 관련 Import
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = 933120000

# Macro 관련 Import
from _library.jymacro.macro import AutoMouse


# UI 관련 Import
from _uiFiles import Ui_MainWindow
from _uiFiles import MainWindow_Style
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt, QThread, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import QPen
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient, QImage)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QDialog

import datetime
import os
import time



v='''
Version 2024-05-03
Git Hub 연동 하였음
Commit Test 3 - git pull 명령어 이 후ㅌ
123123
'''
print(v)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.progress_lasimage = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 기본설정 > Version
        version = self.versions()
        # 기본 설정 > 모든 경로 설정
        self.paths()

        self.ui.btn_macro_command_edit.setEnabled(False)
        self.ui_style(self.ui.radio_setting_lightmode.isChecked())
        self.ui_functions()


        self.setWindowTitle(f'이진영 매크로 {version}')
        self.message(f'프로그램이 실행되었습니다. (실행위치 : {self.now_dir})')
        self.logging(self.get_userinfo("System-Start"))
        self.check_license()
        self.message(f'Now Version : {self.version}')
        self.message(f'Lastest Version : {self.latest_version}')
        self.ui_style(self.ui.radio_setting_lightmode.isChecked())
        self.show()


    # 기본 설정 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # 기본 설정 > Version ───────────────────────────────────────────────────────────────────────────────────────────────
    def versions(self, output=False):
        version = ["Ver 24.04.04 프로젝트 생성",
                   "Ver 24.04.05 NG Image, Log Donwload 기능 추가",
                   "Ver 24.04.06 NG Image, Log Download 기능 완료",
                   "Ver 24.04.09 System 설정 저장 및 불러오기 (settings.json)기능 추가",
                   "Ver 24.04.16 OMM Merge 기능 추가",
                   "Ver 24.04.19 Image 관련 기능 추가 (Crop / Insert)"]
        if output:
            for update in version:
                self.ui.list_RunningMessage.addItem(update)
                self.ui.list_RunningMessage.scrollToBottom()
        # self.version = '24.04.06'
        self.version = version[-1][4:12]
        return version[-1][0:12]

    # 기본 설정 > 모든 경로 설정 ───────────────────────────────────────────────────────────────────────────────────────────
    def paths(self):
        self.now_dir = get_now_dir()    # 현재 폴더의 Dir
        self.path_dir_settings= f"{self.now_dir}/Settings"
        self.path_file_settings_json = f"{self.path_dir_settings}/UI_Settings.json"
        self.path_file_keyboard_command_json = f"{self.path_dir_settings}/Keyboard_Command_Settings.json"
        self.path_dir_macroreciepes = f"{self.path_dir_settings}/Reciepes"

        self.path_dir_logdownload = f'{self.now_dir}/Logdownload'

        self.path_dir_macro = 'S:/자화전자주식회사/임원/사장/제조2본부/기술3팀/0.임시/이진영/(★) 매크로파일/매크로 다운로드'
        self.path_dir_license = 'S:/자화전자주식회사/임원/사장/제조2본부/기술3팀/0.임시/이진영/(☆) 자료'
        self.path_file_license = f'{self.path_dir_license}/license.json'

        self.path_imagepath = f'{self.now_dir}/Images/MES LAS/'

    # 기본 설정 > License ───────────────────────────────────────────────────────────────────────────────────────────────
    def get_userinfo(self, active=""):
        dt = datetime.datetime.now()
        dt = dt.strftime("%y/%m/%d %H:%M:%S")
        user = USER()
        user_name = user.user_name()
        user_mac = user.mac()
        user_ip = user.ip()
        user_pc = user.user_pcSerialNo()
        # print(user_name, user_mac, user_ip, user_pc)
        return f'{dt},{user_name},{user_mac},{user_pc},{self.version},{active}'
    def check_license(self):
        license_json = read_json(self.path_file_license)
        # Expire Check ##################################################################
        license_decode = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
                          'Oct': 10, 'Nov': 11, 'Dec': 12}
        expire = license_json['key']
        key_decode = bytes.fromhex(expire).decode('utf-8')
        key_decode = key_decode.replace('K', '0')
        ex_year = int(key_decode[0:4])
        ex_month = int(license_decode[key_decode[-3:]])
        # 2  0  2  5  .  J  a  n
        # 32 4B 32 35 2E 4A 61 6E

        from datetime import datetime
        nowtime = datetime.now()
        now_year = nowtime.year
        now_month = nowtime.month

        # 프로그램 강제종료 : 사용기간 만료
        if now_year >= ex_year:
            if now_month >= ex_month:
                if self.ui_question("사용 기한 만료",
                                    "프로그램 사용기한이 만료됐습니다.\n기존파일을 삭제한 뒤 최신 버전을 다운로드 하십시오.\n다운로드 폴더를 바로 여시겠습니까?"):
                    path = os.path.realpath(self.path_dir_macro)
                    os.startfile(path)
                sys.exit()
        # Version Check ##################################################################
        self.latest_version = license_json['version'][-1]
        all_versions = len(license_json['version']) - 1
        now_version = license_json['version'].index(self.version)
        if all_versions == now_version:
            # 최신 버전
            pass
        if all_versions > now_version:
            update_title = "프로그램 업데이트"
            if all_versions - 2 > now_version:
                sys_exit = True  # 업데이트 필요
                update_message = "구 버전을 사용 중입니다.\n기존파일을 삭제한 뒤 최신 버전을 다운로드 하십시오.\n다운로드 폴더를 바로 여시겠습니까?"
            else:
                sys_exit = False  # 업데이트 권장
                update_message = "최신 버전이 있습니다.\n업데이트를 위해 다운로드 폴더를 바로 여시겠습니까?"
            if self.ui_question(update_title, update_message):
                path = os.path.realpath(self.path_dir_macro)
                os.startfile(path)
                sys_exit = True
            if sys_exit:
                self.close()
                sys.exit()



    # 전체 기능 관련 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # 전체 기능 관련 > Ui Widget Class Name ──────────────────────────────────────────────────────────────────────────────
    def classname(self, widget):
        return widget.__class__.__name__

    # 전체 기능 관련 > Ui Question 띄우기 ─────────────────────────────────────────────────────────────────────────────────
    def ui_question(self, title, message) -> bool:
        import PyQt5
        msg = PyQt5.QtWidgets.QMessageBox
        question = msg.question(self, title, message, msg.Yes | msg.No)
        if question == msg.Yes:
            return True
        else:
            return False

    # 전체 기능 관련 > Log 기록 남기기 ─────────────────────────────────────────────────────────────────────────────────────
    def logging(self, logdata):
        logfile_path = 'S:/자화전자주식회사/임원/사장/제조2본부/기술3팀/0.임시/이진영/(☆) 자료/logging.csv'
        logsave_count = 0
        while True:
            try:
                with open(logfile_path, 'r', encoding='utf-8') as r:
                    print(f'readlines : {r.readlines()}')
                if logdata is None:
                    logdata = self.get_userinfo("None")
                writedata = f'{logdata},savecount={logsave_count}'
                if writedata is not None:
                    writedata = writedata.rstrip()
                    writedata = writedata.lstrip()
                    writedata += '\n'
                    print(writedata)
                    with open(logfile_path, 'a', encoding='utf-8') as a:
                        a.seek(0)
                        a.write(writedata)
                    return
            except:
                pass
            time.sleep(0.5)
            logsave_count += 1
            if logsave_count >= 5:
                return

    # 전체 기능 관련 > 파일 용량 구하기 ─────────────────────────────────────────────────────────────────────────────────────
    def get_filesize(self, size):
        if size >= 1000000000:
            return f'{round(size / 1000000000, 2)}GB'
        elif size >= 1000000:
            return f'{round(size / 1000000, 2)}MB'
        elif size >= 1000:
            return f'{round(size / 1000, 2)}KB'
        else:
            return f'{size}Byte'

    # 전체 기능 관련 > 날짜 데이터 출력 ─────────────────────────────────────────────────────────────────────────────────────
    def setting_date(self):
        self.y = 0
        self.m = 0
        self.d = 0
        self.period = 0
        while True:
            try:
                from_date = input("검색 시작 날짜를 입력해주세요.(yyyy-mm-dd) : ")
                y = from_date.split("-")[0]
                m = from_date.split("-")[1]
                d = from_date.split("-")[2]
                if len(y) != 4 or len(m) != 2 or len(d) != 2 or int(m) > 12 or int(d) > 31:
                    print("지정된 날짜 형식에 맞게 다시 입력해주세요.")
                else:
                    self.y = int(y)
                    self.m = int(m)
                    self.d = int(d)
                    break
            except:
                print("지정된 형식에 맞게 다시 입력해주세요.")
        while True:
            period = input("검색 시작 날짜로부터 몇 일간의 데이터를 검색할 지 입력해주세요(n) : ")
            try:
                self.period = int(period)
                break
            except:
                print("지정된 형식에 맞게 다시 입력해주세요.")

        self.date_from = datetime.datetime(self.y, self.m, self.d)
        self.date_end = self.date_from+datetime.timedelta(days=self.period)
        date_from = self.date_from.strftime('%Y%m%d')
        date_end = self.date_end.strftime('%Y%m%d')

        if date_from == date_end:
            self.filename = f'{date_from}_'
        else:
            self.filename = f'{date_from}_{date_end}_'



    # UI 설정 관련 분류 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # UI 설정 관련 분류 > UI Thema 관련 ───────────────────────────────────────────────────────────────────────────────────
    def ui_style(self, ui_view):
        lightmode = ui_view
        if lightmode:
            themes = 'light'
        else:
            themes = 'dark'

        colors = self.ui_colors(themes)

        style = {'QWidget': {'background-color': colors['bg2'],
                             'color': colors['text']},
                 'QFrame': {'background-color': colors['bg2']},
                 'QLabel': {'color': colors['text']},
                 'QPushButton': {'background-color': colors['bg3'],
                                 'padding': '3px',
                                 'border-radius': '5px',
                                 'border-color': colors['border'],
                                 'color': colors['text']
                                 },
                 'QPushButton:hover': {'background-color': colors['bg1'],
                                       'border': f"1px solid {colors['bg1']}",
                                       'color': colors['text']
                                       },
                 'QPushButton:disabled': {'color': colors['bg4']},
                 'QLineEdit:enabled': {
                     'background-color': colors['bg4'],
                     'color': colors['text']},
                 'QLineEdit:!enabled': {
                     'background-color': colors['bg3'],
                     'color': colors['text']}
                 }
        self.ui_stylesheet(self.ui.stackedWidget, style)

        # centralwidget
        style = {'QWidget':{'background':colors['bg1'],
                            'color':colors['text']},
                 'QFrame':{'background':colors['bg1']},
                 'QPushButton':{'background-color':colors['bg2'],
                                'padding': '3px',
                                'border': f"1px solid {colors['bg2']}",
                                'border-radius': '10px',
                                'color': colors['text']
                                },
                 'QPushButton:hover': {'background-color': colors['bg3'],
                                       'border': f"1px solid {colors['bg3']}",
                                       'color': colors['text']
                                       },

                 'QLabel':{'color': colors['text']},
                 'QGroupBox': {'border': f"1px solid {colors['border']}",
                               'padding':f'9px 0px 0px 0px',

                               'background-color': colors['bg2'],
                               'color': colors['text']}
        }
        self.ui_stylesheet(self,style)
    def ui_colors(self, thema='light'):
        self.rgb_white = 'rgb(255, 255, 255)'
        self.rgb_black = 'rgb(0, 0, 0)'

        if thema == 'dark':
            return {'text':'rgb(187, 187, 187)',
                    'border':'rgb(89, 91, 93)',
                    'bg1':'rgb(60, 63, 65)',
                    'bg2':'rgb(43, 43, 43)',
                    'bg3':'rgb(89, 91, 93)',
                    'bg4':self.rgb_black}
        elif thema == 'light':
            return {'text': self.rgb_black,
                    'border': 'rgb(166, 164, 162)',
                    'bg1': 'rgb(195, 192, 195)',
                    'bg2': 'rgb(212, 212, 212)',
                    'bg3': 'rgb(166, 164, 162)',
                    'bg4': self.rgb_white}
    def ui_stylesheet(self, ui, stylelist):
        css = ""
        for style in stylelist:
            # Widget 지정 일 경우
            if style[0] == 'Q':
                css += style + "{"
                for option in stylelist[style]:
                    css += f'{option}: {stylelist[style][option]};\n'
                css += '}\n'
                #print(f'CSS : {css}')
            else:
                # 전체 설정일 경우
                for option in stylelist:
                    css += f'{option}: {stylelist[option]};\n'
        ui.setStyleSheet(css)
    def ui_style_description(self):
        print('''
        background: 요소의 배경색을 설정합니다.
        background-color: 요소의 배경색을 설정합니다.
        border: 요소의 테두리를 설정합니다.
        border-radius: 요소의 테두리의 둥글기를 설정합니다.
        border-color: 요소의 테두리 색상을 설정합니다.
        border-style: 요소의 테두리 스타일을 설정합니다.
        border-width: 요소의 테두리 두께를 설정합니다.
        color: 요소의 텍스트 색상을 설정합니다.
        font: 요소의 글꼴 속성을 설정합니다.
        font-family: 요소의 글꼴 패밀리를 설정합니다.
        font-size: 요소의 글꼴 크기를 설정합니다.
        font-weight: 요소의 글꼴 두께를 설정합니다.
        font-style: 요소의 글꼴 스타일을 설정합니다.
        padding: 요소의 안쪽 여백을 설정합니다.
        margin: 요소의 바깥 여백을 설정합니다.
        text-align: 텍스트의 정렬을 설정합니다.
        text-decoration: 텍스트의 장식을 설정합니다.
        text-transform: 텍스트의 대소문자 변환을 설정합니다.
        text-shadow: 텍스트에 그림자 효과를 설정합니다.
        opacity: 요소의 투명도를 설정합니다.
        visibility: 요소의 가시성을 설정합니다.
        display: 요소의 표시 방법을 설정합니다.
        width: 요소의 너비를 설정합니다.
        height: 요소의 높이를 설정합니다.
        max-width: 요소의 최대 너비를 설정합니다.
        max-height: 요소의 최대 높이를 설정합니다.
        min-width: 요소의 최소 너비를 설정합니다.
        min-height: 요소의 최소 높이를 설정합니다.
        icon: QPushButton에 표시되는 아이콘의 스타일을 설정합니다.
        padding-left, padding-right, padding-top, padding-bottom: 요소의 안쪽 여백을 좌, 우, 상, 하 각각 설정합니다.
        margin-left, margin-right, margin-top, margin-bottom: 요소의 바깥 여백을 좌, 우, 상, 하 각각 설정합니다.
        ''')

    # UI 설정 관련 분류 > UI Function 관련 > Ui 설정 불러오기 ───────────────────────────────────────────────────────────────
    def ui_setting(self, jsonfile):
        ui_category = {'UI_NgImage':[   self.ui.check_ngimage_mes, self.ui.check_ngimage_las, self.ui.check_ngimage_excel],
                       'UI_MesData':[   self.ui.check_mes_outlook, self.ui.check_mes_mes, self.ui.check_mes_las, self.ui.check_mes_excel],
                       'UI_LogDownload':[self.ui.check_log_mc1,self.ui.check_log_mc2,self.ui.check_log_mc3,self.ui.check_log_mc4,self.ui.check_log_mc5,self.ui.check_log_secsgem,self.ui.check_log_sequence,self.ui.check_log_mmi,self.ui.check_log_mcinfo,self.ui.check_log_fivekey,self.ui.check_log_submaterials,self.ui.check_log_process1,self.ui.check_log_process2,self.ui.check_log_process3,self.ui.check_log_process4,self.ui.check_log_process5,self.ui.check_log_process6,self.ui.check_log_process7,self.ui.check_log_process8,self.ui.check_log_process9,self.ui.check_log_process10,self.ui.check_log_process11],
                       'UI_CsvMerge':[self.ui.combo_merge_extensions, self.ui.line_merge_savefilename]}
        for category in jsonfile:
            ui_data = jsonfile[category]
            count = 0
            for ui_name in ui_data:
                data = ui_data[ui_name]
                ui = ui_category[category][count]
                ui_type = ui_name.split("_")[0]
                if ui_type == "checkbox":
                    ui.setChecked(data)
                elif ui_type == "text":
                    ui.setText(data)
                elif ui_type == "combobox":
                    ui.setCurrentText(data)
                count += 1

    # UI 설정 관련 분류 > UI Function 관련 > UI Page Change────────────────────────────────────────────────────────────────
    def ui_functions_pagechange(self):
        # self.ui.frame_oismenu.setMaximumSize(QSize(0, 0))
        self.now_width = self.ui.frame_main.width()
        self.ui.frame_oismenu.setFixedWidth(0)
        self.ui.btn_page_ngreport.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ngreport))
        self.ui.btn_page_mes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_mes))
        self.ui.btn_page_logdownload.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_logdownload))
        self.ui.btn_page_csvmerge.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_csvmerge))
        self.ui.btn_page_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting))
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting))
        self.ui.btn_page_omm.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ommmerge))
        self.ui.btn_page_oismenu.clicked.connect(lambda: self.ui_functions_sidemenu(self.ui.frame_oismenu))
        self.ui.btn_page_imagecrop.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_imagecrop))
        self.ui.btn_page_imageinsert.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_imageinsert))
        self.ui.btn_page_automouse.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_automouse))

    # UI 설정 관련 분류 > UI Function 관련 > 각 모듈의 Functions─────────────────────────────────────────────────────────────
    def ui_functions_logdownload(self):
        #Log Download  #################################################################################################

        self.check_log_mc_list = [self.ui.check_log_mc1, self.ui.check_log_mc2, self.ui.check_log_mc3,
                                  self.ui.check_log_mc4, self.ui.check_log_mc5]
        self.check_log_loglist = [self.ui.check_log_secsgem, self.ui.check_log_sequence, self.ui.check_log_mmi,
                                  self.ui.check_log_mcinfo, self.ui.check_log_fivekey, self.ui.check_log_submaterials]
        self.check_log_process_list = [self.ui.check_log_process1, self.ui.check_log_process2,
                                       self.ui.check_log_process3, self.ui.check_log_process4,
                                       self.ui.check_log_process5, self.ui.check_log_process6,
                                       self.ui.check_log_process7, self.ui.check_log_process8,
                                       self.ui.check_log_process9, self.ui.check_log_process10,
                                       self.ui.check_log_process11]

        self.ui.btn_log_mc_selectall.clicked.connect(lambda: self.ui_functions_log_checkbox_selectall("mc"))
        self.ui.btn_log_selectall.clicked.connect(lambda: self.ui_functions_log_checkbox_selectall("log"))
        self.ui.btn_log_process_selectall.clicked.connect(lambda: self.ui_functions_log_checkbox_selectall("process"))
        self.ui.btn_log_yesterday.clicked.connect(lambda: self.ui.line_log_fromdate.setText(self.yesterday.strftime("%Y-%m-%d")))
        self.ui.btn_log_today.clicked.connect(lambda: self.ui.line_log_fromdate.setText(self.today.strftime("%Y-%m-%d")))
        self.ui.check_log_period.clicked.connect(lambda: self.ui.line_log_enddate.setEnabled(self.ui.check_log_period.isChecked()))
        self.ui.btn_log_download_run.clicked.connect(lambda: self.thread_logdownload())
        self.ui.btn_logdownload_openfolder.clicked.connect(lambda: os.startfile(self.path_dir_logdownload))
    def ui_functions_csvmerge(self):
        # CSV Merge ####################################################################################################
        self.ui.line_merge_savepath.setEnabled(False)
        self.ui.radio_merge_savepath_default.clicked.connect(lambda: self.ui_functions_merge_radio_change())
        self.ui.radio_merge_savepath_input.clicked.connect(lambda: self.ui_functions_merge_radio_change())
        self.ui.btn_merge_run.clicked.connect(lambda: self.thread_csvmerge())
        self.ui.btn_merge_paths_read.clicked.connect(lambda: self.csvmerge_addFilelist())
        self.ui.btn_merge_list_delete.clicked.connect(lambda: self.csvmerge_chageFilelist('select'))
        self.ui.btn_merge_list_clear.clicked.connect(lambda: self.csvmerge_chageFilelist('all'))
        self.ui.list_merge_filelist.setSelectionMode(QAbstractItemView.ExtendedSelection)
    def ui_functions_ommmerge(self):
        # OMM Merge ####################################################################################################
        self.ui.btn_omm_load.clicked.connect(lambda: self.omm_get_filelist())
        self.ui.btn_omm_run.clicked.connect(lambda: self.omm_merge_files())
    def ui_functions_imagecrop(self):
        # init
        self.ui.line_imagecrop_x1.setText('0')
        self.ui.line_imagecrop_y1.setText('0')
        self.ui.line_imagecrop_x2.setText('0')
        self.ui.line_imagecrop_y2.setText('0')
        # Image Crop ###################################################################################################
        self.ui.btn_imagecrop_path.clicked.connect(lambda: self.image_crop_load())
        self.ui.list_imagecrop_filelist.clicked.connect(lambda: self.image_crop_view())
        self.ui.list_imagecrop_filelist.doubleClicked.connect(lambda: os.startfile(self.ui.list_imagecrop_filelist.currentItem().text()))
        self.ui.btn_imagecrop_preview.clicked.connect(lambda: self.image_crop_preview())
        self.ui.btn_imagecrop_run.clicked.connect(lambda: self.image_crop_thread())
    def ui_functions_imageinsert(self):
        # init
        self.ui_functions_imageinsert_radio_dir_change()
        self.ui_functions_imageinsert_radio_cellsize_change()

        # Image Insert #################################################################################################
        self.ui.btn_imageinsert_load.clicked.connect(lambda: self.image_insert_excelfile_load())
        self.ui.btn_imageinsert_imagepath_load.clicked.connect(lambda: self.image_insert_imagefile_load(True))
        self.ui.btn_imageinsert_imagepath_add.clicked.connect(lambda: self.image_insert_imagefile_load(False))
        self.ui.btn_imageinsert_imagepath_clear.clicked.connect(lambda: self.ui.list_imageinsert_imagepathlist.clear())

        self.ui.btn_imageinsert_imagepath_load.clicked.connect(lambda: self.image_insert_imagefile_load(True))
        self.ui.list_imageinsert_imagepathlist.clicked.connect(lambda: self.image_insert_inputimage(self.ui.list_imageinsert_imagepathlist.currentItem().text()))
        self.ui.list_imageinsert_imagepathlist.doubleClicked.connect(lambda: os.startfile(self.ui.list_imageinsert_imagepathlist.currentItem().text()))
        self.ui.radio_imageinsert_dir_down.clicked.connect(lambda: self.ui_functions_imageinsert_radio_dir_change())
        self.ui.radio_imageinsert_dir_right.clicked.connect(lambda: self.ui_functions_imageinsert_radio_dir_change())
        self.ui.radio_imageinsert_dir_complex.clicked.connect(lambda: self.ui_functions_imageinsert_radio_dir_change())
        self.ui.radio_imageinsert_fit_height.clicked.connect(lambda: self.ui_functions_imageinsert_radio_cellsize_change())
        self.ui.radio_imageinsert_fit_width.clicked.connect(lambda: self.ui_functions_imageinsert_radio_cellsize_change())
        self.ui.radio_imageinsert_set_width.clicked.connect(lambda: self.ui_functions_imageinsert_radio_cellsize_change())
        self.ui.radio_imageinsert_set_height.clicked.connect(lambda: self.ui_functions_imageinsert_radio_cellsize_change())

        # self.ui.line_imageinsert_excelfilepath.setText('D:/ProgramData/Project/M_Project/1.xlsx')
        # self.ui.line_imageinsert_imagepath.setText('D:/ProgramData/새 폴더 (4)')
        self.ui.btn_imageinsert_run.clicked.connect(lambda: self.image_insert_thread())
        # self.ui.label_imagecrop_image.clicked.connect(lambda: self.test())
        self.ui.btn_page_exit.clicked.connect(lambda: self.close())
    def ui_functions_automouse(self):
        # init
        action_items = ['마우스','키보드','이미지서치','대기','추가기능']
        self.keyboard_command = read_json(self.path_file_keyboard_command_json)
        action_keyboard_category = []
        for setting in self.keyboard_command:
            action_keyboard_category.append(setting)

        self.ui.combo_macro_action.addItems(action_items)
        self.macro_reciepes_load()
        self.ui.btn_imageinsert_load.clicked.connect(lambda: self.image_insert_excelfile_load())
        self.ui.combo_macro_action.currentTextChanged.connect(self.ui_functions_automouse_groupbox)
        self.ui.btn_macro_command_edit.clicked.connect(lambda: self.command_edit())
        self.ui.list_macros.clicked.connect(lambda: self.command_edit_listselect())
        self.ui.list_macro_keyboard_category.addItems(action_keyboard_category)
        self.ui.list_macro_keyboard_category.clicked.connect(lambda: self.command_keyboard_category())
        self.ui.list_macro_keyboard_commands.clicked.connect(lambda: self.command_keyboard_input())

        # UI Buttons
        self.get_mouse_pos_thread()
        self.ui.btn_macro_reciepe_load.clicked.connect(lambda: self.macro_reciepes('load'))
        self.ui.btn_macro_reciepe_save.clicked.connect(lambda: self.macro_reciepes('save'))
        self.ui.btn_macro_list_up.clicked.connect(lambda: self.macro_reciepes_functions('up'))
        self.ui.btn_macro_list_down.clicked.connect(lambda: self.macro_reciepes_functions('down'))
        self.ui.btn_macro_list_clear.clicked.connect(lambda: self.macro_reciepes_functions('clear'))
        self.ui.btn_macro_list_copy.clicked.connect(lambda: self.macro_reciepes_functions('copy'))
        self.ui.btn_macro_list_delete.clicked.connect(lambda: self.macro_reciepes_functions('delete'))
        self.ui.btn_macro_run.clicked.connect(lambda: self.thread_macro())

        # Groupbox Click
        self.ui.groupBox_macro_mouse.mousePressEvent = self.event_group_mouse
        self.ui.groupBox_macro_keyboard.mousePressEvent = self.event_group_keyboard
        self.ui.groupBox_macro_imagesearch.mousePressEvent = self.event_group_imagesearch
        self.ui.groupBox_macro_delay.mousePressEvent = self.event_group_delay
        self.ui.groupBox_macro_plugin.mousePressEvent = self.event_group_plugin


        # UI Text Changes
        self.ui.line_macro_mouse_posx.textChanged.connect(lambda: self.command_generator('마우스'))
        self.ui.line_macro_mouse_posy.textChanged.connect(lambda: self.command_generator('마우스'))
        self.ui.line_macro_mouse_offset_x.textChanged.connect(lambda: self.command_generator('마우스'))
        self.ui.line_macro_mouse_offset_y.textChanged.connect(lambda: self.command_generator('마우스'))
        self.ui.line_macro_mouse_posx2.textChanged.connect(lambda: self.command_generator('마우스'))
        self.ui.line_macro_mouse_posy2.textChanged.connect(lambda: self.command_generator('마우스'))
        self.ui.line_macro_keyboard_keys.textChanged.connect(lambda: self.command_generator('키보드'))
        self.ui.line_macro_imagesearch_path.textChanged.connect(lambda: self.command_generator('이미지서치'))
        self.ui.line_macro_imagesearch_confidence.textChanged.connect(lambda: self.command_generator('이미지서치'))
        self.ui.line_macro_imagesearch_variable.textChanged.connect(lambda: self.command_generator('이미지서치'))
        self.ui.line_macro_delay.textChanged.connect(lambda: self.command_generator('대기'))

        # Command input
        self.ui.btn_macro_command_insert.clicked.connect(lambda: self.command_input())
    def ui_functions_automouse_groupbox(self, text):
        ui_groupbox = {"마우스": self.ui.groupBox_macro_mouse,
                       "키보드": self.ui.groupBox_macro_keyboard,
                       "이미지서치": self.ui.groupBox_macro_imagesearch,
                       "대기": self.ui.groupBox_macro_delay,
                       "추가기능":self.ui.groupBox_macro_plugin}
        ui_groupbox2 = {"마우스": ["좌클릭","우클릭","드래그","더블클릭","이동"],
                       "키보드": ["키입력","키누르기_유지(단일키)","키떼기(단일키)"],
                       "이미지서치": ["이미지서치"],
                       "대기": ["대기"],
                       "추가기능":["추가기능(개발중)"]}

        for ui in ui_groupbox:
            close_ui = ui_groupbox[ui]
            close_title = close_ui.title()
            close_title = close_title.replace("▼", "▶")
            close_ui.setTitle(close_title)
            close_ui.setMinimumHeight(0)
            close_ui.setMaximumHeight(12)
        if text != "-선택-":
            open_ui = ui_groupbox[text]
            open_title = open_ui.title()
            open_title = open_title.replace("▶", "▼")
            open_ui.setTitle(open_title)
            open_ui.setMinimumHeight(350)
            open_ui.setMaximumHeight(350)

            self.ui.combo_macro_action_items.clear()
            self.ui.combo_macro_action_items.addItems(ui_groupbox2[text])
    def ui_functions(self):
        # init
        settings  = read_json(self.path_file_settings_json)
        self.ui_setting(settings)

        # 날짜 자동 기입
        self.today = datetime.datetime.today()
        self.yesterday = self.today - datetime.timedelta(days=1)
        self.ui.line_ngimage_datefrom.setText(self.yesterday.strftime("%Y-%m-%d"))
        self.ui.line_ngimage_dateto.setText(self.today.strftime("%Y-%m-%d"))
        self.ui.line_mes_datefrom.setText(self.yesterday.strftime("%Y-%m-%d"))
        self.ui.line_mes_dateto.setText(self.today.strftime("%Y-%m-%d"))
        self.ui.progressBar.setVisible(False)
        self.ui.checkBox_18.setEnabled(False)
        self.ui.btn_mes_run.setEnabled(False)
        self.ui.line_log_enddate.setEnabled(False)

        # 우측 상단 버튼
        self.ui.btn_version.clicked.connect(lambda: self.versions(True))
        self.ui.bnt_settings_openjson.clicked.connect(lambda: os.startfile(self.path_file_settings_json))

        # OIS Assy 전용 UI Functions ####################################################################################
        self.ui.btn_ngimage_selectall.clicked.connect(lambda: self.ui_functions_checkbox_selectall("ngimage"))
        self.ui.btn_mes_selectall.clicked.connect(lambda: self.ui_functions_checkbox_selectall("mes"))
        self.ui.btn_ngimage_run.clicked.connect(lambda: self.thread_ngimage())


        self.ui_functions_pagechange()
        self.ui_functions_logdownload()
        self.ui_functions_csvmerge()
        self.ui_functions_ommmerge()
        self.ui_functions_imagecrop()
        self.ui_functions_imageinsert()
        self.ui_functions_automouse()


    # UI 기능 관련 분류 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # UI 기능 관련 분류 > 시스템 메세지─────────────────────────────────────────────────────────────────────────────────────
    def message(self, msg):
        dt = datetime.datetime.now()
        dt = dt.strftime("%y/%m/%d %H:%M:%S")
        log = f'[{dt}] {msg}'
        print(log)
        self.ui.list_RunningMessage.addItem(log)
        self.ui.list_RunningMessage.scrollToBottom()

    # UI 기능 관련 분류 > Check Box 전체선택 / 해제 관련 Functions───────────────────────────────────────────────────────────
    def ui_functions_checkbox_selectall(self, page):
        checkbox_list =[]
        if page == 'ngimage':
            checkbox_list = [self.ui.check_ngimage_mes,self.ui.check_ngimage_las,self.ui.check_ngimage_excel]
        elif page == 'mes':
            checkbox_list = [self.ui.check_mes_outlook,self.ui.check_mes_mes,self.ui.check_mes_las,self.ui.check_mes_excel]
        false_count = 0
        for checkbox in checkbox_list:
            if checkbox.isChecked():
                false_count += 1
        for checkbox in checkbox_list:
            if false_count > 0:
                checkbox.setChecked(False)
            else:
                checkbox.setChecked(True)
    def ui_functions_log_checkbox_selectall(self, groupbox):
        if groupbox == 'mc':
            check_list = self.check_log_mc_list
        elif groupbox == 'log':
            check_list = self.check_log_loglist
        elif groupbox == 'process':
            check_list = self.check_log_process_list
        temp_count = 0
        for checkbox in check_list:
            if checkbox.isChecked():
                temp_count += 1
        if temp_count > 0:
            state = False
        else:
            state = True
        for checkbox in check_list:
            checkbox.setChecked(state)
    def ui_functions_sidemenu(self, frame):
        set_width = 109
        if frame.width() == set_width:
            frame.setFixedWidth(0)
            MainWindow.setFixedWidth(self, MainWindow.width(self) - set_width)
        else:
            MainWindow.setFixedWidth(self, MainWindow.width(self) + set_width)
            frame.setFixedWidth(set_width)

    # UI 기능 관련 분류 > Radio Button Click 시 Functions ────────────────────────────────────────────────────────────────
    def ui_functions_merge_radio_change(self):
        if self.ui.radio_merge_savepath_default.isChecked():
            state = False
        else:
            state = True
        self.ui.line_merge_savepath.setEnabled(state)
    def ui_functions_imageinsert_radio_dir_change(self):
        if self.ui.radio_imageinsert_dir_complex.isChecked():
            state = True
        else:
            state = False
        self.ui.line_imageinsert_dir_complex.setEnabled(state)
    def ui_functions_imageinsert_radio_cellsize_change(self):
        if self.ui.radio_imageinsert_set_height.isChecked() or self.ui.radio_imageinsert_set_width.isChecked():
            state = True
        else:
            state = False
        self.ui.line_imageinsert_set_size.setEnabled(state)



    # Main Thread ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # Main Thread > OIS Ass'y 전용 > 불량 이미지 다운로드 ──────────────────────────────────────────────────────────────────
    def thread_ngimage(self):
        run_process_list = []
        if self.ui.check_ngimage_mes.isChecked():
            run_process_list.append('MES')
        if self.ui.check_ngimage_las.isChecked():
            run_process_list.append('LAS')
        if self.ui.check_ngimage_excel.isChecked():
            run_process_list.append('REPORT')

        date_from = self.ui.line_ngimage_datefrom.text()
        date_to = self.ui.line_ngimage_dateto.text()
        imagepath = self.path_imagepath
        self.ngimage_thread = QThread()
        self.ngimage_image = NG_Image(run_process_list=run_process_list, imagepath=imagepath, nowdir=self.now_dir, date_from=date_from, date_to=date_to)
        self.ngimage_image.moveToThread(self.ngimage_thread)
        self.ngimage_thread.started.connect(self.ngimage_image.run)
        self.ngimage_image.prog.connect(self.thread_ngimage_progress)
        self.ngimage_image.flag.connect(self.thread_ngimage_flag)
        self.ngimage_image.msg.connect(self.message)
        self.ngimage_thread.start()
    def thread_ngimage_flag(self,flag):
        if flag:
            self.ngimage_thread.quit()
            self.message(f'NG Image Thread 정상종료')
    def thread_ngimage_progress(self, judge, data):
        if judge:
            self.p_total = data
            self.ui.progressBar.show()
        else:
            self.p_data = data
            p = int((self.p_data/self.p_total)*100)
            self.ui.progressBar.setValue(p)
            if p >= 100:
                self.ui.progressBar.hide()
                self.thread_ngimage_flag(True)

    # Main Thread > OIS Ass'y 전용 > 로그다운로드 ─────────────────────────────────────────────────────────────────────────
    def thread_logdownload(self):
        date_list = []
        if self.ui.check_log_period.isChecked():
            from_date = self.ui.line_log_fromdate.text()
            from_dt_y = int(from_date.split('-')[0])
            from_dt_m = int(from_date.split('-')[1])
            from_dt_d = int(from_date.split('-')[2])
            dt_fromdate = datetime.datetime(from_dt_y,from_dt_m,from_dt_d)
            to_date =  self.ui.line_log_enddate.text()
            to_dt_y = int(to_date.split('-')[0])
            to_dt_m = int(to_date.split('-')[1])
            to_dt_d = int(to_date.split('-')[2])
            dt_todate = datetime.datetime(to_dt_y, to_dt_m, to_dt_d)
            period = dt_todate - dt_fromdate
            period = period.days
            for i in range(0,period+1):
                days = dt_fromdate + datetime.timedelta(days=i)
                date_list.append(days.strftime("%Y-%m-%d"))
        else:
            date_list.append(self.ui.line_log_fromdate.text())

        mc_list = []
        log_list = []
        process_list = []
        checkbox_list = [self.check_log_mc_list, self.check_log_loglist, self.check_log_process_list]
        checkbox_datalist = [mc_list, log_list, process_list]
        for i in range(len(checkbox_list)):
            checkboxs = checkbox_list[i]
            datalist = checkbox_datalist[i]
            for checkbox in checkboxs:
                if checkbox.isChecked():
                    state=True
                else:
                    state=False
                datalist.append(state)
        lotid_list = self.ui.text_log_lotids.toPlainText().split('\n')
        savepath = self.path_dir_logdownload
        self.logdownload_thread = QThread()
        self.logdownload = LogDownload(date_list=date_list, mc_list=mc_list, log_list=log_list, process_list=process_list, lotid_list=lotid_list, savepath=savepath)
        self.logdownload.moveToThread(self.logdownload_thread)
        self.logdownload_thread.started.connect(self.logdownload.run)
        self.logdownload.prog.connect(self.thread_logdownload_progress)
        self.logdownload.flag.connect(self.thread_logdownload_flag)
        self.logdownload.msg.connect(self.message)
        self.logdownload_thread.start()
    def thread_logdownload_flag(self, flag):
        if flag:
            self.logdownload_thread.quit()
            self.message(f'로그다운로드 Thread 정상종료')
            if self.ui.check_logdownload_openfolder.isChecked():
                os.startfile(self.path_dir_logdownload)
    def thread_logdownload_progress(self, judge, data):
        if judge:
            self.p_total = data
            self.ui.progressBar.show()
        else:
            self.p_data = data
            p = int((self.p_data/self.p_total)*100)
            self.ui.progressBar.setValue(p)
            if p >= 100:
                self.ui.progressBar.hide()
                self.thread_logdownload_flag(True)

    # Main Thread > CSV Merge ──────────────────────────────────────────────────────────────────────────────────────────
    def thread_csvmerge(self):
        ui_read_savefilename = self.ui.line_merge_savefilename.text()
        if self.ui.radio_merge_savepath_input.isChecked():
            savepath = self.ui.line_merge_savepath.text()
        else:
            savepath = ""

        path_list = []
        count = 0
        while True:
            try:
                data = self.ui.list_merge_filelist.item(count).text()
                path_data = data.split("<:>")[0]
            except:
                break
            print(self.ui.list_merge_filelist.item(count).text())
            path_list.append(path_data)
            count += 1
        self.csvmerge_thread = QThread()
        self.csvmerge = CSV_Merge(pathlist = path_list, save_path=savepath, save_filename=ui_read_savefilename)
        self.csvmerge.moveToThread(self.csvmerge_thread)
        self.csvmerge_thread.started.connect(self.csvmerge.run)
        self.csvmerge.prog.connect(self.thread_csvmerge_progress)
        self.csvmerge.flag.connect(self.thread_csvmerge_flag)
        self.csvmerge.msg.connect(self.message)
        self.csvmerge_thread.start()
    def csvmerge_addFilelist(self):
        ui_read_path = self.ui.text_merge_paths.toPlainText()
        if ui_read_path.find('\n') != -1:
            pathlist = ui_read_path.split('\n')
        else:
            pathlist = [ui_read_path]
        temp_filelist = []
        filesize_sum = 0
        extensions = self.ui.combo_merge_extensions.currentText()
        for path in pathlist:
            filelist = os.listdir(path)
            for file in filelist:
                if file.find(extensions) != -1:
                    temp_path = f'{path}/{file}'
                    temp_filelist.append(temp_path)
                    filesize = os.path.getsize(temp_path)
                    filesize_sum += filesize
                    self.ui.list_merge_filelist.addItem(f'{temp_path}<:>({self.get_filesize(filesize)})')
                    self.ui.list_merge_filelist.scrollToBottom()
        total_filesize = self.get_filesize(filesize_sum)
        fileread_result = f'파일 수 : {len(temp_filelist)}개 / 전체 파일 크기 : {total_filesize}'
        self.ui.label_merge_fileqty.setText(fileread_result)
    def csvmerge_chageFilelist(self, mode):
        if mode == 'all':
            self.ui.list_merge_filelist.clear()
        else:
            selectedItems = self.ui.list_merge_filelist.selectedItems()

            if not selectedItems: return
            for item in selectedItems:
                self.ui.list_merge_filelist.takeItem(self.ui.list_merge_filelist.row(item))




            # count = 1
            # while True:
            #     current_data = self.ui.list_merge_filelist.item(count)
            #     current_data = current_data.text()
            #     state = True
            #     for remove_text in remove_list:
            #         if remove_text == current_data:
            #             state = False
            #             break
            #     if current_data.find("<:>") == -1:
            #         break
            #     if state:
            #         append_list.append(current_data)
            #     count += 1
            #
            # self.ui.list_merge_filelist.clear()
            # self.ui.list_merge_filelist.addItems(append_list)
    def thread_csvmerge_flag(self, flag):
        if flag:
            self.csvmerge_thread.quit()
            self.message(f'로그다운로드 Thread 정상종료')
    def thread_csvmerge_progress(self, judge, data):
        if judge:
            self.p_total = data
            self.ui.progressBar.show()
        else:
            self.p_data = data
            p = int((self.p_data/self.p_total)*100)
            self.ui.progressBar.setValue(p)
            if p >= 100:
                self.ui.progressBar.hide()
                self.thread_csvmerge_flag(True)

    # Main Thread > OIS Ass'y 전용 > OMM ────────────────────────────────────────────────────────────────────────────────
    def omm_get_filelist(self):
        #self.ui.line_omm_path.setText("D:/1. 측정데이터/OIS Ass'y SIDE2-1_A3.1_FAI10-1,13-1_rev0")
        basicpath = self.ui.line_omm_path.text()
        file_count = 0
        file_size = 0
        for folder in os.listdir(basicpath):
            if os.path.isdir(os.path.join(basicpath, folder)):
                filepath = f'{basicpath}/{folder}/k3'
                for file in os.listdir(filepath):
                    if file.find('.txt') != -1:
                        path = filepath + f'/{file}'
                        self.ui.list_omm_filelist.addItem(path)
                        self.ui.list_omm_filelist.scrollToBottom()
                        file_count += 1
                        file_size += os.path.getsize(path)
                        break
        self.ui.label_omm_fileinfo.setText(f'파일 수 : {file_count} / 파일 크기 : {self.get_filesize(file_size)}')
        self.message(f'OMM Merge 파일 목록 불러오기 완료 ({basicpath})')
    def omm_merge_files(self):
        basicpath = self.ui.line_omm_path.text()
        savefilename = self.ui.line_omm_savefilename.text()
        count = 0
        pathlist = []
        while True:
            try:
                path_from_ui = self.ui.list_omm_filelist.item(count).text()
                pathlist.append(path_from_ui)
            except:
                break
            count += 1
        read_result = []
        for path in pathlist:
            with open(path, 'r') as r:
                read_result += r.readlines()
        with open(f'{basicpath}/{savefilename}', 'w') as w:
            w.writelines(read_result)
        self.message(f'OMM Merge 완료 ({basicpath})')
        if self.ui.check_omm_openfolder.isChecked():
            os.startfile(basicpath)

    # Main Thread > Image Crop ─────────────────────────────────────────────────────────────────────────────────────────
    def image_crop_load(self):
        path_from_ui = self.ui.line_imagecrop_path.text()
        extensions = ['.png', '.jpg', '.jpeg', '.bmp']
        file_count = 0
        file_size = 0
        for p in os.listdir(path_from_ui):
            path = os.path.join(path_from_ui, p)
            if os.path.isfile(path):
                for e in extensions:
                    if path.find(e) != -1:
                        self.ui.list_imagecrop_filelist.addItem(path)
                        file_count += 1
                        file_size += os.path.getsize(path)
                        break
        self.ui.label_imagecrop_fileinfo.setText(f'파일 수 : {file_count}    파일 크기 : {self.get_filesize(file_size)}')
    def image_crop_view(self, button=None, x=-1, y=-1):
        try:
            image_path = self.ui.list_imagecrop_filelist.selectedItems()[0].text()
        except:
            self.ui.list_imagecrop_filelist.setCurrentIndex(0)
            image_path = self.ui.list_imagecrop_filelist.selectedItems()[0].text()
        # Pixmap -> Label
        # Label -> Pixmap
        # List Click -> Label Image Update
        # Label Image Click (L, R) -> Draw Rect on Label Image & Insert selected Positions
        self.iPixmap = QPixmap(image_path)
        self.label_width = self.ui.label_imagecrop_image.width()
        self.label_height = self.ui.label_imagecrop_image.height()

        self.raw_width = self.iPixmap.width()
        self.raw_Height = self.iPixmap.height()
        if self.raw_width >= self.raw_Height:
            #print("가로이미지")
            self.ratio = self.raw_width / self.raw_Height
            self.w_ratio = self.label_width
            self.h_ratio = self.label_width / self.ratio
            iPixmap = self.iPixmap.scaledToWidth(int(self.w_ratio))
        else:
            #print("세로이미지")
            self.ratio =  self.raw_Height / self.raw_width
            self.w_ratio = self.label_height / self.ratio
            self.h_ratio = self.label_height
            iPixmap = self.iPixmap.scaledToHeight(int(self.h_ratio))

        if button != None:

            # w_ratio = (self.raw_width / self.ratio)
            # h_ratio = (self.raw_Height / self.ratio)
            if self.raw_width > self.raw_Height:
                ratio = self.raw_width/self.label_width
            else:
                ratio = self.raw_Height/self.label_height
            if button == 'left':
                self.ui.line_imagecrop_x1.setText(f'{int(x * ratio)}')
                self.ui.line_imagecrop_y1.setText(f'{int(y * ratio)}')
            if button == 'right':
                self.ui.line_imagecrop_x2.setText(f'{int(x * ratio)}')
                self.ui.line_imagecrop_y2.setText(f'{int(y * ratio)}')

            x1 = int(int(self.ui.line_imagecrop_x1.text()) / ratio)
            y1 = int(int(self.ui.line_imagecrop_y1.text()) / ratio)
            x2 = int(int(self.ui.line_imagecrop_x2.text()) / ratio)
            y2 = int(int(self.ui.line_imagecrop_y2.text()) / ratio)

            if x1 <= x2:
                pos_x = x1
                width = x2 - x1
            else:
                pos_x = x2
                width = x1 - x2

            if y1 <= y2:
                pos_y = y1
                height = y2 - y1
            else:
                pos_y = y2
                height = y1 - y2
            painter = QPainter(iPixmap)
            painter.setPen(QPen(Qt.red, 2))
            painter.drawRect(pos_x, pos_y, width, height)
            painter.end()

        self.ui.label_imagecrop_image.setPixmap(iPixmap)
        # self.ui.label_image.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        #print(f'원래 이미지 크기 w : {self.raw_width}  h : {self.raw_Height}   /  변환된 이미지 크기 :  w : {self.w_ratio}   h : {self.h_ratio}')
    def image_crop_preview(self):
        # savepath = ""
        # path_list = [self.ui.list_imagecrop_filelist.selectedItems()[0].text()]
        # x1 = self.ui.line_imagecrop_x1.text()
        # y1 = self.ui.line_imagecrop_y1.text()
        # x2 = self.ui.line_imagecrop_x2.text()
        # y2 = self.ui.line_imagecrop_y2.text()
        # imagecrop = ImageCrop(filepaths = path_list, savepath=savepath, x1=x1, y1=y1, x2=x2, y2=y2, mode=True)
        # imagecrop.run()

        try:
            now_pixmap = self.ui.label_imagecrop_image.pixmap().toImage()
        except:
            now_pixmap = None
    def image_crop_thread(self):
        #self.ui.radio_imagecrop_save_result.isChecked()
        if self.ui.radio_imagecrop_save_result.isChecked():
            savepath = ""
        else:
            savepath = ""
        path_list = []
        count = 0
        while True:
            try:
                data = self.ui.list_imagecrop_filelist.item(count).text()
            except:
                break
            path_list.append(data)
            count += 1
        x1 = self.ui.line_imagecrop_x1.text()
        y1 = self.ui.line_imagecrop_y1.text()
        x2 = self.ui.line_imagecrop_x2.text()
        y2 = self.ui.line_imagecrop_y2.text()

        self.imagecrop_thread = QThread()
        self.imagecrop = ImageCrop(filepaths = path_list, savepath=savepath, x1=x1, y1=y1, x2=x2, y2=y2)
        self.imagecrop.moveToThread(self.imagecrop_thread)
        self.imagecrop_thread.started.connect(self.imagecrop.run)
        self.imagecrop.prog.connect(self.thread_imagecrop_progress)
        self.imagecrop.flag.connect(self.thread_imagecrop_flag)
        self.imagecrop.msg.connect(self.message)
        self.imagecrop_thread.start()
    def thread_imagecrop_flag(self, flag):
        if flag:
            self.imagecrop_thread.quit()
            self.message(f'이미지 Crop Thread 정상종료')
    def thread_imagecrop_progress(self, judge, data):
        if judge:
            self.p_total = data
            self.ui.progressBar.show()
        else:
            self.p_data = data
            p = int((self.p_data / self.p_total) * 100)
            self.ui.progressBar.setValue(p)
            if p >= 100:
                self.ui.progressBar.hide()
                self.thread_imagecrop_flag(True)
    def mousePressEvent(self, event):
        # print('button() : ',event.button())
        # print('buttons() : ', event.buttons())
        # print('pos().x() pos().y(): ',event.pos().x(),event.pos().y())
        # print('flags() : ',event.flags())
        # print('localPos() : ',event.localPos())
        # print('windowPos :', event.windowPos() )
        # label_image_area = (0, 0, 0, 0)
        object_widget = self.ui.label_imagecrop_image
        object_list = ['frame_26','page_imagecrop','stackedWidget','frame_main','frame_24']
        x1 = object_widget.x()
        y1 = object_widget.y()
        width = object_widget.width()
        height = object_widget.height()
        while True:
            try:
                object_widget = object_widget.parentWidget()
                object_name = object_widget.objectName()
                if object_name in object_list:
                    x = object_widget.x()
                    y = object_widget.y()
                    x1 += x
                    y1 += y
            except:
                break

        x2 = x1 + width
        y2 = x2 + height
        if event.pos().x() >= x1 and event.pos().x() <= x2 and event.pos().y() >= y1 and event.pos().y() <= y2:
            if event.button() == 1:
                button = 'left'
            else:
                button = 'right'
            try:
                self.image_crop_view(button, event.pos().x() - x1, int(event.pos().y()-y1))
            except:
                pass


    # Main Thread > Image Insert ───────────────────────────────────────────────────────────────────────────────────────
    def image_insert_excelfile_load(self):
        filepath = self.ui.line_imageinsert_excelfilepath.text()
        self.excel = ImageInsert(excelfilepath=filepath)
        sheetnames = self.excel.sheetnames
        self.ui.combo_imageinsert_sheets.addItems(sheetnames)
        print(self.excel)
    def image_insert_imagefile_load(self, add=False):

        imagefilepath = self.ui.line_imageinsert_imagepath.text()
        filecount = 0
        filesize = 0
        if add:
            self.ui.list_imageinsert_imagepathlist.clear()
        for filepath in os.listdir(imagefilepath):
            imagepath = os.path.join(imagefilepath, filepath)
            if filecount == 0:
                self.image_insert_inputimage(imagepath)
            self.ui.list_imageinsert_imagepathlist.addItem(imagepath)
            filecount += 1
            filesize += os.path.getsize(imagepath)
        self.ui.label_imageinsert_imagepath_load_result.setText(f'이미지 파일 수 : {filecount}  전체 크기 : {self.get_filesize(filesize)}')
        self.message(f'Image Insert Image File Load .. 이미지 파일 수 {filecount} / 파일 전체 크기 {self.get_filesize(filesize)}')
    def image_insert_inputimage(self, image_path):
        iPixmap = QPixmap(image_path)
        label_width = self.ui.label_imageinsert_image.width()
        label_height = self.ui.label_imageinsert_image.height()
        raw_width = iPixmap.width()
        raw_Height = iPixmap.height()
        if raw_width >= raw_Height:
            #print("가로이미지")
            ratio = raw_width / raw_Height
            w_ratio = label_width
            h_ratio = label_width / ratio
            iPixmap = iPixmap.scaledToWidth(int(w_ratio))
        else:
            #print("세로이미지")
            ratio =  raw_Height / raw_width
            w_ratio = label_height / ratio
            h_ratio = label_height
            iPixmap = iPixmap.scaledToHeight(int(h_ratio))
        self.ui.label_imageinsert_image.setPixmap(iPixmap)
        self.ui.label_imageinsert_image.setAlignment(Qt.AlignLeft | Qt.AlignTop)
    def image_insert_thread(self):
        print(self.excel)
        opt_cell = self.ui.line_imageinsert_celladdress.text()
        opt_excelfile = self.ui.line_imageinsert_excelfilepath.text()
        opt_sheetname = self.ui.combo_imageinsert_sheets.currentText()

        if self.ui.radio_imageinsert_fit_height.isChecked():
            size = ['h','0']
        elif self.ui.radio_imageinsert_fit_width.isChecked():
            size = ['w','0']
        elif self.ui.radio_imageinsert_set_height.isChecked():
            size = ['h', self.ui.line_imageinsert_set_size.text()]
        elif self.ui.radio_imageinsert_set_width.isChecked():
            size = ['w', self.ui.line_imageinsert_set_size.text()]

        if self.ui.radio_imageinsert_dir_down.isChecked():
            dir = ['d','0']
        elif self.ui.radio_imageinsert_dir_right.isChecked():
            dir = ['r', '0']
        elif self.ui.radio_imageinsert_dir_complex.isChecked():
            dir = ['c', int(self.ui.line_imageinsert_dir_complex.text())]
        opt_inputfilename = self.ui.check_imageinsert_insertfilename.isChecked()

        opt_imagefilelist = []
        count = 0
        while True:
            try:
                data = self.ui.list_imageinsert_imagepathlist.item(count).text()
            except:
                break
            opt_imagefilelist.append(data)
            count += 1
        self.imageinsert_thread = QThread()
        self.imageinsert = ImageInsert(sheetname=opt_sheetname, excelfilepath=opt_excelfile, imagefilelist=opt_imagefilelist, inputcell=opt_cell, cellsize=size, inputdir=dir, inputfilename=opt_inputfilename)
        self.imageinsert.moveToThread(self.imageinsert_thread)
        self.imageinsert_thread.started.connect(self.imageinsert.run)
        self.imageinsert.prog.connect(self.thread_imageinsert_progress)
        self.imageinsert.flag.connect(self.thread_imageinsert_flag)
        self.imageinsert.msg.connect(self.message)
        self.imageinsert_thread.start()
    def thread_imageinsert_flag(self, flag):
        if flag:
            self.imageinsert_thread.quit()
            self.message(f'이미지 Insert Thread 정상종료')
    def thread_imageinsert_progress(self, judge, data):
        if judge:
            self.p_total = data
            self.ui.progressBar.show()
        else:
            self.p_data = data
            p = int((self.p_data / self.p_total) * 100)
            self.ui.progressBar.setValue(p)
            if p >= 100:
                self.ui.progressBar.hide()
                self.thread_imageinsert_flag(True)


    # Main Thread > automouse ──────────────────────────────────────────────────────────────────────────────────────────
    def thread_macro(self):
        commands = []
        count = 0
        while True:
            try:
                command = self.ui.list_macros.item(count).text()
                command = command.rstrip()
                commands.append(command)
            except:
                break
            count+=1
        repeats = int(self.ui.line_macro_repeat.text())
        stopkey = self.ui.line_macro_forcestop.text()

        # self.message(f'Macro Run.....3s....')
        # time.sleep(1)
        # self.message(f'Macro Run.....2s....')
        # time.sleep(1)
        # self.message(f'Macro Run.....1s....')
        # time.sleep(1)
        # self.message(f'Macro Run')

        self.macro_thread = QThread()
        self.macro = AutoMouse(commands, repeats, stopkey)
        self.macro.moveToThread(self.macro_thread)
        self.macro_thread.started.connect(self.macro.run)
        self.macro.flag.connect(self.thread_macro_flag)
        self.macro.msg.connect(self.message)
        self.macro_thread.start()
    def thread_macro_flag(self, flag):
        if flag:
            self.macro_thread.quit()
            self.message(f'Macro Thread 정상종료')

    def command_generator(self, changeItem):
        command1 = self.ui.combo_macro_action.currentText()
        command2 = self.ui.combo_macro_action_items.currentText()
        items = {'마우스':[self.ui.line_macro_mouse_posx, self.ui.line_macro_mouse_posy, self.ui.line_macro_mouse_offset_x, self.ui.line_macro_mouse_offset_y,self.ui.line_macro_mouse_posx2,self.ui.line_macro_mouse_posy2],
                 '키보드':[self.ui.line_macro_keyboard_keys],
                 '이미지서치':[self.ui.line_macro_imagesearch_variable,self.ui.line_macro_imagesearch_confidence,self.ui.line_macro_imagesearch_path],
                 '대기':[self.ui.line_macro_delay],
                 '추가기능':[],
        }
        command = f'+{command1}+{command2}'
        for ui in items[changeItem]:
            if ui.text() == "":
                command += f'+None'
            else:
                command += f'+{ui.text()}'
        self.ui.line_macro_command.setText(command)
    def command_input(self):
        command = self.ui.line_macro_command.text()
        if command == "" or len(command) <= 5:
            return
        self.ui.list_macros.addItem(command)
        self.ui.list_macros.scrollToBottom()
        self.ui.btn_macro_command_edit.setEnabled(False)
        self.ui_style(self.ui.radio_setting_lightmode.isChecked())
    def command_edit(self):
        change_text = self.ui.line_macro_command.text()
        current_index = self.ui.list_macros.currentRow()
        new_item = QListWidgetItem(change_text)
        self.ui.list_macros.insertItem(current_index + 1, new_item)
        self.ui.list_macros.takeItem(current_index)

    def command_keyboard_category(self):
        selected_category = self.ui.list_macro_keyboard_category.selectedItems()[0].text()

        selected_category_items = self.keyboard_command[selected_category]
        input_items = []
        for item in selected_category_items:
            input_items.append(item)

        descriptions = {'단축키':'＞선택한 단축키 작업을 실행합니다. 키누르기(유지) 키떼기를 선택하면 적용되지 않습니다.',
                        '특수키':'＞특수키',
                        '방향키':'＞방향키',
                        '펑션키':'＞선택한 펑션키 작업을 실행합니다. 키누르기(유지) 키떼기를 적용할 수 있습니다.',
                        '명령어': '＞추가 명령어를 사용해 변수처럼 사용할 수 있습니다.',
                        '날짜와시간':'＞날짜형식의 데이터를 사용할 수 있습니다. 지정된 형식이 없는 경우 직접 입력칸의 괄호 안을 수정하면 사용할 수 있습니다.\n날짜형식에서 yyyy는 4자리 연도, mm은 2자리 월 dd는 2자리 일자입니다.\n시간형식에서 H는 시간, M은 분 S는 초를 나타냅니다.',
                        '클립보드':'＞클립보드에 원하는 문구를 복사할 수 있습니다.'}

        self.ui.list_macro_keyboard_commands.clear()
        self.ui.list_macro_keyboard_commands.addItems(input_items)

        description = descriptions[selected_category]
        self.ui.label_macro_keyboard_description.setWordWrap(True)
        self.ui.label_macro_keyboard_description.setText(description)
    def command_keyboard_input(self):
        category = self.ui.list_macro_keyboard_category.selectedItems()[0].text()
        command = self.ui.list_macro_keyboard_commands.selectedItems()[0].text()
        self.ui.line_macro_keyboard_keys.setText(self.keyboard_command[category][command])


    def command_edit_listselect(self):
        self.ui.line_macro_command.setText(self.ui.list_macros.currentItem().text())
        self.ui.btn_macro_command_edit.setEnabled(True)
        self.ui_style(self.ui.radio_setting_lightmode.isChecked())
    # 매크로 레시피 저장 관련
    def macro_reciepes_functions(self, mode):
        '''mode = up / down / clear / copy / delete'''
        if mode == 'up' or mode == 'down':
            current_index = self.ui.list_macros.currentRow()
            i = 0
            if mode == 'up' and current_index > 0:
                i = -1
            if mode == 'down':
                i = 1
            self.ui.list_macros.insertItem(current_index + i, self.ui.list_macros.takeItem(current_index))
            self.ui.list_macros.setCurrentRow(current_index + i)
        if mode == 'clear':
            if self.ui_question('경고', f'현재까지 작성한 매크로가 초기화 됩니다.\n초기화 하시겠습니까?'):
                self.ui.list_macros.clear()

        if mode == 'copy':
            current_index = self.ui.list_macros.currentRow()
            if current_index < self.ui.list_macros.count() - 1:
                current_item = self.ui.list_macros.currentItem()
                new_item = QListWidgetItem(current_item.text())
                self.ui.list_macros.insertItem(current_index + 1, new_item)

        if mode == 'delete':
            current_index = self.ui.list_macros.currentRow()
            self.ui.list_macros.takeItem(current_index)
    def macro_reciepes_load(self):
        reciepe_path = self.path_dir_macroreciepes
        macro_list = os.listdir(reciepe_path)
        self.ui.combo_macro_reciepe_load.clear()

        for macro in macro_list:
            reciepe_name = macro.replace('.txt','')
            self.ui.combo_macro_reciepe_load.addItem(reciepe_name)
    def macro_reciepes(self, mode='load'):
        path = self.path_dir_macroreciepes
        if mode == 'load':
            # print('load')
            # print(os.listdir(self.path_dir_macroreciepes))
            # self.ui.combo_macro_reciepe_load.addItem('test')

            reciepe_name = self.ui.combo_macro_reciepe_load.currentText()
            reciepe_path = f'{self.path_dir_macroreciepes}/{reciepe_name}.txt'

            if self.ui.list_macros.item(0) != None:
                macro_load = self.ui_question('경고', f'매크로를 불러오게 될 경우 현재까지 작성된 매크로가 초기화 됩니다.\n불러오시겠습니까?')
                if not macro_load:
                    return
            self.ui.list_macros.clear()
            with open(reciepe_path, 'r') as r:
                macro_lines = r.readlines()
            for line in macro_lines:
                data = line.rstrip()
                self.ui.list_macros.addItem(data)

        else:#SAVE!!
            # print('save')
            reciepe_name = self.ui.line_macro_reciepe_name.text()
            if reciepe_name == "":
                self.message('매크로를 저장할 파일명을 입력해주세요.')
                return
            reciepe_file = f'{path}/{reciepe_name}.txt'
            # file exists check !
            if os.path.exists(reciepe_file):
                overwrite = self.ui_question('경고',f'이미 {reciepe_name}이라는 매크로가 있습니다.\n덮어쓰시겠습니까?')
                if overwrite:
                    self.message(f'Reciepe 덮어쓰기 : {reciepe_name}')
                if not overwrite:
                    self.message(f'Reciepe 덮어쓰기 취소 : {reciepe_name}')
                    return
            count = 0
            with open(reciepe_file, 'w') as w:
                while True:
                    try:
                        w.write(self.ui.list_macros.item(count).text()+'\n')
                    except:
                        break
                    count += 1
            self.macro_reciepes_load()
            self.message(f'Reciepe 저장 완료 {reciepe_name}')


    # Mouse 좌표 출력 관련
    def get_mouse_pos_thread(self):
        self.mousepos_thread = QThread()
        self.mousepos = MousePos()
        self.mousepos.moveToThread(self.mousepos_thread)
        self.mousepos_thread.started.connect(self.mousepos.position)
        self.mousepos.flag.connect(self.get_mouse_pos_flag)
        self.mousepos.pos.connect(self.get_mouse_pos_pos)
        self.mousepos_thread.start()
    def get_mouse_pos_pos(self, x, y):
        self.ui.label_macro_mouse_nowpos_x.setText(str(x))
        self.ui.label_macro_mouse_nowpos_y.setText(str(y))
    def get_mouse_pos_flag(self, flag):
        if flag:
            self.ui.label_macro_mouse_nowpos_x.setText('0')
            self.ui.label_macro_mouse_nowpos_y.setText('0')
            self.mousepos_thread.quit()
            self.message(f'Mouse Pos Thread 정상종료')
    # Group Box 클릭 시 크기조정 관련
    def event_group_mouse(self, event):
        self.ui.combo_macro_action.setCurrentText('마우스')
    def event_group_keyboard(self, event):
        self.ui.combo_macro_action.setCurrentText('키보드')
    def event_group_imagesearch(self, event):
        self.ui.combo_macro_action.setCurrentText('이미지서치')
    def event_group_delay(self, event):
        self.ui.combo_macro_action.setCurrentText('대기')
    def event_group_plugin(self, event):
        self.ui.combo_macro_action.setCurrentText('추가기능')
    def event_group_sub_action(self, event = None):
        self.command_generator(self.ui.combo_macro_action.currentText())
        # self.ui.combo_macro_action.setCurrentText(self.ui.combo_macro_action.currentText())


    # EVENT       #########################################################################################
    def closeEvent(self, event):
        self.logging(self.get_userinfo("System-Exit"))
    ####################################################################################################################



    def imageMacroTest(self):
        mes = MES(None)
        check_list = [self.ui.label_test1, self.ui.label_test2, self.ui.label_test3, self.ui.label_test4,
                      self.ui.label_test5]
        result = mes.test_before_start()
        temp_text = ""
        state_check = 0
        for i in range(5):
            temp_text = check_list[i].text()

            if "O" in temp_text or "X" in temp_text:
                temp_text = temp_text[0:-1]

            if result[i]:
                temp_text += "O"
            else:
                temp_text += "X"
                state_check += 1
            check_list[i].setText(temp_text)

        if state_check == 0:
            self.ui.btn_macro_test.setEnabled(False)
            self.ui.btn_macro_run.setEnabled(True)
    def thread_lasimage(self):
        self.las_thread = QThread()
        self.las_image = MES(None)
        self.las_image.moveToThread(self.las_thread)
        self.las_thread.started.connect(self.las_image.get_data_from_LASImageTitle)
        self.las_image.prog.connect(self.progress_lasimage)
        self.las_image.flag.connect(self.thread2_flag)
        self.las_thread.start()
    def outlook_foldercheck(self):
        self.foldername = self.ui.line_outlook_foldername.text()

        outlook = MES(self.foldername)
        if outlook.foldercheck():
            self.ui.label_outlook_test.setText("폴더확인 : O")
            self.ui.btn_outlook_run.setEnabled(True)
            self.message2(f'{self.foldername} 검색완료')
        else:
            self.message2(f'{self.foldername} 검색실패, 폴더명, 폴더위치를 확인하세요.')
    def thread_outlook(self):
        self.foldername = self.ui.line_outlook_foldername.text()
        date_from = self.ui.line_outlook_fromdate.text()
        date_end = self.ui.line_outlook_enddate.text()
        if date_from == "" or date_end == "" or len(date_from) != 10 or len(date_end) != 10:
            self.message2("날짜를 확인하세요.")
            return
        self.outlook_thread = QThread()
        self.outlook = MES(f'{self.foldername}/{date_from}/{date_end}')
        self.outlook.moveToThread(self.outlook_thread)
        self.outlook_thread.started.connect(self.outlook.read_mail)
        self.outlook.flag.connect(self.thread3_flag)
        self.outlook.msg.connect(self.message2)
        self.outlook_thread.start()
    # Thread 완료 시 정상적으로 종료하기
    def thread_flag(self, flag):
        if flag:
            self.mes_thread.quit()
    def progress(self, type, prog):
        if type:
            self.total = prog
            self.ui.progressBar.show()
        else:
            self.count = prog
        self.ui.label_state.setText(f'{self.count}/{self.total}')
        try:
            self.ui.progressBar.setValue(int((self.count / self.total) * 100))
        except:
            pass
    # MES 누락 찾기
    def mesmacro_paths(self):
        self.outlook_downloadpath = os.path.join(self.now_dir,'data/Outlook Data/')
        self.gmes_imagepath = os.path.join(self.now_dir,'images/mesmacro/mes/')
        self.gmes_downloadpath = os.path.join(self.now_dir,'data/mesmacro/mes/')
        self.las_imagepath = os.path.join(self.now_dir, 'images/mesmacro/las/')
        self.las_downloadpath = os.path.join(self.now_dir, 'data/mesmacro/las/')
    def read_outlook(self):
        print('Outlook 프로그램에서 "허용"창이 떴는 지 확인하고 허용하기를 눌러주세요.')
        outlook = Outlook(self.filename, self.outlook_downloadpath, self.date_from, self.date_end)
        lotid, moduleid = outlook.read_mail()
        print(f'outlook result lotid: {lotid}')
        print(f'outlook result moduleid: {moduleid}')
    def get_data_from_gmes(self):
        moduleid_file_path = os.path.join(self.outlook_downloadpath,f'{self.filename}생산모듈ID 모음.txt')
        moduleid = ""
        try:
            with open(moduleid_file_path, 'r') as r:
                moduleid_list = r.readlines()

            for m in moduleid_list:
                moduleid += m
        except:
            print(f'[Error] {moduleid_file_path}를 찾을 수 없습니다. 생산모듈ID를 Outlook에서 다운로드 받았는 지 확인하십시오.')
        #def __init__(self, moduleid, imagepath, querypath, filename):
        gmes = MES(moduleid, self.gmes_imagepath, self.gmes_downloadpath, f'{self.filename}GMES.csv')
    def get_data_from_las(self):
        path = f'{self.las_downloadpath}{self.filename}'
        FolderExists(path)

        lotid_file_path = os.path.join(self.outlook_downloadpath, f'{self.filename}Lot 모음.txt')
        lotid = ""
        try:
            with open(lotid_file_path, 'r') as r:
                lot_list = r.readlines()

            for l in lot_list:
                lotid += l
        except:
            print(f'[Error] {lotid_file_path}를 찾을 수 없습니다. Lot ID를 Outlook에서 다운로드 받았는 지 확인하십시오.')

        # def __init__(self, date_from, date_to, lotid, imagepath, downloadpath, filename):
        date_from = self.date_from.strftime('%Y-%m-%d')
        date_end = self.date_end + datetime.timedelta(days=1)
        date_end = date_end.strftime('%Y-%m-%d')

        las = LAS(date_from, date_end, lotid, self.las_imagepath, path, f'/{self.filename}LAS_Image.txt')
    def find_data_from_emptydata(self):
        # mes macro 폴더
        path_gmes = f'{self.gmes_downloadpath}'
        filename_mes = f'{self.filename}GMES.csv'
        path_las = f'{self.las_downloadpath}{self.filename}/'
        filename_las_image = f'{self.filename}LAS_Image.txt'

        empty = EMPTY(self.filename, filename_mes, path_gmes, path_las, filename_las_image)
        empty.run()
    def check_program(self):
        import subprocess
        import os
        windows_user_name = os.path.expanduser('~')
        p = Process()
        check_outlook, check_mes, check_las = p.check_program_on()
        if not check_outlook:
            print('[Error] OUTLOOK 프로그램 실행 후 다시 시도하세요.')
        if not check_mes:
            print('[Error] MES 프로그램 실행 후 다시 시도하세요.')
            subprocess.call('C:/Users/jylee/Desktop/GMES(JH-KG).appref-ms', shell=True)
            # subprocess.call([sys.executable,f'C:/Users/jylee/Desktop/GMES(JH-KG).appref-ms'])
            # subprocess.Popen(f'C:/Users/{windows_user_name}/Desktop/GMES(JH-KG).appref-ms')
        if not check_las:
            print('LAS 프로그램이을 실행하고 있습니다.')
            subprocess.run(f'C:/Users/{windows_user_name}/AppData/Local/Jahwa_LAS_MAIN_MainShell/app-1.0.37/Jahwa LAS.exe')
            time.sleep(5)
    def check_process(self):
        import psutil
        mes = True
        las = True
        for process in psutil.process_iter():
            if 'Jahwa LAS.exe' in process.name():
                print('las 실행 중')
                las = False
            if 'LGIT.GMES.SFU.MainFrame.exe' in process.name():
                print('mes 실행 중')
                mes = False
        if mes or las:
            print('mes, las 프로그램 실행 후 다시 시도 하세요')
            return False
        else:
            return True



class MousePos(QObject):
    pos = pyqtSignal(int, int)
    flag = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        import pyautogui as pag
        self.pag = pag
    def position(self):
        while True:
            x = self.pag.position().x
            y = self.pag.position().y
            self.pos.emit(x, y)
            time.sleep(0.05)

class MyButton(QPushButton):
    def __init__(self, pixmap=None, parent=None):
        super().__init__(parent)
        self.m_pixmap = pixmap

    def setPixmap(self, pixmap):
        pixmap = pixmap.scaledToWidth(20)
        self.m_pixmap = pixmap


    def sizeHint(self):
        parentHint = super().sizeHint()
        pixmap_width = self.m_pixmap.width() if self.m_pixmap else 0
        pixmap_height = self.m_pixmap.height() if self.m_pixmap else 0
        return QSize(parentHint.width() + pixmap_width, max(parentHint.height(), pixmap_height))

    def paintEvent(self, event):
        super().paintEvent(event)

        if self.m_pixmap:
            pixmap_rect = self.icon().pixmap(self.size())  # QPixmap을 현재 버튼의 크기에 맞게 조정
            painter = QPainter(self)
            painter.drawPixmap(0, 0, pixmap_rect)

    def setTextCentered(self, text):
        self.setText(text)
        self.setStyleSheet('text-align: center;')

class MainWindowStyles(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_style()
    def ui_style(self):
        print('load style')
        thema = 'dark'  # 'white' u"background: rgb(255, 192, 203)"
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


if __name__ == "__main__":
    import sys
    import traceback
    def my_exception_hook(error_exctype, error_value, error_traceback):
        # Print the error and traceback
        # print(error_exctype, error_value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(error_exctype, error_value, error_traceback)
        # sys.exit(1)
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook
    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


