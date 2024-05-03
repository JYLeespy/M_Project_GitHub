from _library.functions.func_nowdirectory import get_now_dir
from _library.functions.func_foldermake import FolderExists
from _library.functions.func_json import read_json

# MES 누락 Macro 관련 Import
from _library.mesmacro.mesmacro_outlook import Outlook
from _library.mesmacro.mesmacro_check import Process
from _library.mesmacro.mesmacro_MES import MES
from _library.mesmacro.mesmacro_LAS import LAS
from _library.mesmacro.mesmacro_find import EMPTY


# MES 누락 Macro 관련 Import
from _library.ng_image.ngimage_MES import NID_MES
from _library.ng_image.ngimage_LAS import NID_LAS
from _library.ng_image.ngimage_Excel_Report import NID_REPORT

import datetime
import os
import time


'''
GBC_40V	 Handler
GBD_40V	 Grease Dispenser #1
GBB_40V	 Ball Mount #1
GBA_40V	 X-Stage Attach
GBD_41V	 Grease Dispenser #2
GBB_41V	 Ball Mount #2
GBA_41V	 Y-Stage Attach
RCA_40V	 Z-Stopper Attach
RCD_40V	 Epoxy Dispenser #1
RCD_41V	 Epoxy Dispenser #2
RCI_40V	 UV Cure
'''
def my_console():
    json_read = read_json("settings.json")
    console = json_read['Console']
    cols = console['cols']
    lines = console['lines']
    os.system(f'mode con: cols={cols} lines={lines}')

    font_color = console['font_color']
    background_color = console['background_color']

    os_colors = {'black':'0',
                 'blue':'1',
                 'green':'2',
                 'turquoise':'3',
                 'red':'4',
                 'purple':'5',
                 'yellow':'6',
                 'white':'7',
                 'gray':'8',
                 'light-blue':'9',
                 'light-green':'A',
                 'light-turquoise':'B',
                 'light-red':'C',
                 'light-purple':'D',
                 'light-yellow':'E',
                 'light-white':'F'
    }
    try:
        os.system(f'color {os_colors[background_color]}{os_colors[font_color]}')
    except:
        print('색상정보를 불러오는 데 실패했습니다.')
        pass

class MACRO:
    def __init__(self):
        try:
            my_console()
        except:
            print('settings.json 파일을 확인 중 문제가 발생하였습니다.')

        self.now_dir = get_now_dir()
        print(f'now_dir : {self.now_dir}')
        self.mesmacro_paths()
        self.nid_paths()
        self.options = '''
▶ 콘솔 사이즈 : settings.json 파일에서 수정 가능
cols : 가로 / lines : 세로

▶ 설정 가능한 색상 목록 : settings.json 파일에서 수정 가능 (배경, 글자색)
black / blue / green / turquoise / red / purple / yellow / white / gray /
light-blue / light-green / light-turquoise / light-red / light-purple / light-yellow / light-white
'''
        self.history ='''
2024.03.22 - LAS 이미지 다운로드 방식 변경 업데이트
           - 기존대비 다운로드 소요시간 50% 이상 감소
'''
        self.howto ='''
## 해당 프로그램에서 사용하는 명령어 모음, [   ] 안의 명령어 입력으로 프로그램 실행  (/?)
▶UI Option(색깔 변경법)
 [/option] or [/옵션]
▶Update History
 [/history] or [/version]
###############################################################################################
▶MES 누락 데이터 찾기 --------------------------------------------------------------------------
 [/outlook] 아웃룩에서 입력한 날짜, 기간동안 MES 누락 메일 읽고 Lot ID와 생산모듈ID 다운로드
 [/MES] 아웃룩에서 다운받은 생산모듈ID를 기반으로 누락된 데이터 정리된 파일 다운로드(키보드&마우스 매크로)
 [/LAS] 아웃룩에서 다운받은 LOT ID를 기반으로 로그파일 다운로드(키보드&마우스 매크로)
 [/MES누락찾기] outlook mes las 데이터 로그파일에서 누락된 데이터 찾기 수동 실행
 [/MES누락자동] 상기 모든 과정을 자동으로 진행 (Outlook, MES, LAS 프로그램을 반드시 켜 놔야함)
▶Daily 불량 이미지 다운로드 ----------------------------------------------------------------------
 [/불량데이터조회] MES에서 입력한 날짜의 불량 데이터를 조회합니다.
 [/불량이미지다운] LAS에서 입력한 날짜의 불량 이미지를 다운로드 합니다.
 [/리포트생성]    MES, LAS에서 받은 정보와 이미지로 Excel Report를 생성합니다.
 [/불량이미지자동] 입력한 날짜의 불량 데이터를 MES에서 조회한 후 LAS에서 자동 다운로드 합니다. 
 --------------------------------------------------------------------------------------------
  [/종료]
###############################################################################################
'''
# [/불량데이터조회2] MES에서 입력한 날짜의 불량 데이터를 조회합니다. (기간이 길 경우 1일 단위로 진행함 24/1/1 부터 + 일수 )

