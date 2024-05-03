from _library.functions.func_pyautogui import KeyboardMouse
from _library.functions.func_foldermake import FolderExists
from _library.functions.func_processcheck import *
from _library.functions.func_hwnd import *

import os
import cv2
import numpy as np
import time
import clipboard
import datetime
import win32com.client
import random
class NID_MES:
    def __init__(self, imagepath = "", downloadpath = "", date_from = "", date_to = ""):
        self.km = KeyboardMouse()

        if imagepath == "" and downloadpath == "" and date_from == "" and date_to == "":
            print("TEST Mode")
            self.date_from = datetime.datetime(2024, 3, 30).strftime('%Y-%m-%d')
            self.date_to = datetime.datetime(2024, 3, 31).strftime('%Y-%m-%d')
            self.imagepath = "D:/ProgramData/_project/M_Project/_images/ngimagedownload/"
            self.downloadpath = "D:/ProgramData/_project/M_Project/_download"
        else:
            self.imagepath = imagepath
            self.downloadpath = downloadpath
            self.date_from = date_from
            self.date_to = date_to

        print("[MES] 시퀀스 시작")
        # 초기설정
        self.closeExcelFile()
        self.processCheck("[MES - 초기설정] 1. 프로그램 체크")
        self.active_window("[MES - 초기설정] 2. 프로그램 활성화")
        # 재공현황
        self.set_work_state("[MES - 재공현황] 3. 재공현황 설정")
        self.set_date("[MES - 재공현황] 4. 날짜 설정")
        self.set_process("[MES - 재공현황] 5. 공정 설정")
        self.set_no_ctq("[MES - 재공현황] 6. 폐기 미포함 설정")
        self.click_search("[MES - 재공현황] 7. 검색 클릭")
        self.click_ng("[MES - 재공현황] 8. 불량 클릭")
        self.click_ng_lotids("[MES - 재공현황] 9. 불량 복사 Lot ID 데이터만 정리")
        if not self.lotid_judge:
            # 복사한 Lot id가 없을 경우 종료
            return
        # 모듈정보조회
        self.set_module_info_search("[MES - 모듈정보조회] 10. 모듈정보조회 설정")
        self.search_lot("[MES - 모듈정보조회] 11. 불량 LOT 검색")
        self.search_lot_export("[MES - 모듈정보조회] 12. Export")

        # 모듈정보조회 엑셀 결과
        # 엑셀 열려있는 경우 닫기 추가
        self.excel_copy2("[MES - 모듈정보조회] 13. Export Excel Data Copy")
        self.excel_datas2("[MES - 모듈정보조회] 14. Export Excel Data 정리")
        self.get_nglist2("[MES - 모듈정보조회] 15. Export Excel Data 저장")

        # Stored Query
        while True:
            if self.n1_system_management("[MES - Stored Query 실행] 16. 매개변수정보등록"):
                break
        self.n2_system_storedQuery("[MES - Stored Query 실행] 17. Stored Query 실행")
        self.closeExcelFile()       #14

        # Stored Query
        self.data_merge("[MES - 데이터정리] 18. 모듈정보조회 & Stored Query 에서 받은 데이터 종합(NG정보 + 부자재정보)")
        print("[MES] 시퀀스 종료")
    def str_strip(self, text):
        text = text.lstrip()
        return text.rstrip()

    # [MES] 초기설정 1
    def processCheck(self, discription):
        print(discription)
        gmes = {'processname': 'LGIT.GMES.SFU.MainFrame.exe',
                'filename_for_run': 'GMES(JH-KG) - 복사본.appref-ms',
                'hwnd_name': "GMES SFU(J44)"}
        process_check_run(gmes['processname'], gmes['filename_for_run'])
        hwnd = HWND(gmes['hwnd_name'])
        hwnd.windowResize()
    # [MES] 초기설정 2
    def active_window(self, discription):
        print(discription)
        while True:
            judge, x, y = self.km.image('이동', f'{self.imagepath}p_mes.png')
            if judge:
                self.km.move(x, y)
                time.sleep(0.1)
                self.km.move(x+1, y+1)
                time.sleep(1)
                self.km.click(x, y-50)
                break
            else:
                time.sleep(0.5)

    # [MES] 재공현황 1
    def set_work_state(self, discription):
        print(discription)
        count = 0
        while True:
            count += 1
            judge, x, y = self.km.image('클릭', f'{self.imagepath}재공현황닫기1.png', limit=2)
            if judge:
                print("재공현황 닫기")
                self.km.click(x + 55, y)
                time.sleep(0.5)
                if count == 5:
                    break
            else:
                break
        self.km.image('클릭', f'{self.imagepath}상단메뉴-정보조회.png', delay=1)
        self.km.image('클릭', f'{self.imagepath}상단메뉴-재공현황.png', delay=1)
    # [MES] 재공현황 2
    def set_date(self, discription):
        print(discription)
        today = self.date_to
        yesterday = self.date_from
        self.km.image('클릭', f'{self.imagepath}재공현황-기간.png', x_offset=50, delay=0.5)
        self.km.selectAll()
        clipboard.copy(yesterday)
        time.sleep(0.1)
        self.km.paste()
        time.sleep(0.1)
        self.km.hotkeys('tab')
        self.km.hotkeys('tab')
        self.km.selectAll()
        clipboard.copy(today)
        time.sleep(0.1)
        self.km.paste()
        time.sleep(0.1)
    # [MES] 재공현황 3
    def set_process(self, discription):
        print(discription)
        self.km.image('클릭',f'{self.imagepath}재공현황-공정.png', x_offset=50, delay=1)
        self.km.image('클릭',f'{self.imagepath}재공현황-공정All.png', x_offset=-10, delay=1)

        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.km.image('클릭', f'{self.imagepath}재공현황-공정OIS.png', delay=1)
        self.km.hotkeys('enter')
        time.sleep(0.5)
    # [MES] 재공현황 4
    def set_no_ctq(self, discription):
        print(discription)
        self.km.image('클릭', f'{self.imagepath}재공현황-폐기.png', x_offset=50, delay=0.5)
        self.km.image('클릭', f'{self.imagepath}재공현황-폐기미포함.png', delay=0.5)
    # [MES] 재공현황 5
    def click_search(self, discription):
        print(discription)
        self.km.image('클릭', f'{self.imagepath}검색.png')
        time.sleep(1)
        while True:
            judge, x, y = self.km.image('이동', f'{self.imagepath}검색완료.png', delay=0.5)
            if judge: #self.km.image('판단', '검색완료', x_off=0, y_off=0, delay=0.5):
                break
            else:
                time.sleep(0.5)
    # [MES] 재공현황 6
    def click_ng(self, discription):
        print(discription)
        count = 0
        self.km.image('더블클릭', f'{self.imagepath}재공현황-불량수량.png', y_offset=30, delay=1)
        while True:
            judge, x, y = self.km.image('이동', f'{self.imagepath}검색완료.png', delay=0.5)
            if judge:
                break
            else:
                count += 1
                if count == 30:
                    self.km.image('더블클릭', f'{self.imagepath}재공현황-불량수량.png', y_offset=30, delay=1)
                    count = 0
    # [MES] 재공현황 7
    def click_ng_lotids(self, discription):
        print(discription)
        while True:
            judge, x, y = self.km.image('이동', f'{self.imagepath}재공현황-불량조회확인.png', delay=1)
            if judge:
                self.km.click(x, y)
                clipboard.copy("")
                self.km.selectAll()
                self.km.copy()
                break
            else:
                time.sleep(1)
        copydatas = ""
        while True:
            copydatas = clipboard.paste()
            if copydatas != "":
                break
            time.sleep(0.1)
        lot_ids = ""
        split_datas = copydatas.split("\n")
        for line in split_datas:
            lotid = line[24:39]
            if lotid[0] == "G":
                lot_ids += line[24:39] + "\n"
        clipboard.copy(lot_ids)
        time.sleep(0.5)
        print(f'[MES - 재공현황] 불량 발생 Lot ID : {lot_ids}')
        if len(lot_ids) < 9:
            self.lotid_judge = False
        else:
            self.lotid_judge = True

    # [MES] 모듈정보조회 1
    def set_module_info_search(self, discription):
        print(discription)
        self.km.image('클릭', f'{self.imagepath}모듈정보조회닫기1.png', x_offset=55, delay=1, limit=1)
        self.km.image('클릭', f'{self.imagepath}모듈정보조회닫기2.png', x_offset=55, delay=1, limit=1)

        count = 0
        while True:
            if count == 0:
                self.km.image('클릭', f'{self.imagepath}상단메뉴-생산실행.png', delay=2)
                self.km.image('클릭', f'{self.imagepath}상단메뉴-모듈정보조회.png', delay=1)
            judge, x, y = self.km.image('이동', f'{self.imagepath}모듈정보조회-확인.png', delay=1)
            if judge:
                break
            else:
                count+=1
                time.sleep(0.1)
            if count == 20:
                count = 0
    # [MES] 모듈정보조회 2
    def search_lot(self, discription):
        print(discription)
        self.km.image('클릭', f'{self.imagepath}모듈정보조회-LOT검색.png', x_offset=50, delay=1)
        self.km.selectAll()
        time.sleep(0.5)
        self.km.paste()
        time.sleep(0.8)
        self.click_search("[MES - 모듈정보조회] 검색 클릭")
        time.sleep(5)

    # [MES] 모듈정보조회 3
    def search_lot_export(self, discription):
        print(discription)
        self.km.image('클릭', f'{self.imagepath}모듈정보조회-Export.png', delay=1)
    # [MES] 모듈정보조회 4
    def search_export(self, discription):
        print(discription)
        while True:
            self.km.image('클릭', f'{self.imagepath}모듈정보조회-LOT검색.png', x_offset=50, delay=1)
            judge, x, y = self.km.image('이동', f'{self.imagepath}모듈정보조회-LOT검색.png', x_offset=50, delay=1)
            if judge:
                time.sleep(2)
                break
            else:
                time.sleep(1)
        self.km.image('클릭', f'{self.imagepath}모듈정보조회-Export.png', delay=1)
    # [MES] 모듈정보조회 5
    def excel_copy2(self, discription):
        print(discription)
        while True:
            judge, x, y = self.km.image('클릭', f'{self.imagepath}모듈정보조회-엑셀파일열림확인.png', x_offset=0, delay=1)
            if judge:
                break
            time.sleep(1)
        time.sleep(1)
        print("[MES - 모듈정보조회] Excel Data 확인 중...")
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = True
        sheet = excel.ActiveSheet
        if sheet.Name == 'dgModuleInfomation':
            cell_count = 1
            while True:
                # print(sheet.Cells(cell_count, 1).Value)
                if sheet.Cells(cell_count, 1).Value == None:
                    break
                cell_count += 1
            sheet.Range(f'A1:Q{cell_count}').Copy()
            self.excel_data = clipboard.paste()
            while True:
                if self.excel_data == "":
                    print("[MES] 복사 대기중....")
                    time.sleep(1)
                else:
                    print("[MES] 복사 완료")
                    break
    # [MES] 모듈정보조회 6
    def excel_datas2(self, discription):
        print(discription)
        self.nglist = {}
        datalist = self.excel_data.split('\n')
        for d in datalist:
            linelist = d.split('\t')
            if len(linelist) > 10:
                if len(linelist[10])>1:
                    moduleid = linelist[0]
                    oisid = linelist[7]
                    lotid = linelist[1]
                    ngname = linelist[10]
                    mc = linelist[4]
                    if 'CTQ' in ngname:
                        pass
                    else:
                        self.nglist[oisid] = [mc,lotid,moduleid,ngname]
    # [MES] 모듈정보조회 7
    def get_nglist2(self, discription):
        print(discription)
        # for i in self.nglist:
        #     print(f'{i} >> {self.nglist[i]}')
        ng_text = ''
        a = clipboard.paste()
        split_data = a.split('\n')
        for line in split_data:
            line_data = line.split('\t')
            try:
                product_moduleid = line_data[0]
                lotid = line_data[1]
                mc = line_data[4]
                trayid = line_data[5]
                pocketno = line_data[6]
                oisid = line_data[7]
                judge = line_data[8]
                ng_name = line_data[10]
                if ng_name == "" or "CTQ" in ng_name:
                    pass
                else:
                    ng_text += f'{product_moduleid},{lotid},{mc},{trayid},{pocketno},{oisid},{judge},{ng_name}\n'
            except:
                pass
        filepath = f'{self.downloadpath}/{self.date_from}_{self.date_to}'

        FolderExists(filepath)

        filename = f'{self.date_from} 0820_{self.date_to} 0820 NG List.csv'
        try:
            with open(filepath + '/' + filename, 'w', encoding='cp949') as w:
                w.write(ng_text)
        except PermissionError:
            print(f'[Error] {filename} 파일이 열려있습니다. 닫고 다시 시도하세요.')


        self.closeExcelFile()


    # [MES] 매개 변수 정보 등록
    def n1_system_management(self, discription):
        print(discription)
        self.km.image('클릭', f'{self.imagepath}topmenu_system2.png', delay=0.7)
        self.km.image('클릭', f'{self.imagepath}topmenu_menu2.png', delay=0.7)
        while True:
            self.km.image('클릭', f'{self.imagepath}menu2_worker.png', x_offset=50, delay=0.1)
            self.km.selectAll()
            time.sleep(0.1)
            self.km.delete()
            time.sleep(0.1)
            self.km.keys('K22206033')
            time.sleep(0.2)
            self.km.hotkeys('enter')
            time.sleep(0.2)
            judge, x_save, y_save = self.km.image('판단', f'{self.imagepath}menu2_save.png', delay=0.5, limit=2)
            if judge:
                break

        print('[MES] 6. 매개 변수 정보 등록 - 매개 변수 정보 입력(제목, 설명, 입력 정보)')
        n = random.randint(1000, 1000000)
        self.transaction_title = f'OIS_MODULEID_{n}'
        self.km.image('클릭', f'{self.imagepath}menu2_input.png', delay=0.5)
        self.km.hotkeys('tab')
        time.sleep(0.5)
        clipboard.copy(self.transaction_title)
        time.sleep(0.3)
        self.km.paste()
        time.sleep(0.2)
        self.km.hotkeys('tab')
        time.sleep(0.2)
        self.km.keys('OIS2')
        time.sleep(0.3)
        self.km.hotkeys('tab')
        time.sleep(0.2)

        self.moduleid = ''
        filepath = f'{self.downloadpath}/{self.date_from}_{self.date_to}'
        filename = f'{self.date_from} 0820_{self.date_to} 0820 NG List.csv'
        with open(filepath + '/' + filename, 'r') as r:
            readlines = r.readlines()
        for line in readlines:
            data = line.split(",")[5]
            if data != "" and data != "Read Fail" and data != "모듈":
                self.moduleid += data + "\n"

        clipboard.copy(self.moduleid)

        self.km.paste()
        while True:
            try:
                self.km.click(x_save, y_save)
                time.sleep(0.8)
                break
            except:
                time.sleep(1)
        self.km.image('클릭', f'{self.imagepath}menu2_save_ok.png', delay=0.5)
        self.km.image('클릭', f'{self.imagepath}menu2_save_ok.png', delay=0.5)
        self.km.image('클릭', f'{self.imagepath}menu2_period.png', x_offset = 100)
        self.km.hotkeys('tab')
        time.sleep(0.1)
        self.km.hotkeys('tab')
        time.sleep(0.1)

        print('[MES] 7. 매개 변수 정보 등록 - 제목 조회')
        self.km.selectAll()
        time.sleep(0.1)
        self.km.delete()
        time.sleep(0.1)
        clipboard.copy(self.transaction_title)
        self.km.paste()
        self.km.image('클릭', f'{self.imagepath}menu2_search.png', delay=1.5)

        clipboard.copy("")
        self.km.image('클릭', f'{self.imagepath}menu2_transactionid.png', y_offset=30)
        self.km.copy()
        temp = clipboard.paste()
        transaction_empty_count = 0
        while True:
            if temp != "":
                self.transaction_id = temp
                break
            time.sleep(0.1)
            transaction_empty_count += 1
            if transaction_empty_count >= 10:
                return False
        time.sleep(2)
        print(f'[MES] 8. 매개 변수 정보 등록 - TransActionID : {self.transaction_id}')
        return True
        # 2. 시스템관리 - Stored Query 실행
    # [MES] Stored Query
    def n2_system_storedQuery(self, discription):
        # self.transaction_id = '20240321085504454293'

        print(discription)
        self.km.image('클릭', f'{self.imagepath}topmenu_system2.png', delay=1)
        self.km.image('클릭', f'{self.imagepath}topmenu_menu1.png', delay=1)

        judge, x, y = self.km.image('클릭', f'{self.imagepath}menu1_queryname.png', x_offset=0, delay=0.5)
        self.km.click(x, y + 50)
        time.sleep(0.5)
        self.km.hotkeys('tab')
        self.km.selectAll()
        self.km.delete()
        search_name = 'OIS Assy 공정 불량 자재 정보 조회 (BY 멀티 OISID)'
        clipboard.copy(search_name)
        self.km.paste()

        self.km.image('클릭', f'{self.imagepath}menu2_search.png', delay=1)

        while True:
            judge, x, y = self.km.image('클릭', f'{self.imagepath}menu1_queryresult2.png', delay=0.1)
            if judge:
                self.km.click(x, y)
                time.sleep(0.1)
                self.km.click(x, y)
                time.sleep(1.5)


                judge2, x2, y2 = self.km.image('클릭', f'{self.imagepath}menu1_parameter.png', y_offset=25, delay=0.5)
                if judge2:
                    self.km.hotkeys('right')
                    break


        # self.transaction_id = "20240315132419473035"
        clipboard.copy(self.transaction_id)
        self.km.selectAll()
        self.km.delete()
        self.km.paste()

        self.km.image('클릭', f'{self.imagepath}menu1_run.png', delay=1)

        while True:
            judge, x, y = self.km.image('클릭', f'{self.imagepath}menu1_queryresult_wait.png', delay=1)
            if judge:
                time.sleep(3)
                break
        print(f'[MES] 10. Stored Query 실행 - CSV Export')
        self.km.image('클릭', f'{self.imagepath}menu1_csvexport.png', delay=1.8)
        self.km.image('클릭', f'{self.imagepath}menu1_csvexport_saveas.png', delay=0.8)

        # clipboard.copy(f'{self.downloadpath}\{self.date_from}_{self.date_to}')
        clipboard.copy(os.path.join(self.downloadpath,f'{self.date_from}_{self.date_to}'))
        time.sleep(0.3)
        self.km.selectAll()
        self.km.delete()
        self.km.paste()
        self.km.hotkeys('enter')
        time.sleep(0.5)
        filename = f'{self.date_from} 0820_{self.date_to} 0820 NG Stored Query.csv'
        clipboard.copy(filename)
        time.sleep(0.4)
        for i in range(6):
            self.km.hotkeys('tab')
            time.sleep(0.1)
        self.km.paste()
        time.sleep(0.1)
        self.km.hotkeys('enter')
        time.sleep(1)
        judge, x, y = self.km.image('클릭', f'{self.imagepath}menu1_saveas.png', delay=0.5)
        if judge:
            self.km.hotkeys('enter')
            time.sleep(1)
        self.km.image('클릭', f'{self.imagepath}menu1_cancel.png', delay=0.5)

    #14 Excel 종료
    def closeExcelFile(self):
        print('closeExcelFile')
        ps_name = 'EXCEL.EXE'
        # if process_list_print(ps_name):
        kill_process(ps_name)

    # [MES] 모듈정보조회 & Stored Query 데이터 합치기(ng 정보 + 부자재정보)
    def data_merge(self, discription):
        print(discription)
        self.moduleid = ''
        filepath = f'{self.downloadpath}/{self.date_from}_{self.date_to}'
        filename2 = f'{self.date_from} 0820_{self.date_to} 0820 NG Stored Query.csv'

        with open(os.path.join(filepath,filename2), 'r', encoding='UTF8') as r:
            readlines = r.readlines()
        dict_querydata = {}
        dict_querydata_time = {}

        for line in readlines:
            print(f'[NG List Query File] {line}')
            split_data = line.split(",")
            p_moduleid = split_data[0]
            if p_moduleid != "PROD_MODULEID":
                submaterials_data = ""
                for i in range(6,22):
                    submaterials_data += f'{split_data[i]},'
                submaterials_data = submaterials_data[0:-1]
                print(f'>> {p_moduleid} : {submaterials_data}')
                dict_querydata[p_moduleid] = submaterials_data

                dict_querydata_time[p_moduleid] = split_data[4]
                # print(split_data[4].split(" "))
                # dict_querydata_judge[p_moduleid] = split_data[5]

        filename1 = f'{self.date_from} 0820_{self.date_to} 0820 NG List.csv'
        filename3 = f'{self.date_from} 0820_{self.date_to} 0820 NG List Result.csv'
        new_line = ["생산 모듈,LOT ID,설비명,일자,예비용,모듈,판정,사유명,MGZ_Z,CARRIERID_Z,POCKET_Z,X_STAGE_PNP_CARRIER_MLOTID,MGZ_X,CARRIERID_X,POCKET_X,MODULE_Y,Y_STAGE_PNP_CARRIER_MLOTID,MGZ_Y,CARRIERID_Y,POCKET_Y,Z_STOPPER_PNP_CARRIER_MLOTID,MGZ_ZS,CARRIERID_ZS,POCKET_ZS\n"]

        with open(os.path.join(filepath,filename1), 'r') as r:
            readlines = r.readlines()
        for line in readlines:
            # print(f'[NG List NG List File] {line}')
            split_data = line.split(",")
            try:
                p_moduleid = split_data[0]
                lotid = split_data[1]
                mc = split_data[2]
                dt = dict_querydata_time[p_moduleid]
                temp_ = "NO DATA"
                oisid = split_data[5]
                judge = split_data[6]
                ngname = self.str_strip(split_data[7])

                file1_line = f'{p_moduleid},{lotid},{mc},{dt},{temp_},{oisid},{judge},{ngname}'
                #생산 모듈,LOT ID,설비명,일자,예비용,모듈,판정,사유명  , MGZ_Z,CARRIERID_Z,POCKET_Z,X_STAGE_PNP_CARRIER_MLOTID,MGZ_X,CARRIERID_X,POCKET_X,MODULE_Y,Y_STAGE_PNP_CARRIER_MLOTID,MGZ_Y,CARRIERID_Y,POCKET_Y,Z_STOPPER_PNP_CARRIER_MLOTID,MGZ_ZS,CARRIERID_ZS,POCKET_ZS\n
                new_line.append(f'{file1_line},{dict_querydata[p_moduleid]}')
            except KeyError:
                print("ERROR")
                pass

        with open(os.path.join(filepath,filename3), 'w') as w:
            w.writelines(new_line)
