from _library.functions.func_pyautogui import KeyboardMouse
from _library.functions.func_foldermake import FolderExists
from _library.functions.func_Excel import *
from _library.functions.func_processcheck import *
from _library.functions.func_hwnd import *
from .ngimage_LAS import NID_LAS
from .ngimage_MES import NID_MES
from .ngimage_Excel_Report import NID_REPORT
from PyQt5.QtCore import *
import os
import time
import clipboard
import datetime
import win32com.client
import random

class NG_Image(QThread):
    flag = pyqtSignal(bool)
    msg = pyqtSignal(str)
    prog = pyqtSignal(bool, int)
    def __init__(self, run_process_list, imagepath, nowdir, date_from, date_to):
        super().__init__()
        self.imagepath = imagepath
        self.main_downloadpath = f'{nowdir}/_download'
        self.base_filename =   f'{self.main_downloadpath}/기본양식파일.xlsm'
        self.downloadpath =    f'{self.main_downloadpath}/{date_from}_{date_to}'
        self.filename =        f'{self.main_downloadpath}/{date_from}_{date_to}/{date_from} 0820_{date_to} 0820 NG List Result.csv'
        self.report_savepath = f'{self.main_downloadpath}/{date_from}_{date_to}/{date_from} 0820_{date_to} 0820 NG REPORT.xlsm'
        self.run_process_list = run_process_list
        print(self.run_process_list)
        self.date_from = date_from
        self.date_to = date_to
    def run(self):
        self.km = KeyboardMouse()
        for process in self.run_process_list:
            if process == 'MES':
                self.mes_run(imagepath=self.imagepath, downloadpath=self.downloadpath, date_from=self.date_from, date_to=self.date_to)
            if process == 'LAS':
                self.las_run(imagepath=self.imagepath, filename=self.filename, downloadpath=self.downloadpath, date_from=self.date_from, date_to=self.date_to)
            if process == 'REPORT':
                self.make_report(downloadpath=self.downloadpath, base_filename=self.base_filename, filename=self.filename, report_savepath=self.report_savepath)
        self.flag.emit(True)
    def str_strip(self, text):
        text = text.lstrip()
        return text.rstrip()
    def processCheck(self, description, category):
        print(description)
        import getpass
        if category == 'mes':
            gmes = {'processname': 'LGIT.GMES.SFU.MainFrame.exe',
                    'filename_for_run': 'GMES(JH-KG) - 복사본.appref-ms',
                    'hwnd_name': "GMES SFU(J44)"}
            process_check_run(gmes['processname'], gmes['filename_for_run'])
            hwnd = HWND(gmes['hwnd_name'])
            hwnd.windowResize()
        elif category == 'las':
            las = {'processname': 'Jahwa LAS.exe',
                    'filename_for_run': f'C:/Users/{getpass.getuser()}/AppData/Local/Jahwa_LAS_MAIN_MainShell/Jahwa LAS.exe',
                    'hwnd_name': "JLAS (Gumi) Ver.1.0.43"}
            process_check_run(las['processname'], las['filename_for_run'])
            hwnd = HWND(las['hwnd_name'])
            hwnd.windowResize()
    def active_window(self, discription, category):
        self.msg.emit(discription)
        count = 0
        while True:
            judge, x, y = self.km.image('이동', f'{self.imagepath}p_{category}.png')
            time.sleep(0.5)
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

        # [MES] 재공현황 1
    # MESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMESMES
    def mes_run(self, imagepath, downloadpath, date_from, date_to):
        self.msg.emit("asdfasfdsadfsadfsadf")
        self.imagepath = imagepath
        self.downloadpath = downloadpath
        self.date_from = date_from
        self.date_to = date_to
        self.msg.emit("[MES] 시퀀스 시작")
        # 초기설정
        self.closeExcelFile()
        self.processCheck("[MES - 초기설정] 1. 프로그램 체크", category='mes')
        self.active_window("[MES - 초기설정] 2. 프로그램 활성화", category='mes')
        transactionid = False
        querydata = False
        if os.path.exists(f'{self.downloadpath}/트렌젝션ID.txt'):
            with open(f'{self.downloadpath}/트렌젝션ID.txt', 'r') as transactionid_read:
                transactionid = transactionid_read.read()
            self.transaction_id = transactionid.rstrip()
            transactionid = True
        if os.path.exists(f'{self.downloadpath}/{self.date_from} 0820_{self.date_to} 0820 NG Stored Query.csv'):
            querydata = True
        # 재공현황
        if not transactionid and not querydata:
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
        if not querydata:
            self.n2_system_storedQuery("[MES - Stored Query 실행] 17. Stored Query 실행")
            self.closeExcelFile()  # 14

            # Stored Query
            self.data_merge("[MES - 데이터정리] 18. 모듈정보조회 & Stored Query 에서 받은 데이터 종합(NG정보 + 부자재정보)")
            self.msg.emit("[MES] 시퀀스 종료")
    def set_work_state(self, discription):
        self.msg.emit(discription)
        count = 0
        while True:
            count += 1
            judge, x, y = self.km.image('클릭', f'{self.imagepath}재공현황닫기1.png', limit=2)
            if judge:
                self.msg.emit("재공현황 닫기")
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
        self.msg.emit(discription)
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
        self.msg.emit(discription)
        self.km.image('클릭', f'{self.imagepath}재공현황-공정.png', x_offset=50, delay=1)
        self.km.image('클릭', f'{self.imagepath}재공현황-공정All.png', x_offset=-10, delay=1)

        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.km.hotkeys('pagedown')
        self.km.image('클릭', f'{self.imagepath}재공현황-공정OIS.png', delay=1)
        self.km.hotkeys('enter')
        time.sleep(0.5)

        # [MES] 재공현황 4
    def set_no_ctq(self, discription):
        self.msg.emit(discription)
        self.km.image('클릭', f'{self.imagepath}재공현황-폐기.png', x_offset=50, delay=0.5)
        self.km.image('클릭', f'{self.imagepath}재공현황-폐기미포함.png', delay=0.5)

        # [MES] 재공현황 5
    def click_search(self, discription):
        self.msg.emit(discription)
        self.km.image('클릭', f'{self.imagepath}검색.png')
        time.sleep(1)
        while True:
            judge, x, y = self.km.image('이동', f'{self.imagepath}검색완료.png', delay=0.5)
            if judge:  # self.km.image('판단', '검색완료', x_off=0, y_off=0, delay=0.5):
                break
            else:
                time.sleep(0.5)

        # [MES] 재공현황 6
    def click_ng(self, discription):
        self.msg.emit(discription)
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
        self.msg.emit(discription)
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
        self.msg.emit(f'[MES - 재공현황] 불량 발생 Lot ID : {lot_ids}')
        if len(lot_ids) < 9:
            self.lotid_judge = False
        else:
            self.lotid_judge = True

        # [MES] 모듈정보조회 1
    def set_module_info_search(self, discription):
        self.msg.emit(discription)
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
                count += 1
                time.sleep(0.1)
            if count == 20:
                count = 0

        # [MES] 모듈정보조회 2
    def search_lot(self, discription):
        self.msg.emit(discription)
        self.km.image('클릭', f'{self.imagepath}모듈정보조회-LOT검색.png', x_offset=50, delay=1)
        self.km.selectAll()
        time.sleep(0.5)
        self.km.paste()
        time.sleep(0.8)
        self.click_search("[MES - 모듈정보조회] 검색 클릭")
        time.sleep(5)

        # [MES] 모듈정보조회 3
    def search_lot_export(self, discription):
        self.msg.emit(discription)
        self.km.image('클릭', f'{self.imagepath}모듈정보조회-Export.png', delay=1)

        # [MES] 모듈정보조회 4
    def search_export(self, discription):
        self.msg.emit(discription)
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
        self.msg.emit(discription)
        while True:
            judge, x, y = self.km.image('클릭', f'{self.imagepath}모듈정보조회-엑셀파일열림확인.png', x_offset=0, delay=1)
            if judge:
                break
            time.sleep(1)
        time.sleep(1)
        self.msg.emit("[MES - 모듈정보조회] Excel Data 확인 중...")
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = True
        sheet = excel.ActiveSheet
        if sheet.Name == 'dgModuleInfomation':
            cell_count = 1
            while True:
                # self.msg.emit(sheet.Cells(cell_count, 1).Value)
                if sheet.Cells(cell_count, 1).Value == None:
                    break
                cell_count += 1
            sheet.Range(f'A1:Q{cell_count}').Copy()
            self.excel_data = clipboard.paste()
            while True:
                if self.excel_data == "":
                    self.msg.emit("[MES] 복사 대기중....")
                    time.sleep(1)
                else:
                    self.msg.emit("[MES] 복사 완료")
                    break

        # [MES] 모듈정보조회 6
    def excel_datas2(self, discription):
        self.msg.emit(discription)
        self.nglist = {}
        datalist = self.excel_data.split('\n')
        for d in datalist:
            linelist = d.split('\t')
            if len(linelist) > 10:
                if len(linelist[10]) > 1:
                    moduleid = linelist[0]
                    oisid = linelist[7]
                    lotid = linelist[1]
                    ngname = linelist[10]
                    mc = linelist[4]
                    if 'CTQ' in ngname:
                        pass
                    else:
                        self.nglist[oisid] = [mc, lotid, moduleid, ngname]

        # [MES] 모듈정보조회 7
    def get_nglist2(self, discription):
        self.msg.emit(discription)
        # for i in self.nglist:
        #     self.msg.emit(f'{i} >> {self.nglist[i]}')
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
        filepath = f'{self.downloadpath}'

        FolderExists(filepath)

        filename = f'{self.date_from} 0820_{self.date_to} 0820 NG List.csv'
        try:
            with open(filepath + '/' + filename, 'w', encoding='cp949') as w:
                w.write(ng_text)
        except PermissionError:
            self.msg.emit(f'[Error] {filename} 파일이 열려있습니다. 닫고 다시 시도하세요.')

        self.closeExcelFile()

        # [MES] 매개 변수 정보 등록
    def n1_system_management(self, discription):
        self.msg.emit(discription)
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

        self.msg.emit('[MES] 6. 매개 변수 정보 등록 - 매개 변수 정보 입력(제목, 설명, 입력 정보)')
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
        filepath = f'{self.downloadpath}'
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
        self.km.image('클릭', f'{self.imagepath}menu2_period.png', x_offset=100)
        self.km.hotkeys('tab')
        time.sleep(0.1)
        self.km.hotkeys('tab')
        time.sleep(0.1)

        self.msg.emit('[MES] 7. 매개 변수 정보 등록 - 제목 조회')
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
        with open(f'{self.downloadpath}/트렌젝션ID.txt', 'w') as w:
            w.write(self.transaction_id)

        self.msg.emit(f'[MES] 8. 매개 변수 정보 등록 - TransActionID : {self.transaction_id}')
        return True
        # 2. 시스템관리 - Stored Query 실행

        # [MES] Stored Query
    def n2_system_storedQuery(self, discription):
        # self.transaction_id = '20240321085504454293'
        self.msg.emit(discription)
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

                judge2, x2, y2 = self.km.image('클릭', f'{self.imagepath}menu1_parameter.png', y_offset=25,
                                               delay=0.5)
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
        self.msg.emit(f'[MES] 10. Stored Query 실행 - CSV Export')
        self.km.image('클릭', f'{self.imagepath}menu1_csvexport.png', delay=1.8)
        self.km.image('클릭', f'{self.imagepath}menu1_csvexport_saveas.png', delay=0.8)

        # clipboard.copy(f'{self.downloadpath}\{self.date_from}_{self.date_to}')
        clipboard.copy(self.downloadpath)
        time.sleep(0.3)
        self.km.selectAll()
        self.km.delete()
        self.km.paste()
        self.km.hotkeys('enter')
        time.sleep(0.5)
        filename = f'{self.date_from} 0820_{self.date_to} 0820 NG Stored Query.csv'
        clipboard.copy(filename)
        time.sleep(0.8)

        self.km.keydown('alt')
        time.sleep(0.01)
        self.km.keys('t')
        time.sleep(0.01)
        self.km.keys('n')
        time.sleep(0.01)
        self.km.keyup('alt')
        time.sleep(0.01)
        # for i in range(6):
        #     self.km.hotkeys('tab')
        #     time.sleep(0.1)

        self.km.paste()
        time.sleep(0.1)
        self.km.hotkeys('enter')
        time.sleep(1)
        judge, x, y = self.km.image('클릭', f'{self.imagepath}menu1_saveas.png', delay=0.5)
        if judge:
            self.km.hotkeys('enter')
            time.sleep(1)
        self.km.image('클릭', f'{self.imagepath}menu1_cancel.png', delay=0.5)

        # 14 Excel 종료
    def closeExcelFile(self):
        self.msg.emit('closeExcelFile')
        ps_name = 'EXCEL.EXE'
        # if process_list_self.msg.emit(ps_name):
        kill_process(ps_name)

        # [MES] 모듈정보조회 & Stored Query 데이터 합치기(ng 정보 + 부자재정보)
    def data_merge(self, discription):
        self.msg.emit(discription)
        self.moduleid = ''
        filepath = f'{self.downloadpath}'
        filename2 = f'{self.date_from} 0820_{self.date_to} 0820 NG Stored Query.csv'

        with open(os.path.join(filepath, filename2), 'r', encoding='UTF8') as r:
            readlines = r.readlines()
        dict_querydata = {}
        dict_querydata_time = {}

        for line in readlines:
            self.msg.emit(f'[NG List Query File] {line}')
            split_data = line.split(",")
            p_moduleid = split_data[0]
            if p_moduleid != "PROD_MODULEID":
                submaterials_data = ""
                for i in range(6, 22):
                    submaterials_data += f'{split_data[i]},'
                submaterials_data = submaterials_data[0:-1]
                self.msg.emit(f'>> {p_moduleid} : {submaterials_data}')
                dict_querydata[p_moduleid] = submaterials_data

                dict_querydata_time[p_moduleid] = split_data[4]
                # self.msg.emit(split_data[4].split(" "))
                # dict_querydata_judge[p_moduleid] = split_data[5]

        filename1 = f'{self.date_from} 0820_{self.date_to} 0820 NG List.csv'
        filename3 = f'{self.date_from} 0820_{self.date_to} 0820 NG List Result.csv'
        new_line = [
            "생산 모듈,LOT ID,설비명,일자,예비용,모듈,판정,사유명,MGZ_Z,CARRIERID_Z,POCKET_Z,X_STAGE_PNP_CARRIER_MLOTID,MGZ_X,CARRIERID_X,POCKET_X,MODULE_Y,Y_STAGE_PNP_CARRIER_MLOTID,MGZ_Y,CARRIERID_Y,POCKET_Y,Z_STOPPER_PNP_CARRIER_MLOTID,MGZ_ZS,CARRIERID_ZS,POCKET_ZS\n"]

        with open(os.path.join(filepath, filename1), 'r') as r:
            readlines = r.readlines()
        for line in readlines:
            # self.msg.emit(f'[NG List NG List File] {line}')
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
                # 생산 모듈,LOT ID,설비명,일자,예비용,모듈,판정,사유명  , MGZ_Z,CARRIERID_Z,POCKET_Z,X_STAGE_PNP_CARRIER_MLOTID,MGZ_X,CARRIERID_X,POCKET_X,MODULE_Y,Y_STAGE_PNP_CARRIER_MLOTID,MGZ_Y,CARRIERID_Y,POCKET_Y,Z_STOPPER_PNP_CARRIER_MLOTID,MGZ_ZS,CARRIERID_ZS,POCKET_ZS\n
                new_line.append(f'{file1_line},{dict_querydata[p_moduleid]}')
            except KeyError:
                self.msg.emit("ERROR")
                pass

        with open(os.path.join(filepath, filename3), 'w') as w:
            w.writelines(new_line)

    # LASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLASLAS
    def las_run(self,imagepath, downloadpath, filename, date_from, date_to):
        self.imagepath = imagepath

        self.filename = filename
        self.downloadpath = downloadpath
        self.date_from = date_from
        self.date_to = date_to

        self.downloadpath_log = f'{self.downloadpath}/log'
        self.count_dict = {}
        # Program Settings ###########
        self.processCheck("[LAS - 초기설정] 1. 프로그램 체크", category='las')
        self.active_window("[LAS - 초기설정] 2. 프로그램 창 열기", category='las')
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
        self.downloadpath_log = f'{self.downloadpath}/log'
        self.count_dict = {}


    def las_make_folders(self, mc, oisid, ngname) -> str:
        path = f'{self.downloadpath}/#{mc[-1]}/{ngname}/{oisid}'
        FolderExists(path)
        return path
    def moveFile(self, src, dst, filename):
        import shutil
        import os
        shutil.move(os.path.join(src, filename), os.path.join(dst, filename))

    ##################################################################
    #공통 [LAS] 초기설정 - 정리된 불량데이터파일 열기
    def read_file(self, description):
        self.msg.emit(description)
        self.nglist = {}
        self.lotids = []
        with open(self.filename, encoding='cp949') as r:
            nglist = r.readlines()
        for line in nglist:
            str_line = self.str_strip(line)
            split_datas = str_line.split(',')
            print(split_datas)
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
        # self.msg.emit(self.nglist)
    #공통 [LAS] 초기설정 - 날짜 및 공정 셋팅
    def las_options_settings(self, description):
        self.msg.emit(description)
        df_y = int(self.date_from.split('-')[0])
        df_m = int(self.date_from.split('-')[1])
        df_d = int(self.date_from.split('-')[2])
        dt_y = int(self.date_to.split('-')[0])
        dt_m = int(self.date_to.split('-')[1])
        dt_d = int(self.date_to.split('-')[2])
        datetime_from = datetime.datetime(df_y,df_m,df_d)
        datetime_to = datetime.datetime(dt_y,dt_m,dt_d)

        search_from = datetime_from - datetime.timedelta(days=1)
        search_to = datetime_to + datetime.timedelta(days=1)
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
        self.msg.emit(description)
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
        self.msg.emit(description)
        files = ['XAT.txt', 'YAT.txt', 'ZAT.txt', 'UVI.txt']
        self.logfile_exists = True
        for filename in files:
            filepath = os.path.join(self.downloadpath_log, filename)
            if not os.path.exists(filepath):
                self.logfile_exists = False
                break
        if self.logfile_exists:
            self.msg.emit(f'[LAS] 해당 기간 내에 이미 다운로드 받은 LAS로그파일이 있습니다.')
            return
        self.km.image('클릭', f'{self.imagepath}LAS-상단메뉴-데이터.png', delay=0.1)
        self.km.hotkeys('tab')
        time.sleep(0.1)
        self.km.hotkeys('enter')
        self.km.hotkeys('enter')
    #4 [LAS] 실행 - 로그 파일 다운로드
    def las_log_download(self, description):
        self.msg.emit(description)

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
        self.msg.emit(f'[LAS - 실행] 로그 파일 조회 시작')
        while True:
            judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-로딩.png', limit=2)
            if not judge:
                time.sleep(1.5)
                judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-로딩.png', limit=1)
                if not judge:
                    break
            time.sleep(1)
        self.msg.emit(f'[LAS - 실행] 로그파일 조회 완료')

        self.km.image('클릭', f'{self.imagepath}LAS-결과전체선택.png', y_offset=50, delay=0.1)
        self.km.selectAll()
        self.km.image('클릭', f'{self.imagepath}LAS-저장.png', delay=3)
        self.msg.emit(f'[LAS - 실행] 로그파일 다운로드 시작')
        while True:
            judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-다운로드로딩.png', limit=2)
            if not judge:
                time.sleep(1.5)
                judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-다운로드로딩.png', limit=1)
                if not judge:
                    break
            time.sleep(1)
        self.msg.emit(f'[LAS - 실행] 로그파일 다운로드 완료)')
    #5 [LAS] 실행 - 로그 파일 정리
    def las_logfile_merge(self, description):
        self.msg.emit(description)
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
        self.msg.emit(description)
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

        self.msg.emit(description)
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
        self.msg.emit(description)
        self.km.image('클릭', f'{self.imagepath}LAS-상단메뉴-데이터.png', delay=0.1)
        self.km.hotkeys('tab')
        self.km.hotkeys('tab')
        time.sleep(0.1)
        self.km.hotkeys('enter')
        self.km.hotkeys('enter')
    #8 [LAS] 실행 - 불량 이미지 다운로드 (material : "main" or "sub")
    def las_search(self, material, discription):
        self.msg.emit(discription)
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
        self.msg.emit(f'[LAS - 실행] 이미지 조회 시작 ({material})')
        while True:
            judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-로딩.png', limit=2)
            if not judge:
                time.sleep(1.5)
                judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-로딩.png', limit=1)
                if not judge:
                    break
            time.sleep(1)
        self.msg.emit(f'[LAS - 실행] 이미지 조회 완료 ({material})')

        self.km.image('클릭', f'{self.imagepath}LAS-결과전체선택.png', y_offset=50, delay=0.1)
        self.km.selectAll()
        self.km.image('클릭', f'{self.imagepath}LAS-저장.png', delay=3)
        self.msg.emit(f'[LAS - 실행] 이미지 다운로드 시작 ({material})')
        while True:
            judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-다운로드로딩.png', limit=2)
            if not judge:
                time.sleep(1.5)
                judge, x, y = self.km.image('판단', f'{self.imagepath}LAS-다운로드로딩.png', limit=1)
                if not judge:
                    break
            time.sleep(1)
        self.msg.emit(f'[LAS - 실행] 이미지 다운로드 완료 ({material})')
    #9 [LAS] 분류 - 불량 이미지 분류를 위한 count
    def categorization(self, material, discription):
        # 1. 폴더 내 파일 리스트 읽기.
        # 2. 지정한 폴더로 이동 ( 지정한 폴더가 없을 시 생성 )
        self.msg.emit(discription)
        imagefilelist = os.listdir(self.downloadpath)
        if material == 'sub':
            temp_dict = {}
            for module in self.nglist:
                try:
                    self.msg.emit(f'{module} {self.nglist[module]}')
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
                    self.msg.emit(f'[temp_dict Error]')

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
                print(temp_dict)
                oisid = f'{temp_dict[f.split("_")[2]]}'
                mc = self.nglist[oisid][0][-3:]
                ngname = self.nglist[oisid][3]
                # count = self.count_dict[oisid]
                dst = self.las_make_folders(mc, oisid, ngname)
                self.moveFile(self.downloadpath, dst, f)
    #10 [LAS] 결과 폴더 열기
    def las_finish(self, discription):
        self.msg.emit(discription)
        os.startfile(self.downloadpath)
    def copy_data(self, data):
        self.msg.emit(f'clipboard')
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


    def make_report(self, downloadpath, base_filename, filename, report_savepath):
        self.path = downloadpath
        self.logfile = filename
        self.filename = base_filename
        self.savepath = report_savepath

        filepath = os.path.join(self.path, self.filename)
        self.excel = ExcelWings(filepath)
        self.get_ngnames_for_add_sheets("[EXCEL REPORT] #1 로그파일 읽고 불량명으로 시트 추가")
        # self.excel.save(saveas=new_file)
        self.image_insert("[EXCEL REPORT] #2 로그파일 읽기")
        self.excel.save(saveas=self.savepath)
    # [EXCEL REPORT] #1 초기설정
    def initial_sheets(self, sheetnames):
        first_row = ["생산 모듈", "LOT ID", "설비명", "일자", "예비용", "모듈", "판정", "사유명", "MGZ_Z", "CARRIERID_Z", "POCKET_Z",
                     "X_STAGE_PNP_CARRIER_MLOTID", "MGZ_X", "CARRIERID_X", "POCKET_X", "MODULE_Y",
                     "Y_STAGE_PNP_CARRIER_MLOTID", "MGZ_Y", "CARRIERID_Y", "POCKET_Y", "Z_STOPPER_PNP_CARRIER_MLOTID",
                     "MGZ_ZS", "CARRIERID_ZS", "POCKET_ZS", "불량발생설비", "불량코드", "불량명"]
        cells_width = [20, 17, 11, 7, 2, 24, 6, 30, 10, 7, 2, 17, 10, 7, 2, 24, 17, 10, 7, 2, 17, 10, 7, 2, 18, 9, 32]
        cells_width_image = 56
        self.prog.emit(True, len(sheetnames))
        count = 0
        for sheetname in sheetnames:
            # 불량명으로 sheet 생성
            sheetadd_result = self.excel.sheetadd(sheetname, zoom=70)
            if sheetadd_result:
                self.excel.insert(sheetname, 'A1', first_row)
                # 시트 생성 후 열 너비 설정
                for c in range(len(cells_width)):
                    self.excel.coumns_width(sheetname, f'{self.excel.convert_cols(c)}:{self.excel.convert_cols(c)}',
                                            cells_width[c])
                self.excel.coumns_width(sheetname, f'{self.excel.convert_cols(26)}:{self.excel.convert_cols(55)}', 56)
            self.prog.emit(False, count)
            count += 1
        # 데이터종합시트
        sheetadd_result = self.excel.sheetadd("데이터 종합", zoom=70, showGrid=False)
        self.excel.insert("데이터 종합", 'A1', first_row)
        if sheetadd_result:
            for c in range(len(cells_width)):
                self.excel.coumns_width("데이터 종합", f'{self.excel.convert_cols(c)}:{self.excel.convert_cols(c)}',
                                        cells_width[c])
    # [EXCEL REPORT] #2 LOGFILE 읽기
    def get_ngnames_for_add_sheets(self, description):
        self.msg.emit(description)
        filepath = os.path.join(self.path, self.logfile)
        ngnames = []
        with open(filepath, 'r') as r:
            read_lines = r.readlines()
        for i in range(len(read_lines)):
            line = read_lines[i]
            split_datas = line.split(',')
            moduleid = split_datas[0]
            if moduleid == "생산 모듈":
                continue
            ngnames.append(split_datas[7])  # sheet name
        # return ngnames
        self.initial_sheets(ngnames)
        # [EXCEL REPORT] #3 Image Insert
    def image_insert(self, description):
        self.msg.emit(description)
        filepath = os.path.join(self.path, self.logfile)
        with open(filepath, 'r') as r:
            read_lines = r.readlines()
        nglist_dict = {}
        self.prog.emit(True, len(read_lines))
        count = 0
        for i in range(len(read_lines)):
            line = read_lines[i]
            split_datas = line.split(',')
            moduleid = split_datas[0]
            lotid = split_datas[1]
            mc = split_datas[2]
            oisid = split_datas[5]
            ngname = split_datas[7]  # sheet name

            if moduleid == "생산 모듈" or oisid == "NoneModuleID":
                continue
            try:
                ng_count = nglist_dict[ngname]
                nglist_dict[ngname] = ng_count + 1
            except:
                self.excel.sheetadd(ngname)
                nglist_dict[ngname] = 1

            self.excel.insert(ngname, f'A{nglist_dict[ngname] + 1}', split_datas)
            self.excel.insert("데이터 종합", f'A{i + 1}', split_datas)

            image_file_list = os.listdir(f'{self.path}/#{mc[-1:]}/{ngname}/{oisid}')
            mc_Barcode = []
            mc_Grease1 = []
            mc_Ball1 = []
            mc_XATT = []
            mc_Grease2 = []
            mc_Ball2 = []
            mc_YATT = []
            mc_ZSATT = []
            mc_Epoxy1 = []
            mc_Epoxy2 = []
            mc_UVInsp = []

            for image_file in image_file_list:
                if image_file.find('H01.jpg') != -1:
                    mc_Barcode.append(image_file)
                elif image_file.find('T01.jpg') != -1:
                    mc_Grease1.append(image_file)
                elif image_file.find('T02.jpg') != -1:
                    mc_Ball1.append(image_file)
                elif image_file.find('T03.jpg') != -1:
                    mc_XATT.append(image_file)
                elif image_file.find('T04.jpg') != -1:
                    mc_Grease2.append(image_file)
                elif image_file.find('T05.jpg') != -1:
                    mc_Ball2.append(image_file)
                elif image_file.find('T06.jpg') != -1:
                    mc_YATT.append(image_file)
                elif image_file.find('T07.jpg') != -1:
                    mc_ZSATT.append(image_file)
                elif image_file.find('T08.jpg') != -1:
                    mc_Epoxy1.append(image_file)
                elif image_file.find('T09.jpg') != -1:
                    mc_Epoxy2.append(image_file)
                elif image_file.find('T10.jpg') != -1:
                    mc_UVInsp.append(image_file)

            image_files_lists = mc_Barcode + mc_Grease1 + mc_Ball1 + mc_XATT + mc_Grease2 + mc_Ball2 + mc_YATT + mc_ZSATT + mc_Epoxy1 + mc_Epoxy2 + mc_UVInsp
            self.temp_dict = {}
            for i in range(len(image_files_lists)):
                image = image_files_lists[i]
                # self.get_data_from_filename(ngname, nglist_dict[ngname]+1, image)
                img_file = os.path.join(f'{self.path}/#{mc[-1:]}/{ngname}/{oisid}', image)

                # Image 넣기
                try:
                    self.excel.image_insert(img_file=img_file, sheetname=ngname, row=f'{self.excel.convert_cols(i + 28)}',
                                            col=nglist_dict[ngname] + 1, resize=['h', 400])
                except:
                    pass
                # Image 경로 넣기
                self.excel.insert(ngname, f'{self.excel.convert_cols(i + 28)}{nglist_dict[ngname] + 1}', [img_file])

            self.prog.emit(False, count)
            count += 1
