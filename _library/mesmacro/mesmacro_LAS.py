from _library.functions.func_pyautogui import KeyboardMouse
import time
import clipboard
import datetime

class LAS:
    # def __init__(self, lotid, imagepath, downloadpath, filename):
    # def __init__(self):
    def __init__(self, date_from, date_end, lotid, imagepath, downloadpath, filename):
        print('[LAS] 시퀀스 시작 ################################################')
        self.km = KeyboardMouse()
        self.date_from = date_from

        temp_y = int(self.date_from.split("-")[0])
        temp_m = int(self.date_from.split("-")[1])
        temp_d = int(self.date_from.split("-")[2])
        temp_date_from = datetime.datetime(temp_y,temp_m, temp_d)
        date_from_delta = temp_date_from + datetime.timedelta(days=-1)
        self.date_from_delta = date_from_delta.strftime('%Y-%m-%d')


        self.date_end = date_end
        self.lotid = lotid
        self.imagepath = imagepath
        self.downloadpath = downloadpath
        self.filename = filename
        self.n1_las_init()
        self.n2_las_log_init()
        self.n3_las_log_download()
        self.n4_las_image_init()
        self.n5_las_image_copydata()
        print(f'[LAS] 시퀀스 완료 ################################################')

    # LAS 프로그램 초기화
    def n1_las_init(self):
        print('[LAS] 0. 창 열기')
        while True:
            x, y = self.km.find_image(f'{self.imagepath}p_las.png')
            if x != 0 and y != 0:
                self.km.move(x, y)
                time.sleep(1)
                self.km.click(x, y-50)
                break
            else:
                time.sleep(0.5)

        print('[LAS] 1. LAS 열려 있는 지 확인')
        try:
            self.km.find_image(f'{self.imagepath}las1.png')
        except:
            x, y = self.km.find_image(f'{self.imagepath}las_logo.png')
            self.km.move(x, y)
            time.sleep(1)
            self.km.click(x, y-50)
        print('[LAS] 2. LAS 열려있는 탭 있는 지 확인하고 닫기')
        # 기존 열려있는 탭 모두 닫기
        x, y = self.km.find_image(f'{self.imagepath}las-tab1.png')
        if x != 0 and y != 0:
            self.km.click(x+50, y)
            time.sleep(0.1)
        x, y = self.km.find_image(f'{self.imagepath}las-tab2.png')
        if x != 0 and y != 0:
            self.km.click(x+60, y)
            time.sleep(0.1)
    def mcsetting_search(self):
        print('[LAS] 설비 선택')
        x, y = self.km.find_image(f'{self.imagepath}las-mc.png')
        self.km.click(x+100, y)
        time.sleep(0.1)
        self.km.move(x + 100, y+30)
        x, y = self.km.find_image(f'{self.imagepath}las-selectall.png')
        if x !=0 and y != 0:
            self.km.click(x-30, y)
            time.sleep(0.1)

        self.km.hotkeys('end')
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        self.km.scroll(100)
        time.sleep(0.5)

        for i in range(4):
            x, y = self.km.find_image(f'{self.imagepath}las-ois.png')
            if x != 0 and y != 0:
                self.km.click(x - 20, y)
                time.sleep(0.1)
            time.sleep(0.1)
        time.sleep(0.5)
        x, y = self.km.find_image(f'{self.imagepath}las-ok.png')
        self.km.click(x, y)
        time.sleep(0.1)
        print('[LAS] 로그 다운로드 - 조회 버튼 클릭')
        x, y = self.km.find_image(f'{self.imagepath}las-search.png')
        self.km.click(x, y)
        time.sleep(0.1)

        print('[LAS] 로그 다운로드 - 조회 결과 대기')
        time.sleep(5)
        while True:
            x, y = self.km.find_image(f'{self.imagepath}las-result1.png')
            if x != 0 and y != 0:
                break
        time.sleep(2)
        self.km.click(x, y)
        time.sleep(0.1)
        self.km.selectAll()
        time.sleep(1)

    def datesetting(self):
        print('[LAS] 로그 다운로드 - 날짜 선택')
        from_y = self.date_from.split("-")[0]
        from_m = self.date_from.split("-")[1]
        from_d = self.date_from.split("-")[2]
        from_d_delta = self.date_from_delta.split("-")[2]
        end_y = self.date_end.split("-")[0]
        end_m = self.date_end.split("-")[1]
        end_d = self.date_end.split("-")[2]
        ################################################################################################################
        x, y = self.km.find_image(f'{self.imagepath}las-datefrom.png')
        self.km.click(x+70, y)
        time.sleep(0.1)
        print('[LAS] 조회기간(From) 입력')
        self.km.selectAll()
        self.km.delete()
        self.km.keys(from_y)
        self.km.hotkeys('right')
        self.km.keys(from_m)
        self.km.hotkeys('right')
        self.km.keys(from_d_delta)
        self.km.hotkeys('right')
        self.km.keys('20')
        self.km.hotkeys('tab')
        print('[LAS] 조회기간(To) 입력')
        self.km.selectAll()
        self.km.delete()
        self.km.keys(end_y)
        self.km.hotkeys('right')
        self.km.keys(end_m)
        self.km.hotkeys('right')
        self.km.keys(end_d)
        self.km.hotkeys('right')
        self.km.keys('00')
        ################################################################################################################
    def n2_las_log_init(self):
        # lOG 파일 조회
        print('[LAS] Log 파일 조회 탭 열기')
        x, y = self.km.find_image(f'{self.imagepath}las-topmenu-data.png')
        self.km.click(x, y)
        time.sleep(0.1)
        self.km.move(x, y+40)
        time.sleep(1)
        self.km.click(x+50, y + 40)
        time.sleep(1)
        self.datesetting()
        print('[LAS] 구분 - 양산로그 선택')
        self.km.hotkeys('tab')
        self.km.hotkeys('down')
        self.km.hotkeys('down')

        clipboard.copy(self.lotid)
        time.sleep(0.5)
        if len(self.lotid) <= 1:
            print('[LAS] Error Lot ID가 비어있습니다. 확인하십시오.')
        for i in range(5):
            self.km.hotkeys('tab')
        self.km.paste()

        self.mcsetting_search()
    def n3_las_log_download(self):

        print('[LAS] 로그 다운로드 - 조회 결과 완료')
        print('[LAS] 로그 다운로드 - Merge 클릭')
        x, y = self.km.find_image(f'{self.imagepath}las-merge.png')
        if x != 0 and y != 0:
            self.km.click(x, y)

        x, y = self.km.find_image(f'{self.imagepath}las-saveas.png')
        self.km.click(x-50, y)
        time.sleep(1)

        print('[LAS] 로그 다운로드 - 경로 선택')
        clipboard.copy(self.downloadpath)
        x, y = self.km.find_image(f'{self.imagepath}las-saveas_path.png')
        if x != 0 and y != 0:
            self.km.rclick(x+200, y)
            time.sleep(0.05)
            self.km.keys('e')
        else:
            x, y = self.km.find_image(f'{self.imagepath}las-saveas_path.png')
            if x != 0 and y != 0:
                self.km.rclick(x+200, y)
                time.sleep(0.05)
                self.km.keys('e')

        time.sleep(0.1)
        self.km.paste()
        time.sleep(0.5)
        self.km.hotkeys('enter')
        time.sleep(0.5)
        for i in range(7):
            self.km.hotkeys('tab')
        self.km.hotkeys('enter')
        while True:
            x, y = self.km.find_image(f'{self.imagepath}las-save.png')
            if x != 0 and y != 0:
                self.km.click(x, y)
                print('[LAS] 로그 다운로드 - 다운로드 > 5초 대기')
                time.sleep(5)
                break
    def n4_las_image_init(self):
        # lOG 파일 조회
        print('[LAS] 이미지 파일 조회 탭 열기')
        x, y = self.km.find_image(f'{self.imagepath}las-topmenu-data.png')

        self.km.click(x, y)
        time.sleep(0.1)
        self.km.move(x, y+80)
        time.sleep(1)
        self.km.click(x+50, y + 80)
        time.sleep(1)


        self.datesetting()
        print('[LAS] 구분 - 3개월보관이미지 선택')
        self.km.hotkeys('tab')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')
        self.km.hotkeys('down')

        clipboard.copy(self.lotid)
        time.sleep(0.5)
        for i in range(4):
            self.km.hotkeys('tab')
        self.km.paste()

        self.mcsetting_search()
    def n5_las_image_copydata(self):
        time.sleep(0.5)
        clipboard.copy("")
        self.km.copy()
        print('[LAS] 결과 복사 완료 대기중.....')
        while True:
            copyresult = clipboard.paste()
            if copyresult != "":
                break
            time.sleep(1)

        result_conv = []
        temp_list = copyresult.split('\n')
        for temp_index in temp_list:
            try:
                if temp_index[0] == "C":
                    result_conv.append(temp_index)
            except:
                pass
        print('[LAS] 이미지로그 결과 데이터 저장 완료')
        with open(f'{self.downloadpath}{self.filename}', 'w') as w:
            w.writelines(result_conv)



        x, y = self.km.find_image(f'{self.imagepath}las-downloading.png')
        if x != 0 and y != 0:
            print('[LAS] 아직 다운로드 진행 중입니다.')
            while True:
                x, y = self.km.find_image(f'{self.imagepath}las-downloading.png')
                if x == 0 and y == 0:
                    print('[LAS] 로그파일 다운로드가 완료되었습니다.')
                    time.sleep(1)
                    break
                time.sleep(1)
