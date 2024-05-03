from _library.functions.func_pyautogui import KeyboardMouse
import time
import clipboard

class MES:
    def __init__(self, moduleid="", imagepath="", downloadpath="", filename=""):
        print('[MES] 시퀀스 시작 ################################################')
        self.km = KeyboardMouse()
        self.moduleid = moduleid
        self.imagepath = imagepath
        self.querypath = downloadpath
        self.filename = filename

        self.transaction_id = ""
        self.n0_init()
        self.n1_system_management()
        self.n2_system_storedQuery()
        print(f'[MES] 시퀀스 완료 ################################################')

    #0. MES 기본설정
    def n0_init(self):
        print('[MES] 0. 창 열기')
        while True:
            print(self.imagepath)
            x, y = self.km.find_image(f'{self.imagepath}p_mes.png')
            if x != 0 and y != 0:
                print(x, y)
                self.km.move(x, y)
                time.sleep(1)
                self.km.click(x, y-50)
                break
            else:
                time.sleep(0.5)

        print('[MES] 1. 기존 열려있던 탭 종료')
        x, y = self.km.find_image(f'{self.imagepath}init11.png')
        print(x, y)
        if x != 0 or y != 0:
            self.km.click(x+60, y)
        x, y = self.km.find_image(f'{self.imagepath}init12.png')
        print(x, y)
        if x != 0 or y != 0:
            self.km.click(x+60, y)
        x, y = self.km.find_image(f'{self.imagepath}init21.png')
        print(x, y)
        if x != 0 or y != 0:
            self.km.click(x+60, y)
        x, y = self.km.find_image(f'{self.imagepath}init22.png')
        print(x, y)
        if x != 0 or y != 0:
            self.km.click(x+60, y)

    #1. 시스템관리 - 매개 변수 정보 등록
    def n1_system_management(self):
        print('[MES] 2. 상단 탑 메뉴 - 시스템 관리 클릭')
        x, y = self.km.find_image(f'{self.imagepath}topmenu_system2.png')
        time.sleep(1)
        self.km.click(x, y)
        time.sleep(0.5)
        print('[MES] 3. 상단 탑 메뉴 - 매개 변수 정보 등록 클릭')

        x, y = self.km.find_image(f'{self.imagepath}topmenu_menu2.png')
        self.km.click(x, y)
        time.sleep(0.5)
        while True:
            print('[MES] 4. 매개 변수 정보 등록 - 작업자 입력')
            x, y = self.km.find_image(f'{self.imagepath}menu2_worker.png')
            self.km.click(x+50, y)
            time.sleep(0.5)

            self.km.selectAll()
            time.sleep(0.1)
            self.km.delete()
            time.sleep(0.1)

            self.km.keys('K22206033')
            time.sleep(0.5)
            self.km.hotkeys('enter')
            time.sleep(0.5)
            x_save = 0
            y_save = 0
            try:
                x_save, y_save = self.km.find_image(f'{self.imagepath}menu2_save.png')
                state = True
            except:
                state = False
            if state:
                print('[MES] 5. 매개 변수 정보 등록 - 작업자 입력(완료)')
                break
        print('[MES] 6. 매개 변수 정보 등록 - 매개 변수 정보 입력(제목, 설명, 입력 정보)')
        import random
        n = random.randint(1000,1000000)
        self.transaction_title = f'OIS_MODULEID_{n}'

        x, y = self.km.find_image(f'{self.imagepath}menu2_input.png')
        self.km.click(x, y)
        # time.sleep(0.5)
        # self.km.key_press('shift')
        self.km.hotkeys('tab')
        # self.km.key_release('shift')
        time.sleep(0.5)

        clipboard.copy(self.transaction_title)
        time.sleep(0.1)
        self.km.paste()
        time.sleep(0.1)
        self.km.hotkeys('tab')
        time.sleep(0.1)
        self.km.keys('OIS2')
        time.sleep(0.1)
        self.km.hotkeys('tab')
        time.sleep(0.1)

        clipboard.copy(self.moduleid)
        self.km.paste()
        while True:
            try:
                self.km.click(x_save, y_save)
                time.sleep(0.8)
                break
            except:
                time.sleep(1)
        x, y = self.km.find_image(f'{self.imagepath}menu2_save_ok.png')
        self.km.click(x, y)
        time.sleep(1)
        x, y = self.km.find_image(f'{self.imagepath}menu2_save_ok.png')
        self.km.click(x, y)
        time.sleep(0.5)
        x, y = self.km.find_image(f'{self.imagepath}menu2_period.png')
        self.km.click(x+100, y)
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
        x, y = self.km.find_image(f'{self.imagepath}menu2_search.png')
        self.km.click(x, y)
        time.sleep(1.5)

        clipboard.copy("")
        x, y = self.km.find_image(f'{self.imagepath}menu2_transactionid.png')
        self.km.click(x, y+60)
        self.km.copy()
        temp = clipboard.paste()
        while True:
            if temp != "":
                self.transaction_id = temp
                break
            time.sleep(0.1)
        time.sleep(2)
        print(f'[MES] 8. 매개 변수 정보 등록 - TransActionID : {self.transaction_id}')
    #2. 시스템관리 - Stored Query 실행
    def n2_system_storedQuery(self):

        print('[MES] 2. 상단 탑 메뉴 - 시스템 관리 클릭')
        x, y = self.km.find_image(f'{self.imagepath}topmenu_system2.png')
        time.sleep(1)
        print(x, y)
        self.km.move(x, y)
        time.sleep(1)
        print(x, y)
        self.km.click(x, y)
        time.sleep(1)

        print('[MES] 9. 상단 탑 메뉴 - Stored Query 클릭')
        x, y = self.km.find_image(f'{self.imagepath}topmenu_menu1.png')
        self.km.click(x, y)
        time.sleep(1)

        x, y = self.km.find_image(f'{self.imagepath}menu1_queryname.png')
        self.km.click(x, y)
        time.sleep(0.5)
        self.km.click(x, y+50)
        time.sleep(0.5)
        self.km.hotkeys('tab')
        self.km.selectAll()
        self.km.delete()
        search_name = 'OIS Assy 공정 사용 자재 정보 조회 (MGZ, TRAY, POCKET / BY 멀티 생산모듈ID)'
        clipboard.copy(search_name)
        self.km.paste()
        x, y = self.km.find_image(f'{self.imagepath}menu2_search.png')
        self.km.click(x, y)
        time.sleep(0.5)

        x, y = self.km.find_image(f'{self.imagepath}menu1_queryresult.png')
        self.km.click(x, y)
        self.km.click(x, y)
        time.sleep(0.5)

        x, y = self.km.find_image(f'{self.imagepath}menu1_parameter.png')
        self.km.click(x, y+25)
        time.sleep(1)
        self.km.click(x, y+25)

        clipboard.copy(self.transaction_id)
        self.km.selectAll()
        self.km.delete()
        self.km.paste()

        x, y = self.km.find_image(f'{self.imagepath}menu1_run.png')
        self.km.click(x, y)
        time.sleep(1)

        while True:
            try:
                x, y = self.km.find_image(f'{self.imagepath}menu1_queryresult_wait.png')
                state = True
            except:
                state = False
            time.sleep(0.5)
            if state:
                time.sleep(3)
                break
        print(f'[MES] 10. Stored Query 실행 - CSV Export')
        x, y = self.km.find_image(f'{self.imagepath}menu1_csvexport.png')
        self.km.click(x, y)
        time.sleep(1.5)

        x, y = self.km.find_image(f'{self.imagepath}menu1_csvexport_saveas.png')
        self.km.click(x, y)
        time.sleep(0.5)
        clipboard.copy(self.querypath)
        self.km.selectAll()
        self.km.delete()
        self.km.paste()
        self.km.hotkeys('enter')
        time.sleep(0.5)

        clipboard.copy(self.filename)
        for i in range(6):
            self.km.hotkeys('tab')
            time.sleep(0.1)
        self.km.paste()
        time.sleep(0.1)
        self.km.hotkeys('enter')
        time.sleep(1)
        try:
            x, y = self.km.find_image(f'{self.imagepath}menu1_saveas.png')
            self.km.hotkeys('enter')
            time.sleep(1)
        except:
            pass
        x, y = self.km.find_image(f'{self.imagepath}menu1_cancel.png')
        self.km.click(x, y)
        time.sleep(0.5)


