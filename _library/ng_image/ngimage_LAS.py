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
            self.date_from = datetime.datetime(2024, 3, 28)
            self.date_to = datetime.datetime(2024, 3, 29)
            date_from = self.date_from.strftime('%Y-%m-%d')
            date_to = self.date_to.strftime('%Y-%m-%d')
            # self.filename = f'D:/ProgramData/_project/M_Project/_download/{date_from}_{date_to}/{date_from} 0820_{date_to} 0820 NG List Result.csv'
            self.filename = f'D:/ProgramData/새 폴더/2024-03-28_2024-03-29/2024-03-28 0820_2024-03-29 0820 NG List Result.csv'
            self.downloadpath = "D:/ProgramData/새 폴더/2024-03-28_2024-03-29/"

        else:
            self.imagepath = imagepath
            self.date_from = date_from
            self.date_to = date_to
            self.filename = filename
            self.downloadpath = downloadpath


        self.downloadpath_log = f'{self.downloadpath}/log'
        self.count_dict = {}
        # Program Settings ###########
        self.processCheck("[LAS - 초기설정] 1. 프로그램 체크")
        self.active_window("[LAS - 초기설정] 2. 프로그램 창 열기")
        self.read_file("[LAS - 초기설정] 3. 정리된 불량데이터파일 열기")

        # LAS 로그파일 조회
        self.las_open_log_tab("[LAS - 초기설정] 3. 로그파일조회 열기")
        if not self.logfile_exists:
            self.las_options_settings("[LAS - 초기설정(공통)] 4. 날짜 및 공정 셋팅")
            self.las_downloadpath_settings(self.downloadpath_log,"[LAS - 초기설정(공통)] 5. 다운로드 경로 선택")
            self.las_log_download("[LAS - 실행] 6. 로그 다운로드 시퀀스")
            # 로그 다운로드 후 파일 정리 시퀀스
            self.las_logfile_merge("[LAS - 실행] 7. 로그 파일 필요한 데이터만 정리")
        self.las_logfile_summary_to_dict("[LAS - 실행] 8. 로그 파일 요약한 데이터 Dict로 정리")
        self.las_empty_log_attach("[LAS - 실행] 8. Query 빈 데이터 채워넣기")

        # LAS 이미지파일 조회
        self.read_file("[LAS - 초기설정(공통)] 7. 정리된 불량데이터파일 열기")
        self.las_open_image_tab("[LAS - 초기설정] 9. 이미지파일조회 열기")

        self.las_options_settings("[LAS - 초기설정(공통)] 10. 날짜 및 공정 셋팅")
        self.las_downloadpath_settings(self.downloadpath, "[LAS - 초기설정(공통)] 11. 다운로드 경로 선택")
        # ###################################################################
        self.las_search("main","[LAS - 실행] 12. 이미지 다운로드 시퀀스 (메인자재)")
        self.las_search("sub","[LAS - 실행] 13. 이미지 다운로드 시퀀스 (부자재)")

        self.categorization("main","[LAS] 14. 파일 분류 시작 (메인자재 이미지)")
        self.categorization("sub","[LAS] 15. 파일 분류 시작 (부자재 이미지)")
        self.las_finish("[LAS] 16. 파일 분류가 완료됐습니다.")

    def str_strip(self, text):
        text = text.lstrip()
        return text.rstrip()

    def las_make_folders(self, mc, oisid, ngname) -> str:
        path = f'{self.downloadpath}/#{mc[-1]}/{ngname}/{oisid}'
        FolderExists(path)
        return path
    def moveFile(self, src, dst, filename):
        import shutil
        import os
        shutil.move(os.path.join(src, filename), os.path.join(dst, filename))

    #1 [LAS] 초기설정 - 프로그램 체크
    def processCheck(self, description):
        print(description)
        import getpass
        las = {'processname': 'Jahwa LAS.exe',
                'filename_for_run': f'C:/Users/{getpass.getuser()}/AppData/Local/Jahwa_LAS_MAIN_MainShell/Jahwa LAS.exe',
                'hwnd_name': "JLAS (Gumi) Ver.1.0.42"}
        process_check_run(las['processname'], las['filename_for_run'])
        hwnd = HWND(las['hwnd_name'])
        hwnd.windowResize()
    #2 [LAS] 초기설정 - 프로그램 창 열기
    def active_window(self, description):
        print(description)
        count = 0
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
            if count >= 5:
                self.km.move(30, 30)
                time.sleep(0.5)
            count += 1



    ##################################################################
    #공통 [LAS] 초기설정 - 정리된 불량데이터파일 열기
    def read_file(self, description):
        print(description)
        self.nglist = {}
        self.lotids = []
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

            if oisid == "모듈":
                pass
            else:
                self.lotids.append(lotid)
                self.nglist[oisid] = [mc, lotid, moduleid, ngname, z_mgz, z_tray, z_pocket, x_mgz, x_tray, x_pocket,
                                      y_id, y_mgz, y_tray, y_pocket, zs_mgz, zs_tray, zs_pocket, x_mlotid,
                                      zs_mlotid]
        # print(self.nglist)
    #공통 [LAS] 초기설정 - 날짜 및 공정 셋팅
    def las_options_settings(self, description):
        print(description)
        search_from = self.date_from - datetime.timedelta(days=1)
        search_to = self.date_to + datetime.timedelta(days=1)
        y1 = search_from.year
        m1 = search_from.month
        d1 = search_from.day

        y2 = search_to.year
        m2 = search_to.month
        d2 = search_to.day


        self.km.image('클릭', f'{self.imagepath}LAS-기간From.png', x_offset=60, delay=0.5)

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

        self.km.image('클릭', f'{self.imagepath}텍스트부분검색.png', delay=0.1)
        self.km.image('클릭', f'{self.imagepath}LAS-설비.png', x_offset=55, delay=0.5)
        self.km.image('클릭', f'{self.imagepath}LAS-SelectAll.png', x_offset=10, delay=0.5)

        self.km.hotkeys('end')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')
        self.km.hotkeys('pageup')

        for i in range(4):
            self.km.image('클릭', f'{self.imagepath}LAS-OIS공정1.png', x_offset=5, delay=0.1)
        self.km.image('클릭', f'{self.imagepath}LAS-OIS공정OK.png', delay=1)
    #공통 [LAS] 초기설정 - 다운로드 경로 설정
    def las_downloadpath_settings(self, downloadpath, description):
        print(description)
        # 다운로드 폴더 경로 선택 ###################################################################
        self.km.image('클릭', f'{self.imagepath}LAS-다운로드경로.png', delay=1.5)
        self.km.image('우클릭', f'{self.imagepath}LAS-다운로드경로주소창.png', x_offset=250, delay=0.5)
        self.km.keys('E')
        path = os.path.abspath(downloadpath)
        FolderExists(path)
        time.sleep(0.2)
        clipboard.copy(path)
        time.sleep(0.2)
        self.km.paste()
        self.km.hotkeys('return')
        self.km.image('클릭', f'{self.imagepath}LAS-다운로드폴더선택.png', delay=1)
    ##################################################################

    # 로그파일 로그파일 로그파일 로그파일 로그파일 로그파일 로그파일 로그파일 로그파일 로그파일 로그파일 로그파일 로그파일
    #3 [LAS] 초기설정 - 로그 파일 조회 열기
    def las_open_log_tab(self, description):
        print(description)
        files = ['XAT.txt', 'YAT.txt', 'ZAT.txt', 'UVI.txt']
        self.logfile_exists = True
        for filename in files:
            filepath = os.path.join(self.downloadpath_log, filename)
            if not os.path.exists(filepath):
                self.logfile_exists = False
                break
        if self.logfile_exists:
            print(f'[LAS] 해당 기간 내에 이미 다운로드 받은 LAS로그파일이 있습니다.')
            return
        self.km.image('클릭', f'{self.imagepath}LAS-상단메뉴-데이터.png', delay=0.1)
        self.km.hotkeys('tab')
        time.sleep(0.1)
        self.km.hotkeys('enter')
        self.km.hotkeys('enter')
    #4 [LAS] 실행 - 로그 파일 다운로드
    def las_log_download(self, description):
        print(description)

        self.km.image('클릭', f'{self.imagepath}LAS-Merge여부.png', delay=1)

        lotlist = set(self.lotids)
        lotno = ""
        for lotid in lotlist:
            lotno += lotid + "\n"

        self.copy_data(lotno)
        time.sleep(1)
        self.km.image('클릭', f'{self.imagepath}LAS-LotNo.png', x_offset=50, delay=0.1)
        self.km.selectAll()
        self.km.paste()
        time.sleep(0.5)
        self.km.image('클릭', f'{self.imagepath}LAS-조회.png', delay=3)
        print(f'[LAS - 실행] 로그 파일 조회 시작')
        while True:
            judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-로딩.png', limit=2)
            if not judge:
                time.sleep(1.5)
                judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-로딩.png', limit=1)
                if not judge:
                    break
            time.sleep(1)
        print(f'[LAS - 실행] 로그파일 조회 완료')

        self.km.image('클릭', f'{self.imagepath}LAS-결과전체선택.png', y_offset=50, delay=0.1)
        self.km.selectAll()
        self.km.image('클릭', f'{self.imagepath}LAS-저장.png', delay=3)
        print(f'[LAS - 실행] 로그파일 다운로드 시작')
        while True:
            judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-다운로드로딩.png', limit=2)
            if not judge:
                time.sleep(1.5)
                judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-다운로드로딩.png', limit=1)
                if not judge:
                    break
            time.sleep(1)
        print(f'[LAS - 실행] 로그파일 다운로드 완료)')
    #5 [LAS] 실행 - 로그 파일 정리
    def las_logfile_merge(self, description):
        print(description)
        las_logfilelist = os.listdir(self.downloadpath_log)
        for filename in las_logfilelist:
            merge_filename = ""
            if filename.find("XAT") != -1:
                merge_filename ="XAT.txt"
            elif filename.find("YAT") != -1:
                merge_filename = "YAT.txt"
            elif filename.find("ZAT") != -1:
                merge_filename = "ZAT.txt"
            elif filename.find("UVI") != -1:
                merge_filename = "UVI.txt"
            if merge_filename != "":
                logfile = os.path.join(self.downloadpath_log, filename)
                with open(logfile, 'r') as r:
                    readlines = r.readlines()
                temp_list = []
                for line in readlines:
                    split_datas = line.split(",")
                    oisid = split_datas[9]
                    if merge_filename == "UVI.txt":
                        ng_process = split_datas[18]
                        ng_code = split_datas[19]
                        ng_description = split_datas[20]
                        if ng_process == "" and ng_code == "" and ng_description == "":
                            continue
                        else:
                            newline = f'{oisid},{ng_process},{ng_code},{ng_description},\n'
                    else:
                        sub_mgz = split_datas[16]
                        sub_tray = split_datas[17]
                        sub_pocket = split_datas[18]
                        if merge_filename == "YAT.txt":
                            sub_module = split_datas[21]
                        else:
                            sub_module = ""
                        newline = f'{oisid},{sub_mgz},{sub_tray},{sub_pocket},{sub_module}\n'
                    temp_list.append(newline)
                logfile = os.path.join(self.downloadpath_log, merge_filename)
                with open(logfile, 'a') as w:
                    w.writelines(temp_list)

    #6 [LAS] 실행 - 로그 요약 파일 정리
    def las_logfile_summary_to_dict(self, description):
        print(description)
        self.moduleinfo_dict = {}
        logfiles = ['XAT', 'YAT', 'ZAT', 'UVI']
        self.x_dict = {}
        self.y_dict = {}
        self.zs_dict = {}
        self.uv_dict = {}
        for logfile in logfiles:
            filepath = os.path.join(self.downloadpath_log, f'{logfile}.txt')
            with open(filepath, 'r') as r:
                readlines = r.readlines()
            for line in readlines:
                split_datas = line.split(",")
                oisid = split_datas[0]
                if oisid == "Barcode" or "":
                    continue
                if logfile == 'XAT':
                    self.x_dict[oisid] = {'xmgz': split_datas[1], 'xtray': split_datas[2], 'xpocket': split_datas[3]}
                elif logfile == 'YAT':
                    self.y_dict[oisid] = {'ymgz': split_datas[1], 'ytray': split_datas[2], 'ypocket': split_datas[3],
                                          'ymodule': split_datas[4]}
                elif logfile == 'ZAT':
                    self.zs_dict[oisid] = {'zsmgz': split_datas[1], 'zstray': split_datas[2],
                                           'zspocket': split_datas[3]}
                elif logfile == 'UVI':
                    self.uv_dict[oisid] = {'mc': split_datas[1], 'ngcode': split_datas[2], 'ngname': split_datas[3]}

    #7 [LAS] 실행 - 로그 파일 빈 데이터 채우기
    def las_empty_log_attach(self, description):

        print(description)
        with open(self.filename, 'r', encoding='cp949') as r:
            readlines = r.readlines()
        self.subinfo_empty_dict = {}
        new_list = []
        for line in readlines:
            split_datas = line.split(",")
            if split_datas[0] == "생산 모듈":
                continue
            oisid = split_datas[5]

            xmgz = split_datas[12]
            xtray = split_datas[13]
            xpocket = split_datas[14]
            if xmgz == "":
                xmgz = self.submaterial_dict_return(oisid, 'X', 'xmgz')
            if xtray == "":
                xtray = self.submaterial_dict_return(oisid, 'X', 'xtray')
            if xpocket == "":
                xpocket = self.submaterial_dict_return(oisid, 'X', 'xpocket')

            ymodule = split_datas[15]
            ymgz = split_datas[17]
            ytray = split_datas[18]
            ypocket = split_datas[19]
            if ymodule == "":
                ymodule = self.submaterial_dict_return(oisid, 'Y', 'ymodule')
            if ymgz == "":
                ymgz = self.submaterial_dict_return(oisid, 'Y', 'ymgz')
            if ytray == "":
                ytray = self.submaterial_dict_return(oisid, 'Y', 'ytray')
            if ypocket == "":
                ypocket = self.submaterial_dict_return(oisid, 'Y', 'ypocket')

            zsmgz = split_datas[21]
            zstray = split_datas[22]
            zspocket = split_datas[23]
            if zsmgz == "":
                zsmgz = self.submaterial_dict_return(oisid, 'ZS', 'zsmgz')
            if zstray == "":
                zstray = self.submaterial_dict_return(oisid, 'ZS', 'zstray')
            if zspocket == "\n":
                zspocket = self.submaterial_dict_return(oisid, 'ZS', 'zspocket')

            new_line = split_datas
            new_line[12] = xmgz
            new_line[13] = xtray
            new_line[14] = xpocket
            new_line[15] = ymodule
            new_line[17] = ymgz
            new_line[18] = ytray
            new_line[19] = ypocket
            new_line[21] = zsmgz
            new_line[22] = zstray
            zspocket = zspocket.replace('\n','')
            new_line[23] = zspocket

            mc_code_dict = {'GBC_40V':'Handler',
                            'GBD_40V':'Grease Dispenser #1',
                            'GBB_40V':'Ball Mount #1',
                            'GBA_40V':'X-Stage Attach',
                            'GBD_41V':'Grease Dispenser #2',
                            'GBB_41V':'Ball Mount #2',
                            'GBA_41V':'Y-Stage Attach',
                            'RCA_40V':'Z-Stopper Attach',
                            'RCA_30V':'Z-Stopper Attach',
                            'RCD_40V':'Epoxy Dispenser #1',
                            'RCD_41V':'Epoxy Dispenser #2',
                            'RCI_40V':'UV Cure'}
            try:
                mc_code = mc_code_dict[self.submaterial_dict_return(oisid, 'UV', 'mc')]
            except:
                mc_code = self.submaterial_dict_return(oisid, 'UV', 'mc')

            new_line = new_line + [mc_code,self.submaterial_dict_return(oisid, 'UV', 'ngcode'),self.submaterial_dict_return(oisid, 'UV', 'ngname')+"\n"]

            line_data = ""
            for l in new_line:
                line_data += l + ","
            line_data = line_data[:-1]
            new_list.append(line_data)

        firstline = "생산 모듈,LOT ID,설비명,일자,예비용,모듈,판정,사유명,MGZ_Z,CARRIERID_Z,POCKET_Z,X_STAGE_PNP_CARRIER_MLOTID,MGZ_X,CARRIERID_X,POCKET_X,MODULE_Y,Y_STAGE_PNP_CARRIER_MLOTID,MGZ_Y,CARRIERID_Y,POCKET_Y,Z_STOPPER_PNP_CARRIER_MLOTID,MGZ_ZS,CARRIERID_ZS,POCKET_ZS,불량발생설비,불량코드,불량명\n"
        new_list.insert(0,firstline)
        with open(self.filename, 'w') as w:
            w.writelines(new_list)
    def submaterial_dict_return(self, oisid, category, submaterial):
        if category == 'X':
            sub_dict = self.x_dict
        elif category == 'Y':
            sub_dict = self.y_dict
        elif category == 'ZS':
            sub_dict = self.zs_dict
        elif category == 'UV':
            sub_dict = self.uv_dict
        else:
            return ""

        try:
            result = sub_dict[oisid][submaterial]
            return result.replace('\n','')
        except:
            return ""

    # 이미지파일 이미지파일 이미지파일 이미지파일 이미지파일 이미지파일 이미지파일 이미지파일 이미지파일 이미지파일 이미지파일
    #4 [LAS] 초기설정 - 이미지파일조회 열기
    def las_open_image_tab(self, description):
        print(description)
        self.km.image('클릭', f'{self.imagepath}LAS-상단메뉴-데이터.png', delay=0.1)
        self.km.hotkeys('tab')
        self.km.hotkeys('tab')
        time.sleep(0.1)
        self.km.hotkeys('enter')
        self.km.hotkeys('enter')
    #8 [LAS] 실행 - 불량 이미지 다운로드 (material : "main" or "sub")
    def las_search(self, material, discription):
        print(discription)
        # 메인 검색
        lotno = ""
        barcode = ""
        for module in self.nglist:
            try:
                mc = self.nglist[module][0]
                lotid = self.nglist[module][1]
                moduleid = self.nglist[module][2]
                ngname = self.nglist[module][3]
                z_mgz = self.nglist[module][4]
                z_tray = self.nglist[module][5]
                z_pocket = self.nglist[module][6]
                x_mgz = self.nglist[module][7]
                x_tray = self.nglist[module][8]
                x_pocket = self.nglist[module][9]
                y_id = self.nglist[module][10]
                y_mgz = self.nglist[module][11]
                y_tray = self.nglist[module][12]
                y_pocket = self.nglist[module][13]
                zs_mgz = self.nglist[module][14]
                zs_tray = self.nglist[module][15]
                zs_pocket = self.nglist[module][16]
                x_mlotid = self.nglist[module][17]
                zs_mlotid = self.nglist[module][18]
                if material == "main":
                    lotno += lotid + "\n"
                    barcode += module + "\n"
                elif material == "sub":
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
                    lotno += f'{x_mgz}\n{y_mgz}\n{zs_mgz}\n'
                    barcode += f'{x_info}\n{y_info}\n{zs_info}\n'
            except:
                pass


        self.copy_data(lotno)

        self.km.image('클릭', f'{self.imagepath}LAS-LotNo.png', x_offset=50, delay=0.1)
        self.km.selectAll()
        self.km.paste()
        time.sleep(0.5)

        self.copy_data(barcode)

        self.km.hotkeys('tab')
        self.km.selectAll()
        if material == "sub":
            self.km.paste()
            self.km.hotkeys('tab')
            self.km.selectAll()
            self.km.delete()
        if material == "main":
            self.km.delete()
            self.km.hotkeys('tab')
            self.km.selectAll()
            self.km.paste()
        time.sleep(0.5)
        self.km.image('클릭', f'{self.imagepath}LAS-조회.png', delay=3)
        print(f'[LAS - 실행] 이미지 조회 시작 ({material})')
        while True:
            judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-로딩.png', limit=2)
            if not judge:
                time.sleep(1.5)
                judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-로딩.png', limit=1)
                if not judge:
                    break
            time.sleep(1)
        print(f'[LAS - 실행] 이미지 조회 완료 ({material})')

        self.km.image('클릭', f'{self.imagepath}LAS-결과전체선택.png', y_offset=50, delay=0.1)
        self.km.selectAll()
        self.km.image('클릭', f'{self.imagepath}LAS-저장.png', delay=3)
        print(f'[LAS - 실행] 이미지 다운로드 시작 ({material})')
        while True:
            judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-다운로드로딩.png', limit=2)
            if not judge:
                time.sleep(1.5)
                judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-다운로드로딩.png', limit=1)
                if not judge:
                    break
            time.sleep(1)
        print(f'[LAS - 실행] 이미지 다운로드 완료 ({material})')
    #9 [LAS] 분류 - 불량 이미지 분류를 위한 count
    def categorization(self, material, discription):
        # 1. 폴더 내 파일 리스트 읽기.
        # 2. 지정한 폴더로 이동 ( 지정한 폴더가 없을 시 생성 )
        print(discription)
        imagefilelist = os.listdir(self.downloadpath)
        if material == 'sub':
            temp_dict = {}
            for module in self.nglist:
                try:
                    print(module, self.nglist[module])
                    mc = self.nglist[module][0]
                    moduleid = self.nglist[module][2]
                    ngname = self.nglist[module][3]
                    x_mgz = self.nglist[module][7]
                    x_tray = self.nglist[module][8]
                    x_pocket = self.nglist[module][9]
                    y_mgz = self.nglist[module][11]
                    y_tray = self.nglist[module][12]
                    y_pocket = self.nglist[module][13]
                    zs_mgz = self.nglist[module][14]
                    zs_tray = self.nglist[module][15]
                    zs_pocket = self.nglist[module][16]
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
                    temp_dict[x_info] = module
                    temp_dict[y_info] = module
                    temp_dict[zs_info] = module
                except:
                    pass

        for f in imagefilelist:
            filename_lotid = f.split("_")[0]
            if material == 'main' and filename_lotid[0] == "G":
                # 메인 이미지
                oisid = f.split("_")[3]
                mc = self.nglist[oisid][0][-3:]
                ngname = self.nglist[oisid][3]
                count = 0
                for n in self.nglist:
                    count += 1
                    if n == oisid:
                        self.count_dict[oisid] = count
                        break
                dst = self.las_make_folders(mc, oisid, ngname)
                self.moveFile(self.downloadpath, dst, f)
            elif material == 'sub' and filename_lotid[0] == "A":
                oisid = f'{temp_dict[f.split("_")[2]]}'
                mc = self.nglist[oisid][0][-3:]
                ngname = self.nglist[oisid][3]
                count = self.count_dict[oisid]
                dst = self.las_make_folders(mc, oisid, ngname)
                self.moveFile(self.downloadpath, dst, f)
    #10 [LAS] 결과 폴더 열기
    def las_finish(self, discription):
        print(discription)
        os.startfile(self.downloadpath)
    def copy_data(self, data):
        print(f'clipboard')
        # 초기화
        clipboard.copy("")
        clipboard.copy(data)
        time.sleep(1)
        clipboard_temp = clipboard.paste()
        clipboard_count = 0
        while True:
            if clipboard_temp != "":
                break
            else:
                time.sleep(0.1)
                clipboard_count += 1
            if clipboard_count == 10:
                clipboard_temp = clipboard.paste()
            elif clipboard_count == 11:
                clipboard.copy(data)
                time.sleep(1)
                clipboard_temp = clipboard.paste()

# a = NID_LAS()