# a= NID_MES()



'''
    def img_search(self, command, img, x_off, y_off, delay):
        ima_name = img
        img_path = os.path.abspath(f'{self.imagepath}{img}.png')
        np_img = np.fromfile(img_path, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        if command == '판단':
            try:
                x, y = self.km.find_image(img)
                print(f'판단 : {x}, {y}')
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
                    print(f'{ima_name} : {command} 후 {delay}s 대기')
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
                    print(f'{ima_name} 찾기 실패 재시도 ... {i}')
                    time.sleep(0.5)

    #0 정보조회 - 재공현황
    def workreport(self):
        # x, y = self.img_search('이동', 'MES로고', x_off=0, y_off=0, delay=1)

        print('[NID] [NID] #0 정보조회 - 재공현황 #################################################')
        # if self.img_search('판단', 'MES로고', x_off=0, y_off=0, delay=1):
        # mes가 창 위로 안 나와 있을 때, mes 아이콘 클릭해서 켜기
        # get hnwd size > 최대 화면 일 때 아닐때 구분해서 최대화하기
        try:
            try:
                self.img_search('클릭','재공현황닫기1',x_off=55, y_off=0, delay=1)
            except:
                self.img_search('클릭','재공현황닫기2',x_off=55, y_off=0, delay=1)
        except:
            pass
        self.img_search('클릭','상단메뉴-정보조회', x_off=0, y_off=0, delay=1)
        self.img_search('클릭','상단메뉴-재공현황', x_off=0, y_off=0, delay=1)
    #1 재공현황 - 날짜변경
    def change_date(self):
        print('[NID] [NID] #1 재공현황 - 날짜변경 #################################################')
        today = self.date_to
        yesterday = self.date_from
        x, y = self.img_search('클릭','재공현황-기간', x_off=50, y_off=0, delay=0.5)
        self.km.selectAll()
        clipboard.copy(yesterday)
        time.sleep(0.1)
        self.km.paste()
        time.sleep(0.1)
        self.km.hotkeys('tab')
        self.km.hotkeys('tab')
        self.km.selectAll()
        clipboard.copy(today)
        time.sleep(0.1)
        self.km.paste()
        time.sleep(0.1)

    #3 재공현황 - 공정선택
    def change_process(self):
        print('[NID] [NID] #3 재공현황 - 공정선택 #################################################')
        x, y = self.img_search('클릭','재공현황-공정', x_off=50, y_off=0, delay=1)
        self.img_search('클릭','재공현황-공정All', x_off=-10, y_off=0, delay=1)

        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.img_search('클릭', '재공현황-공정OIS', x_off=0, y_off=0, delay=1)
        self.km.hotkeys('enter')
        time.sleep(0.5)
    #4 재공현황 - 폐기 미포함 선택
    def change_notincludectq(self):
        print('[NID] #4 재공현황 - 폐기 미포함 선택 #################################################')
        self.img_search('클릭', '재공현황-폐기', x_off=50, y_off=0, delay=0.5)
        self.img_search('클릭', '재공현황-폐기미포함', x_off=0, y_off=0, delay=0.5)
    #5 재공현황 - 검색
    def search_btn(self):
        print('[NID] #5 재공현황 - 검색 #################################################')
        self.img_search('클릭', '검색', x_off=0, y_off=0, delay=0)
        while True:
            if self.img_search('판단', '검색완료', x_off=0, y_off=0, delay=0.5):
                break
            else:
                pass
    #6 재공현황 - 불량 클릭
    def click_ngqty(self):
        print('[NID] #6 재공현황 - 불량 클릭 #################################################')
        count = 0
        self.img_search('더블클릭', '재공현황-불량수량', x_off=0, y_off=30, delay=2)
        while True:
            if self.img_search('판단', '검색완료', x_off=0, y_off=0, delay=1):
                break
            else:
                count += 1
                time.sleep(0.5)
                if count == 30:
                    self.img_search('더블클릭', '재공현황-불량수량', x_off=0, y_off=30, delay=1)
                    count = 0
    #7 재공현황 - 불량 랏ID 선택
    def click_lotids(self):
        print('[NID] #7 재공현황 - 불량 랏ID 선택 #################################################')
        self.img_search('클릭', '재공현황-결과LOTID', x_off=0, y_off=5, delay=1)

        clipboard.copy("")
        self.km.selectAll()
        self.km.copy()
        copydatas = ""
        while True:
            copydatas = clipboard.paste()
            if copydatas != "":
                break
            time.sleep(0.1)
        lot_ids = ""
        split_datas = copydatas.split("\n")
        for line in split_datas:
            lotid = line[24:39]
            if lotid[0] == "G":
                lot_ids += line[24:39] + "\n"
        clipboard.copy(lot_ids)
        time.sleep(0.5)

        if len(lot_ids) < 9:
            return False
        else:
            return True


        # self.km.keydown('shift')
        # while True:
        #     print('[NID] 반복')
        #     self.km.scroll(-500)
        #     self.km.scroll(-500)
        #     self.km.scroll(-500)
        #     self.km.scroll(-500)
        #     self.km.scroll(-500)
        #     self.km.scroll(-500)
        #     self.km.scroll(-500)
        # 
        #     if self.img_search('클릭', '재공현황-결과LOTID끝', x_off=0, y_off=-70, delay=1):
        #         self.km.keyup('shift')
        #         time.sleep(3)
        #         self.km.copy()
        #         self.lotlist = clipboard.paste()
        #         break
        #     else:
        #         time.sleep(0.5)

'''
'''

    #8 모듈정보조회 선택
    def find_module(self):
        print('[NID] [NID] #8 모듈정보조회 선택 #################################################')

        try:
            try:
                self.img_search('클릭','모듈정보조회닫기1',x_off=55, y_off=0, delay=1)
            except:
                self.img_search('클릭','모듈정보조회닫기2',x_off=55, y_off=0, delay=1)
        except:
            pass

        self.img_search('클릭', '상단메뉴-생산실행', x_off=0, y_off=0, delay=2)
        self.img_search('클릭', '상단메뉴-모듈정보조회', x_off=0, y_off=0, delay=1)
        count = 0
        while True:
            if self.img_search('판단', '모듈정보조회-확인', x_off=0, y_off=0, delay=1):
                break
            else:
                count+=1
                time.sleep(0.1)
            if count == 20:
                count = 0
                self.img_search('클릭', '상단메뉴-생산실행', x_off=0, y_off=0, delay=2)
                self.img_search('클릭', '상단메뉴-모듈정보조회', x_off=0, y_off=0, delay=1)
    #9 모듈정보조회 - LotID 입력 후 검색
    def find_lotids(self):
        print('[NID] #9 모듈정보조회 - LotID 입력 후 검색 #################################################')
        self.img_search('클릭', '모듈정보조회-LOT검색', x_off=50, y_off=0, delay=1)
        self.km.selectAll()
        time.sleep(0.5)
        self.km.paste()
        time.sleep(0.8)
        self.img_search('클릭', '검색', x_off=0, y_off=0, delay=0)
    #10 모듈정보조회 - 검색 완료 시 Export
    def result_find_module(self):
        print('[NID] #10 모듈정보조회 - 검색 완료 시 Export #################################################')
        while True:
            if self.img_search('판단', '검색완료', x_off=0, y_off=0, delay=1):
                time.sleep(5)
                break
            else:
                time.sleep(1)
        self.img_search('클릭', '모듈정보조회-Export', x_off=0, y_off=0, delay=1)



    #11 모듈정보조회 - 결과 엑셀파일 복사
    def excel_copy(self):
        print('[NID] #11 모듈정보조회 - 결과 엑셀파일 복사 #################################################')
        while True:
            if self.img_search('판단', '모듈정보조회-엑셀파일열림확인', x_off=0, y_off=0, delay=1):
                time.sleep(1)
                break
            else:
                time.sleep(1)

        self.img_search('클릭', '엑셀파일-셀선택', x_off=0, y_off=0, delay=1)
        clipboard.copy('')
        self.km.selectAll()
        time.sleep(0.5)
        self.km.copy()
        time.sleep(1)
        while True:
            self.excel_data = clipboard.paste()
            if len(self.excel_data) >= 5:
                time.sleep(0.5)
                break
            else:
                time.sleep(1)
    #12 모듈정보조회 - 결과 엑셀파일 정리
    def excel_datas(self):
        print('[NID] #12 모듈정보조회 - 결과 엑셀파일 정리 #################################################')
        self.nglist = {}
        datalist = self.excel_data.split('\n')
        for d in datalist:
            linelist = d.split('\t')
            if len(linelist) > 10:
                if len(linelist[10])>1:
                    moduleid = linelist[0]
                    oisid = linelist[7]
                    lotid = linelist[1]
                    ngname = linelist[10]
                    mc = linelist[4]
                    if 'CTQ' in ngname:
                        pass
                    else:
                        self.nglist[oisid] = [mc,lotid,moduleid,ngname]
    #13 NG List 출력 및 저장
    def get_nglist(self):
        print('[NID] #13 NG List 출력 및 저장 #################################################')
        # for i in self.nglist:
        #     print(f'{i} >> {self.nglist[i]}')
        ng_text = ''
        a = clipboard.paste()
        split_data = a.split('\n')
        for line in split_data:
            line_data = line.split('\t')
            try:
                product_moduleid = line_data[0]
                lotid = line_data[1]
                mc = line_data[4]
                trayid = line_data[5]
                pocketno = line_data[6]
                oisid = line_data[7]
                judge = line_data[8]
                ng_name = line_data[10]
                if ng_name == "" or "CTQ" in ng_name:
                    pass
                else:
                    ng_text += f'{product_moduleid},{lotid},{mc},{trayid},{pocketno},{oisid},{judge},{ng_name}\n'
            except:
                pass
        filepath = f'{self.downloadpath}/{self.date_from}_{self.date_to}'

        FolderExists(filepath)

        filename = f'{self.date_from} 0820_{self.date_to} 0820 NG List.csv'
        try:
            with open(filepath + '/' + filename, 'w', encoding='cp949') as w:
                w.write(ng_text)
        except PermissionError:
            print(f'[Error] {filename} 파일이 열려있습니다. 닫고 다시 시도하세요.')


'''