# '''
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃    ┎───────┐┎──┐   ┎──┐   ┎──┐       ┎─────────┐┎─────────┐  ┃
# ┃    ┗━━━━┓  │┃  │   ┃  │   ┃  │       ┃  ┍━━━━━━┙┃  ┍━━━━━━┙  ┃
# ┃         ┃  │┃  │   ┃  │   ┃  │       ┃  │       ┃  │         ┃
# ┃         ┃  │┃  └───┚  │   ┃  │       ┃  └──────┐┃  └──────┐  ┃
# ┃  ┎──┐   ┃  │┗━━━━━━┓  │   ┃  │       ┃  ┍━━━━━━┙┃  ┍━━━━━━┙  ┃
# ┃  ┃  │   ┃  │┎──┐   ┃  │   ┃  │       ┃  │       ┃  │         ┃
# ┃  ┃  └───┚  │┃  └───┚  │┎─┐┃  └──────┐┃  └──────┐┃  └──────┐  ┃
# ┃  ┗━━━━━━━━━┙┗━━━━━━━━━┙┗━┙┗━━━━━━━━━┙┗━━━━━━━━━┙┗━━━━━━━━━┙  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# '''
        # 1. Outlook MES LAS 켜져있는 지 확인하고 켠다.
        print('''
# n a m e : main.exe
# made by : jylee (jylee@jahwa.co.kr)
# d a t e : 2024-01-23
# update  : 2024-03-22
# version : 1

프로그램이 실행되었습니다''')
        print(self.howto)
        while True:
            info = '''
## 명령어를 입력하세요 (명령어보기 = /?).
'''
            print(info)
            r = self.commands(input())
            if r:
                break
    def commands(self, command):
        if command == '' or command[0] != '/':
            return
        elif command == '/?' or command == '/help':
            print(self.howto)
            return
        elif command == '/option' or command == '/옵션':
            print(self.options)
        elif command == '/history' or command == '/version':
            print(self.history)
        elif command == '/종료':
            return True

        else:
            self.setting_date()
            # self.check_program()
            # print('3초 후 실행됩니다.')
            # time.sleep(1)
            # print('2초 후 실행됩니다.')
            # time.sleep(1)
            # print('1초 후 실행됩니다.')
            # time.sleep(1)

            if command == '/outlook' or command == '/Outlook':
                self.read_outlook()
            elif command == '/MES' or command == '/mes':
                self.get_data_from_gmes()
            elif command == '/LAS' or command == '/las':
                self.get_data_from_las()
            elif command == '/MES누락찾기':
                self.find_data_from_emptydata()
            elif command == '/MES누락자동':
                self.read_outlook()
                self.get_data_from_gmes()
                self.get_data_from_las()
                self.find_data_from_emptydata()

            elif command == '/불량데이터조회':
                self.get_nglist_from_gmes()
            elif command == '/불량데이터조회2':
                self.get_nglist_from_gmes2()
            elif command == '/불량이미지다운':
                self.download_ngimage()
            elif command == '/리포트생성':
                self.make_report()
            elif command == '/불량이미지자동':
                self.get_nglist_from_gmes()
                self.download_ngimage()
                self.make_report()
            else:
                print('명령어를 확인 후 다시 시도하십시오.')
    def commandlist(self, command) -> bool:
        # self.check_program()
        self.command_dict = {'/outlook':self.read_outlook(),
                             '/Outlook':self.read_outlook(),
                             '/MES':self.get_data_from_gmes(),
                             '/mes':self.get_data_from_gmes(),
                             '/LAS':self.get_data_from_las(),
                             '/las':self.get_data_from_las(),
                             '/MES누락찾기':self.find_data_from_emptydata(),
                             '/MES누락자동':self.auto('/MES누락자동'),
                             '/불량데이터조회':self.get_nglist_from_gmes(),
                             '/불량이미지다운':self.download_ngimage(),
                             '/불량이미지자동':self.auto('/불량이미지자동')}
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
    # MES 누락 찾기
    def mesmacro_paths(self):
        self.outlook_downloadpath = os.path.join(self.now_dir,'_data/Outlook Data/')
        self.gmes_imagepath = os.path.join(self.now_dir,'_images/mesmacro/mes/')
        self.gmes_downloadpath = os.path.join(self.now_dir,'_data/mesmacro/mes/')
        self.las_imagepath = os.path.join(self.now_dir, '_images/mesmacro/las/')
        self.las_downloadpath = os.path.join(self.now_dir, '_data/mesmacro/las/')
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

    # MES NG 이미지 다운로딩
    def nid_paths(self):
        # nid = ng image download
        #self.outlook_downloadpath = os.path.join(self.now_dir,'_data/Outlook Data/')
        self.nid_image_path = os.path.join(self.now_dir, '_images/ngimagedownload/')
        self.nid_download_path = os.path.join(self.now_dir,'_download/')
    def get_nglist_from_gmes(self):
        date_from = self.date_from.strftime('%Y-%m-%d')
        date_to = self.date_end.strftime('%Y-%m-%d')
        mes_ng = NID_MES(self.nid_image_path, self.nid_download_path, date_from, date_to)

    def get_nglist_from_gmes2(self):
        date1 = self.date_from
        for i in range(self.period):
            date_from = date1 + datetime.timedelta(days=i)
            date_end = date1 + datetime.timedelta(days=i+1)
            date_from = date_from.strftime('%Y-%m-%d')
            date_to = date_end.strftime('%Y-%m-%d')
            mes_ng = NID_MES(self.nid_image_path, self.nid_download_path, date_from, date_to)
    # def check_process(self):
    #     import psutil
    #     mes = True
    #     las = True
    #     for process in psutil.process_iter():
    #         if 'Jahwa LAS.exe' in process.name():
    #             print('las 실행 중')
    #             las = False
    #         if 'LGIT.GMES.SFU.MainFrame.exe' in process.name():
    #             print('mes 실행 중')
    #             mes = False
    #     if mes or las:
    #         print('mes, las 프로그램 실행 후 다시 시도 하세요')
    #         return False
    #     else:
    #         return True
    def download_ngimage(self):
        date_from = self.date_from.strftime('%Y-%m-%d')
        date_to = self.date_end.strftime('%Y-%m-%d')
        filename = f'{self.nid_download_path}/{date_from}_{date_to}/{date_from} 0820_{date_to} 0820 NG List Result.csv'
        downloadpath = f'{self.nid_download_path}/{date_from}_{date_to}'
        las_ng = NID_LAS(self.nid_image_path, filename, downloadpath, self.date_from, self.date_end)

    def make_report(self):
        date_from = self.date_from.strftime('%Y-%m-%d')
        date_to = self.date_end.strftime('%Y-%m-%d')
        path = f'{self.nid_download_path}/{date_from}_{date_to}'
        log_filename = f'{self.nid_download_path}/{date_from}_{date_to}/{date_from} 0820_{date_to} 0820 NG List Result.csv'
        base_filename = f'{self.nid_download_path}/기본양식파일.xlsm'
        report_savepath = f'{self.nid_download_path}/{date_from}_{date_to}/{date_from} 0820_{date_to} 0820 NG REPORT.xlsm'
        las_ng = NID_REPORT(path, base_filename, log_filename, report_savepath)
MACRO()

#
#
# if __name__ == "__main__":
#     import sys
#     def my_exception_hook(error_exctype, error_value, error_traceback):
#         # Print the error and traceback
#         # print(error_exctype, error_value, traceback)
#         # Call the normal Exception hook after
#         sys._excepthook(error_exctype, error_value, error_traceback)
#         # sys.exit(1)
#     # Back up the reference to the exceptionhook
#     sys._excepthook = sys.excepthook
#
#     # Set the exception hook to our wrapping function
#     sys.excepthook = my_exception_hook
#
#     app = MES_MACRO()
#
#     app.exec_()