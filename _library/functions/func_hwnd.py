import win32gui
import win32ui
import win32api
import win32con
#윈도우 핸들을 찾기 위한 라이브러리
#pip install pypiwin32
from PIL import Image
#이미지저장을 위한 라이브러리
#pip install pillow
from ctypes import windll

import time

class HWND:
    def __init__(self, hwndname):
        self.hwndname = hwndname
        self.hwnd = win32gui.FindWindow(None, hwndname)
    def windowResize(self):
        if self.hwnd >= 1:
            left, top, right, bot = win32gui.GetWindowRect(self.hwnd)
            w = right - left
            h = bot - top
            # print(f'GetActiveWindow : {win32gui.GetActiveWindow()}')
            print(w, h)
            win32gui.MoveWindow(self.hwnd, 0, 0, 1920, 1040, True)


    # 실패
    def maximize(self):
        import ctypes
        # user32 = ctypes.WinDLL('user32')
        # user32.ShowWindow
        hwnd = win32gui.GetForegroundWindow()
        # win32gui.SetWindowLong(hwnd, win32con.SW_MAXIMIZE)
        win32gui.ShowWindow(self.hwnd, win32con.SW_MAXIMIZE)
    # 실패
    def enumwindows(self):
        wintext = win32gui.GetWindowText(self.hwnd)
        print(self.hwnd, wintext)
    #실패
    def click(self, x, y):
        # self.hwnd2 = self.get_inner_windows(self.hwnd)
        # self.hwnd2 = self.hwnd
        # print('HWND click')
        lParam = win32api.MAKELONG(x, y)
        # print(f'lParam : {lParam}')
        # # win32gui.SendMessage(self.hwnd2, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        # time.sleep(0.2)
        # win32gui.SendMessage(self.hwnd2, win32con.WM_LBUTTONUP, None, lParam)
        # time.sleep(0.5)
        # win32gui.PostMessage(self.hwnd2, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        # time.sleep(0.2)
        # win32gui.PostMessage(self.hwnd2, win32con.WM_LBUTTONUP, None, lParam)
        # time.sleep(0.5)
        # self.hwnd_sub = self.getInnerWindows(self.hwnd)["DirectUIHWND"]
        self.win = win32ui.CreateWindowFromHandle(self.hwnd)
        self.win.PostMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        time.sleep(0.1)
        self.win.PostMessage(win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
        time.sleep(0.1)
    # 실패
    def getCursorPosition(self):
        while True:
            print(win32api.GetCursorPos())
    # 실패
    def getInnerWindows(self, whndl):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                hwnds[win32gui.GetClassName(hwnd)] = hwnd
                print(hwnd)
            return True
        hwnds = {}
        win32gui.EnumChildWindows(whndl, callback, hwnds)
        return hwnds
    # def saveimage(hwndname =""):
    #     hwnd = win32gui.FindWindow(None, hwndname)
    #     if hwnd >= 1:
    #         left, top, right, bot = win32gui.GetWindowRect(hwnd)
    #         w = right - left
    #         h = bot - top
    #
    #         hwndDC = win32gui.GetWindowDC(hwnd)
    #         mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    #         saveDC = mfcDC.CreateCompatibleDC()
    #         saveBitMap = win32ui.CreateBitmap()
    #
    #         saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    #
    #         saveDC.SelectObject(saveBitMap)
    #
    #         result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    #
    #         bmpinfo = saveBitMap.GetInfo()
    #
    #         bmpstr = saveBitMap.GetBitmapBits(True)
    #
    #         im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    #
    #         win32gui.DeleteObject(saveBitMap.GetHandle())
    #
    #         saveDC.DeleteDC()
    #
    #         mfcDC.DeleteDC()
    #
    #         win32gui.ReleaseDC(hwnd, hwndDC)
    #
    #         im.save("asdf.png")


import getpass
las = {'processname': 'Jahwa LAS.exe',
        'filename_for_run': f'C:/Users/{getpass.getuser()}/AppData/Local/Jahwa_LAS_MAIN_MainShell/Jahwa LAS.exe',
        'hwnd_name': "JLAS (Gumi) Ver.1.0.42"}
hwnd = HWND(las['hwnd_name'])
hwnd.windowResize()