import psutil
import os
import subprocess

def process_list_print():
    for proc in psutil.process_iter():
        ps_name = proc.name()
        print(ps_name)

def process_check_run(check_ps_name, p_name):
    check_flag = False
    for proc in psutil.process_iter():
        ps_name = proc.name()
        if check_ps_name in ps_name:
            check_flag = True
            break
    if not check_flag:
        try:
            os.system(f'"{p_name}"')
        except:
            subprocess.Popen(p_name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        import time
        for i in range(5):
            print(f'\rProgram Running wait... {5-i}s', end="")
            time.sleep(1)
        print("")
    return check_flag
def kill_process(p_name):
    os.system(f'taskkill /f /im {p_name}')



# def run_process(p_name):
#     try:
#         os.system(f'"{p_name}"')
#     except:
#         subprocess.Popen(p_name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)





# process_list_print()


# run_process(f'C:/Users/{getpass.getuser()}/AppData/Local/Jahwa_LAS_MAIN_MainShell/Jahwa LAS.exe')
# 'Jahwa LAS.exe'
# print(process_list('LGIT.GMES.SFU.MainFrame.exe'))
# if process_list('EXCEL.EXE'):
#     kill_process('EXCEL.EXE')
# else:
#     run_process('calc.exe')