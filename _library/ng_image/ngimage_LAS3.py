from _library.functions.func_pyautogui import KeyboardMouse
from _library.functions.func_foldermake import FolderExists
from _library.functions.func_progress import Progressbar
from _library.functions.func_processcheck import *
from _library.functions.func_hwnd import *
# from _library.functions.func_admin import *

import os

import cv2
import numpy as np
import time
import clipboard


import datetime


class NID_LAS:
    def __init__(self, imagepath="", filename="", downloadpath="", date_from="", date_to=""):
        # print(is_admin())
        self.km = KeyboardMouse()

        if imagepath == "" and filename == "" and date_from == "" and date_to == "":
            self.imagepath = "D://ProgramData//_project//M_Project//_images//LAS//"

            # Program Settings ###########
            # self.processCheck()
            # self.active_window()
            # self.las_closed_tab()
            # self.las_open_image_tab()
            self.date_from = datetime.datetime(2024, 3, 18)
            self.date_to = datetime.datetime(2024, 3, 19)
            self.downloadpath = "D:/새 폴더 (3)"
            # self.las_options_settings()
            ##############################
            date_from = self.date_from.strftime('%Y-%m-%d')
            date_to = self.date_to.strftime('%Y-%m-%d')
            self.filename = f'D:/ProgramData/Project/M_Project/_download/{date_from}_{date_to}/{date_from} 0820_{date_to} 0820 NG List Result.csv'
            self.read_file()
            self.las_image_search2()
            ##############################
        else:

            self.imagepath = imagepath
            self.downloadpath = downloadpath
            self.filename = filename
            self.date_from = date_from
            self.date_to = date_to
            self.read_file()
            self.las_check()
            self.las_imagesearch()        #14
            self.las_search()

    #1
    def processCheck(self):
        import getpass
        las = {'processname': 'Jahwa LAS.exe',
                'filename_for_run': f'C:/Users/{getpass.getuser()}/AppData/Local/Jahwa_LAS_MAIN_MainShell/Jahwa LAS.exe',
                'hwnd_name': "JLAS (Gumi) Ver.1.0.38"}
        process_check_run(las['processname'], las['filename_for_run'])
        hwnd = HWND(las['hwnd_name'])
        hwnd.windowResize()
    #2
    def active_window(self):
        print('[LAS] 0. 창 열기')
        while True:
            judge, x, y = self.km.image('이동', f'{self.imagepath}p_las.png')
            if judge:
                self.km.move(x, y)
                time.sleep(0.1)
                self.km.move(x+1, y+1)
                time.sleep(1)
                self.km.click(x, y-50)
                break
            else:
                time.sleep(0.5)
    #3
    def las_closed_tab(self):
        print('las_closed_tab')
        judge, x, y = self.km.image('이동', f'{self.imagepath}LAS-이미지파일조회닫기.png', delay=1, limit=1)
        if judge:
            self.km.click(x+50, y)
        judge, x, y = self.km.image('이동', f'{self.imagepath}LAS-이미지파일조회닫기.png', delay=1, limit=1)
        if judge:
            self.km.click(x + 50, y)
    #4
    def las_open_image_tab(self):
        judge, x, y = self.km.image('클릭', f'{self.imagepath}LAS-상단메뉴-데이터.png', delay=0.1)
        self.km.hotkeys('tab')
        self.km.hotkeys('tab')
        time.sleep(0.1)
        self.km.hotkeys('enter')
        self.km.hotkeys('enter')
    #5
    def las_options_settings(self):
        search_from = self.date_from - datetime.timedelta(days=1)
        search_to = self.date_to + datetime.timedelta(days=1)
        y1 = search_from.year
        m1 = search_from.month
        d1 = search_from.day

        y2 = search_to.year
        m2 = search_to.month
        d2 = search_to.day


        judge, x, y = self.km.image('클릭', f'{self.imagepath}LAS-기간From.png', x_offset=60, delay=0.5)

        for i in range(2):
            if i == 0:
                y = str(y1)
                m = str(m1)
                d = str(d1)
                t = "22"
            elif i == 1:
                self.km.hotkeys('tab')
                y = str(y2)
                m = str(m2)
                d = str(d2)
                t = "02"
            else:
                break
            self.km.keys(y)
            self.km.hotkeys('right')
            time.sleep(0.01)
            self.km.keys(m)
            self.km.hotkeys('right')
            time.sleep(0.01)
            self.km.keys(d)
            self.km.hotkeys('right')
            time.sleep(0.01)
            self.km.write(t)

        # 구분 - 3개월보관이미지
        self.km.hotkeys('tab')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')

        judge, x, y = self.km.image('클릭', f'{self.imagepath}텍스트부분검색.png', delay=0.1)
        judge, x, y = self.km.image('클릭', f'{self.imagepath}LAS-설비.png', x_offset=55, delay=0.5)
        judge, x, y = self.km.image('클릭', f'{self.imagepath}LAS-SelectAll.png', x_offset=10, delay=0.5)

        self.km.hotkeys('end')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')

        for i in range(4):
            judge, x, y = self.km.image('클릭', f'{self.imagepath}LAS-OIS공정1.png', x_offset=5, delay=0.1)
        judge, x, y = self.km.image('클릭', f'{self.imagepath}LAS-OIS공정OK.png', delay=1)

    def empty_data_check(self, text):
        # if text == "#N/A" or text == '0':
        #     return ""
        # else:
        return text
    def las_image_search(self):
        for oisid in self.nglist:
            mc = self.nglist[oisid][0]
            lotid = self.nglist[oisid][1]
            moduleid = self.nglist[oisid][2]
            ngname = self.nglist[oisid][3]
            z_mgz = self.empty_data_check(self.nglist[oisid][4])
            z_tray = self.empty_data_check(self.nglist[oisid][5])
            z_pocket = self.empty_data_check(self.nglist[oisid][6])
            x_mgz = self.empty_data_check(self.nglist[oisid][7])
            x_tray = self.empty_data_check(self.nglist[oisid][8])
            x_pocket = self.empty_data_check(self.nglist[oisid][9])
            y_id = self.empty_data_check(self.nglist[oisid][10])
            y_mgz = self.empty_data_check(self.nglist[oisid][11])
            y_tray = self.empty_data_check(self.nglist[oisid][12])
            y_pocket = self.empty_data_check(self.nglist[oisid][13])
            zs_mgz = self.empty_data_check(self.nglist[oisid][14])
            zs_tray = self.empty_data_check(self.nglist[oisid][15])
            zs_pocket = self.empty_data_check(self.nglist[oisid][16])
            x_mlotid = self.empty_data_check(self.nglist[oisid][17])
            zs_mlotid = self.empty_data_check(self.nglist[oisid][18])

            x_info = f'{x_tray}-00-2#{x_mgz}#{x_tray}#{x_pocket}#4#0-00PKRT-ALIG1-OK'
            y_info = f'{y_tray}-00-3#{y_mgz}#{y_tray}#{y_pocket}#BarcodeID#4#0-00PKRT-ALIG1-OK'
            if len(zs_pocket) == 1:
                zs_pocket = f'0{zs_pocket}'
            zs_info = f'{zs_tray}-{zs_pocket}-4#{zs_mgz}#{zs_tray}#{zs_pocket}#4#0-00PKRT-ALIG1-OK'

    def las_image_search2(self):
        lotid_ex = ""
        print('[NID] #16 las_search #################################################')
        print('\n')
        p = Progressbar()
        total = len(self.nglist)
        count = 0
        count_progress = 0
        lefttime = "예상 시간 계산 중..."
        p.run("다운로딩",0,total,lefttime)

        t = time.time()
        count_step = 0.2

        for i in self.nglist:
            oisid = i
            #Progress #1 ################################################
            count_progress += count_step
            p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')

            mc = self.nglist[oisid][0]
            lotid = self.nglist[oisid][1]
            moduleid = self.nglist[oisid][2]
            ngname = self.nglist[oisid][3]
            z_mgz = self.empty_data_check(self.nglist[oisid][4])
            z_tray = self.empty_data_check(self.nglist[oisid][5])
            z_pocket = self.empty_data_check(self.nglist[oisid][6])
            x_mgz = self.empty_data_check(self.nglist[oisid][7])
            x_tray = self.empty_data_check(self.nglist[oisid][8])
            x_pocket = self.empty_data_check(self.nglist[oisid][9])
            y_id = self.empty_data_check(self.nglist[oisid][10])
            y_mgz = self.empty_data_check(self.nglist[oisid][11])
            y_tray = self.empty_data_check(self.nglist[oisid][12])
            y_pocket = self.empty_data_check(self.nglist[oisid][13])
            zs_mgz = self.empty_data_check(self.nglist[oisid][14])
            zs_tray = self.empty_data_check(self.nglist[oisid][15])
            zs_pocket = self.empty_data_check(self.nglist[oisid][16])
            x_mlotid = self.empty_data_check(self.nglist[oisid][17])
            zs_mlotid = self.empty_data_check(self.nglist[oisid][18])

            x_info = f'{x_tray}-00-2#{x_mgz}#{x_tray}#{x_pocket}#4#0-00PKRT-ALIG1-OK'
            y_info = f'{y_tray}-00-3#{y_mgz}#{y_tray}#{y_pocket}#BarcodeID#4#0-00PKRT-ALIG1-OK'
            if len(zs_pocket) == 1:
                zs_pocket_2 = f'0{zs_pocket}'
            else:
                zs_pocket_2 = zs_pocket
            if int(zs_pocket) <= 30:
                head = "R"
            else:
                head = "L"
            zs_info = f'{zs_tray}-{zs_pocket_2}-4#{zs_mgz}#{zs_tray}#{zs_pocket}#4#0-00PKT{head}-ALIG1-OK'
            #print(f'{oisid} >> {self.nglist[i]}')
            ''
            'FJ5168-07-4#ABX91951K#FJ5168#7#4#0-00PKTR-ALIG1-OK'
            judge, lotno_x, lotno_y = self.km.image('이동', f'{self.imagepath}LAS-LotNo.png', x_offset=50, delay=0.1)

            # 다운로드 폴더 경로 선택 ###################################################################
            path = self.las_make_folders(mc, count, oisid, ngname)
            self.km.image('클릭', f'{self.imagepath}LAS-다운로드경로.png', delay=1.5)
            self.km.image('우클릭', f'{self.imagepath}LAS-다운로드경로주소창.png', x_offset=250, delay=0.1)
            self.km.keys('E')
            #Progress #4 ################################################
            count_progress += count_step
            p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')
            path = os.path.abspath(path)
            clipboard.copy(path)
            self.km.paste()
            self.km.hotkeys('return')
            self.km.image('클릭', f'{self.imagepath}LAS-다운로드폴더선택.png', delay=1)
            # 다운로드 폴더 경로 선택 ###################################################################

            for i in range(1, 2):
                #Lot No 검색
                # 1 일 때는 바코드로
                # 2 일 때는 부자재로
                clipboard.copy("")
                if i == 0:
                    lotno = lotid
                else:
                    lotno = f'{x_mgz}\n{y_mgz}\n{zs_mgz}'
                check_lotno = lotno.replace("\n","")
                if len(check_lotno) == 0:
                    continue
                print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>11 lotno : {lotno}  len(lotno) : {len(check_lotno)}')
                clipboard.copy(lotno)
                time.sleep(0.01)
                # for i in range(3):
                #     print(f'[1] {3-i}..............')
                #     time.sleep(1)
                self.km.click(lotno_x, lotno_y)
                self.km.selectAll()
                self.km.hotkeys('delete')
                self.km.paste()
                time.sleep(0.05)
                # for i in range(3):
                #     print(f'[1] {3-i}..............')
                #     time.sleep(1)
                if i == 0:
                    clipboard.copy(oisid)
                    self.km.hotkeys('tab')
                    self.km.selectAll()
                    self.km.hotkeys('delete')
                    self.km.hotkeys('tab')
                    self.km.selectAll()
                    self.km.paste()
                    print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>22 {oisid}')
                else:
                    infos = f'{x_info}\n{y_info}\n{zs_info}'
                    clipboard.copy(infos)
                    self.km.hotkeys('tab')
                    self.km.selectAll()
                    self.km.paste()
                    self.km.hotkeys('tab')
                    self.km.selectAll()
                    self.km.hotkeys('delete')
                    print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>33 {infos}')
                time.sleep(0.05)
                # for i in range(3):
                #     print(f'[1] {3-i}..............')
                #     time.sleep(1)
                #Progress #2 ################################################
                # count_progress += count_step
                # p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')

                self.km.image('클릭', f'{self.imagepath}LAS-조회.png', delay=0.5)

                while True:
                    judge, x, y = self.km.image('이동', f'{self.imagepath}LAS-로딩.png')
                    if not judge:
                        break
                        # judge, x, y = self.km.image('이동', f'{self.imagepath}LAS-로딩.png')
                        # if not judge:
                        #     time.sleep(1)
                    time.sleep(1)


                self.km.image('클릭', f'{self.imagepath}LAS-결과전체선택.png', y_offset=50, delay=0.1)
                self.km.selectAll()

                # #Progress #3 ################################################
                # count_progress += count_step
                # p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')

                while True:
                    try:
                        judge, x, y = self.km.image('이동', f'{self.imagepath}LAS-저장.png')
                    except:
                        pass
                    if judge:
                        self.km.click(x, y)
                        time.sleep(5)
                        break
                    else:
                        time.sleep(1)

                while True:
                    try:
                        judge, x, y = self.km.image('이동', f'{self.imagepath}LAS-로딩.png')
                    except:
                        pass
                    if not judge:
                        time.sleep(1)
                        break
                    else:
                        time.sleep(1)
                clipboard.copy("")

            count += 1

            #Progress #5 ################################################
            # during_time = time.time()-t
            # t = time.time()
            # count_progress += count_step
            # during_time_min = int(during_time * (total-count_progress)/60)
            # during_time_sec = int(during_time * (total-count_progress)%60)
            # lefttime = f'left {during_time_min}m {during_time_sec}s...'
            # p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')
    def str_strip(self, text):
        text = text.lstrip()
        return text.rstrip()
    def img_search(self, command, img, x_off, y_off, delay):
        ima_name = img
        img_path = os.path.abspath(f'{self.imagepath}{img}.png')
        np_img = np.fromfile(img_path, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        if command == '판단':
            try:
                x, y = self.km.find_image(img)
                #print(f'판단 : {x}, {y}')
                if x != 0 and y != 0:
                    self.km.move(x, y)
                    return True
                else:
                    self.km.move(10, 10)
                    return False
            except:
                self.km.move(10, 10)
                return False
        else:
            for i in range(4):
                try:
                    x, y = self.km.find_image(img)
                    #print(f'{ima_name} : {command} 후 {delay}s 대기')
                    if command == '클릭':
                        self.km.click(x + x_off, y + y_off)
                    elif command == '이동':
                        self.km.move(x + x_off, y + y_off)
                    elif command == '더블클릭':
                        self.km.doubleClick(x + x_off, y + y_off)
                    elif command == '우클릭':
                        self.km.rclick(x + x_off, y + y_off)
                    # elif command == '드래그':
                    #     self.km.drag()
                    time.sleep(delay)
                    return x, y
                except:
                    #print(f'{ima_name} 찾기 실패 재시도 ... {i}')
                    time.sleep(0.5)

    def read_file(self):
        self.nglist = {}
        with open(self.filename, encoding='cp949') as r:
            nglist = r.readlines()
        for line in nglist:
            str_line = self.str_strip(line)
            split_datas = str_line.split(',')
            oisid = split_datas[5]
            mc = split_datas[2]
            lotid = split_datas[1]
            moduleid = split_datas[0]
            ngname = split_datas[7]
            z_mgz = split_datas[8]
            z_tray = split_datas[9]
            z_pocket = split_datas[10]
            x_mgz = split_datas[12]
            x_tray = split_datas[13]
            x_pocket = split_datas[14]
            y_id = split_datas[15]
            y_mgz = split_datas[17]
            y_tray = split_datas[18]
            y_pocket = split_datas[19]
            zs_mgz = split_datas[21]
            zs_tray = split_datas[22]
            zs_pocket = split_datas[23]
            x_mlotid = split_datas[11]
            zs_mlotid = split_datas[20]

            if oisid =="모듈":
                pass
            else:
                self.nglist[oisid] = [mc, lotid, moduleid, ngname, z_mgz, z_tray, z_pocket, x_mgz, x_tray, x_pocket, y_id, y_mgz, y_tray, y_pocket, zs_mgz, zs_tray, zs_pocket, x_mlotid, zs_mlotid]
        # print(self.nglist)



    #14 LAS
    def las_check(self):
        print('[NID] #14 las_check #################################################')
        if not self.img_search('판단', 'LAS-기간From', x_off=0, y_off=0, delay=1):
            self.img_search('클릭', 'LAS-아이콘', x_off=0, y_off=0, delay=1)
            if not self.img_search('판단', 'LAS-기간From', x_off=0, y_off=0, delay=1):
                self.img_search('클릭', 'LAS-아이콘', x_off=0, y_off=0, delay=1)
                if not self.img_search('판단', 'LAS-기간From', x_off=0, y_off=0, delay=1):
                    self.img_search('클릭', 'LAS-아이콘', x_off=0, y_off=0, delay=1)
    #15
    def las_imagesearch(self):
        print('[NID] #15 las  #################################################')
        # 라스 프로그램 활성화 코드 추가
        #
        #

        try:
            self.img_search('클릭','LAS-이미지파일조회닫기',x_off=50, y_off=0, delay=1)
        except:
            pass
        self.img_search('클릭', 'LAS-이미지파일조회1', x_off=0, y_off=0, delay=0.5)
        x, y = self.img_search('이동', 'LAS-이미지파일조회2', x_off=0, y_off=0, delay=0.5)
        self.km.click(x+50,y)

        search_from = self.date_from - datetime.timedelta(days=1)
        search_to = self.date_to + datetime.timedelta(days=1)
        y1 = search_from.year
        m1 = search_from.month
        d1 = search_from.day

        y2 = search_to.year
        m2 = search_to.month
        d2 = search_to.day

        self.img_search('클릭', 'LAS-기간From', x_off=60, y_off=0, delay=0.5)

        for i in range(2):
            if i == 0:
                y = str(y1)
                m = str(m1)
                d = str(d1)
                t = "22"
            elif i == 1:
                self.km.hotkeys('tab')
                y = str(y2)
                m = str(m2)
                d = str(d2)
                t = "02"
            else:
                break
            self.km.keys(y)
            self.km.hotkeys('right')
            time.sleep(0.01)
            self.km.keys(m)
            self.km.hotkeys('right')
            time.sleep(0.01)
            self.km.keys(d)
            self.km.hotkeys('right')
            time.sleep(0.01)
            self.km.write(t)

        self.km.hotkeys('tab')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')

        self.img_search('클릭', 'LAS-설비', x_off=55, y_off=0, delay=0.5)
        self.img_search('클릭', 'LAS-SelectAll', x_off=-10, y_off=0, delay=0.5)

        self.km.hotkeys('end')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')

        for i in range(4):
            self.img_search('클릭', 'LAS-OIS공정1', x_off=-5, y_off=0, delay=0.1)
        self.img_search('클릭', 'LAS-OIS공정OK', x_off=0, y_off=0, delay=1)
    #16
    def las_search2(self):
        print('[NID] #16 las_search #################################################')
        p = Progressbar()
        total = len(self.nglist)
        count = 0
        count_progress = 0
        p.run("이미지파일 다운로드",0,total,"")
        lefttime = "남은 예상 시간을 계산 중 입니다........"

        oisid_list = []
        lotid_list = []
        oisids = ""
        lotids = ""
        for oisid in self.nglist:
            oisid_list.append(oisid)
            lotid_list.append(self.nglist[oisid][1])

        for oisid in oisid_list:
            oisids += oisid + "\n"

        lotid_list = set(lotid_list)
        for lotid in lotid_list:
            lotids += lotid + "\n"

        clipboard.copy(lotids)
        self.img_search('클릭', 'LAS-LotNo', x_off=50, y_off=0, delay=0.1)
        self.km.selectAll()
        self.km.paste()
        time.sleep(0.5)

        clipboard.copy(oisids)
        self.km.hotkeys('tab')
        self.km.hotkeys('tab')
        self.km.selectAll()
        self.km.paste()
        time.sleep(0.5)

        self.img_search('클릭', 'LAS-조회', x_off=0, y_off=0, delay=1)

        # t = time.time()
        # for i in self.nglist:
        #     oisid = i
        #     #Progress #1 ################################################
        #     count_progress += 0.25
        #     p.run("이미지파일 다운로드", count_progress, total, f'{oisid} ({count}/{total}) {lefttime}')
        #
        #     mc = self.nglist[oisid][0]
        #     lotid = self.nglist[oisid][1]
        #     moduleid = self.nglist[oisid][2]
        #     ngname = self.nglist[oisid][3]
        #     #print(f'{oisid} >> {self.nglist[i]}')
        #
        #     clipboard.copy(lotid)
        #     self.img_search('클릭', 'LAS-LotNo', x_off=50, y_off=0, delay=0.1)
        #     self.km.selectAll()
        #     self.km.paste()
        #     time.sleep(0.5)
        #
        #     clipboard.copy(oisid)
        #     self.km.hotkeys('tab')
        #     self.km.hotkeys('tab')
        #     self.km.selectAll()
        #     self.km.paste()
        #     time.sleep(0.5)
        #
        #     #Progress #2 ################################################
        #     count_progress += 0.25
        #     p.run("이미지파일 다운로드", count_progress, total, f'{oisid} ({count}/{total}) {lefttime}')
        #
        #     self.img_search('클릭', 'LAS-조회', x_off=0, y_off=0, delay=1)
        #
        #     while True:
        #         if self.img_search('판단', 'LAS-로딩', x_off=0, y_off=0, delay=0.5):
        #             pass
        #         else:
        #             time.sleep(1)
        #             break
        #
        #     self.img_search('클릭', 'LAS-결과전체선택', x_off=0, y_off=+50, delay=0.1)
        #     self.km.selectAll()
        #
        #     path = self.las_make_folders(mc, count, oisid, ngname)
        #     self.img_search('클릭', 'LAS-다운로드경로', x_off=0, y_off=0, delay=1.5)
        #     self.img_search('우클릭', 'LAS-다운로드경로주소창', x_off=250, y_off=0, delay=0.2)
        #     self.km.keys('E')
        #
        #     #Progress #3 ################################################
        #     count_progress += 0.25
        #     p.run("이미지파일 다운로드", count_progress, total, f'{oisid} ({count}/{total}) {lefttime}')
        #
        #     path = os.path.abspath(path)
        #     clipboard.copy(path)
        #     self.km.paste()
        #     self.km.hotkeys('return')
        #     self.img_search('클릭', 'LAS-다운로드폴더선택', x_off=0, y_off=0, delay=1)
        #     self.img_search('클릭', 'LAS-저장', x_off=0, y_off=0, delay=5)
        #
        #     while True:
        #         try:
        #             if self.img_search('판단', 'LAS-로딩', x_off=0, y_off=0, delay=2):
        #                 pass
        #             else:
        #                 break
        #         except:
        #             time.sleep(1)
        #             if self.img_search('판단', 'LAS-로딩', x_off=0, y_off=0, delay=2):
        #                 pass
        #             else:
        #                 break
        #     time.sleep(0.2)
        #
        #     count += 1
        #
        #     #Progress #4 ################################################
        #     during_time = time.time()-t
        #     t = time.time()
        #     count_progress += 0.25
        #     during_time_min = int(during_time * (total-count_progress)/60)
        #     during_time_sec = int(during_time * (total-count_progress)%60)
        #     lefttime = f'{during_time_min}분 {during_time_sec}초 남았습니다.'
        #     p.run("이미지파일 다운로드", count_progress, total, f'{oisid} ({count}/{total}) {lefttime}')
    def las_search(self):
        lotid_ex = ""
        print('[NID] #16 las_search #################################################')
        print('\n')
        p = Progressbar()
        total = len(self.nglist)
        count = 0
        count_progress = 0
        lefttime = "예상 시간 계산 중..."
        p.run("다운로딩",0,total,lefttime)

        t = time.time()
        count_step = 0.2

        for i in self.nglist:
            oisid = i
            #Progress #1 ################################################
            count_progress += count_step
            p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')

            mc = self.nglist[oisid][0]
            lotid = self.nglist[oisid][1]
            moduleid = self.nglist[oisid][2]
            ngname = self.nglist[oisid][3]
            #print(f'{oisid} >> {self.nglist[i]}')
            lotid_same = False
            if lotid == lotid_ex:
                lotid_same = True
            lotid_ex = lotid

            clipboard.copy(lotid)
            self.img_search('클릭', 'LAS-LotNo', x_off=50, y_off=0, delay=0.1)
            if not lotid_same:
                self.km.selectAll()
                self.km.paste()
                time.sleep(0.05)

            clipboard.copy(oisid)
            self.km.hotkeys('tab')
            self.km.hotkeys('tab')
            self.km.selectAll()
            self.km.paste()
            time.sleep(0.05)
            #Progress #2 ################################################
            count_progress += count_step
            p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')

            self.img_search('클릭', 'LAS-조회', x_off=0, y_off=0, delay=0.5)

            while True:
                if self.img_search('판단', 'LAS-로딩', x_off=0, y_off=0, delay=1):
                    pass
                else:
                    time.sleep(1)
                    break

            self.img_search('클릭', 'LAS-결과전체선택', x_off=0, y_off=+50, delay=0.1)
            self.km.selectAll()

            #Progress #3 ################################################
            count_progress += count_step
            p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')


            path = self.las_make_folders(mc, count, oisid, ngname)
            self.img_search('클릭', 'LAS-다운로드경로', x_off=0, y_off=0, delay=1.5)
            self.img_search('우클릭', 'LAS-다운로드경로주소창', x_off=250, y_off=0, delay=0.1)
            self.km.keys('E')

            #Progress #4 ################################################
            count_progress += count_step
            p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')

            path = os.path.abspath(path)
            clipboard.copy(path)
            self.km.paste()
            self.km.hotkeys('return')
            self.img_search('클릭', 'LAS-다운로드폴더선택', x_off=0, y_off=0, delay=1)

            while True:
                try:
                    self.img_search('클릭', 'LAS-저장', x_off=0, y_off=0, delay=5)
                    break
                except:
                    time.sleep(1)

            while True:
                try:
                    if self.img_search('판단', 'LAS-로딩', x_off=0, y_off=0, delay=2):
                        pass
                    else:
                        break
                except:
                    time.sleep(1)

            count += 1

            #Progress #5 ################################################
            during_time = time.time()-t
            t = time.time()
            count_progress += count_step
            during_time_min = int(during_time * (total-count_progress)/60)
            during_time_sec = int(during_time * (total-count_progress)%60)
            lefttime = f'left {during_time_min}m {during_time_sec}s...'
            p.run("다운로딩", count_progress, total, f'({count}/{total}) {lefttime}')

    def las_make_folders(self, mc, count, oisid, ngname) -> str:
        if "UserSelectedNG" in ngname:
            ngname = ngname.replace("UserSelectedNG","USN")
        path = f'{self.downloadpath}\#{mc[-1]}\{ngname}\{count}_{oisid}'

        # if len(path) >= 123:
        #     margin = 123-len(path)
        #     path = f'{self.downloadpath}\#{mc[-1]}\{ngname[0:-margin]}\{count}_{oisid}'
        FolderExists(path)
        return path

a = NID_LAS()