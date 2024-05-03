#GitHub Update 2024-05-03
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # 관리자 권한으로 실행 중일 때 수행할 작업
    pass
else:
    # 현재 프로그램 인스턴스를 관리자 권한으로 다시 실행
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)