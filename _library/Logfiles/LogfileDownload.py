from _library.functions.func_foldermake import FolderExists
import os
import shutil
from distutils.dir_util import copy_tree
import json

from PyQt5.QtCore import *

class LogDownload(QThread):
    flag = pyqtSignal(bool)
    msg = pyqtSignal(str)
    prog = pyqtSignal(bool, int)
    def __init__(self, date_list, mc_list, log_list, process_list, lotid_list, savepath):
        super().__init__()
        self.date_list = date_list
        self.mc_list=mc_list
        self.log_list=log_list
        self.process_list=process_list
        self.lotid_list=lotid_list
        self.savepath = savepath
        self.initials()
    def initials(self):
        self.all_paths = []
        self.all_files_size = 0
        self.mc_nums = ['MC1','MC2','MC3','MC4','MC5']
        self.process_names = ['Handler', 'Grease1', 'Ball1', 'XATT', 'Grease2','Ball2','YATT','ZSATT','Epoxy1','Epoxy2','UVINSP']
        self.log_names = ['SECSGEM','SeqLog','MMIOperationLog','MachineInfo','FiveKeyMatrix','SubMaterialLog']
        self.iplist = {
                        "MC1": {"Handler": "10.3.15.98",
                                "Grease1": "10.3.15.99",
                                "Ball1": "10.3.15.100",
                                "XATT": "10.3.15.101",
                                "Grease2": "10.3.15.102",
                                "Ball2": "10.3.15.103",
                                "YATT": "10.3.15.104",
                                "ZSATT": "10.3.15.105",
                                "Epoxy1": "10.3.15.106",
                                "Epoxy2": "10.3.15.107",
                                "UVINSP": "10.3.15.108"},
                        "MC2": {"Handler": "10.3.10.66",
                                "Grease1": "10.3.10.67",
                                "Ball1": "10.3.10.68",
                                "XATT": "10.3.10.69",
                                "Grease2": "10.3.10.70",
                                "Ball2": "10.3.10.71",
                                "YATT": "10.3.10.72",
                                "ZSATT": "10.3.10.73",
                                "Epoxy1": "10.3.10.74",
                                "Epoxy2": "10.3.10.75",
                                "UVINSP": "10.3.10.76"},
                        "MC3": {"Handler": "10.3.10.77",
                                "Grease1": "10.3.10.78",
                                "Ball1": "10.3.10.79",
                                "XATT": "10.3.10.80",
                                "Grease2": "10.3.10.81",
                                "Ball2": "10.3.10.82",
                                "YATT": "10.3.10.83",
                                "ZSATT": "10.3.10.84",
                                "Epoxy1": "10.3.10.85",
                                "Epoxy2": "10.3.10.86",
                                "UVINSP": "10.3.10.87"},
                        "MC4": {"Handler": "10.3.10.88",
                                "Grease1": "10.3.10.89",
                                "Ball1": "10.3.10.90",
                                "XATT": "10.3.10.91",
                                "Grease2": "10.3.10.92",
                                "Ball2": "10.3.10.93",
                                "YATT": "10.3.10.94",
                                "ZSATT": "10.3.10.95",
                                "Epoxy1": "10.3.10.96",
                                "Epoxy2": "10.3.10.97",
                                "UVINSP": "10.3.10.98"},
                        "MC5": {"Handler": "10.3.10.197",
                                 "Grease1": "10.3.10.198",
                                 "Ball1": "10.3.10.199",
                                 "XATT": "10.3.10.200",
                                 "Grease2": "10.3.10.201",
                                 "Ball2": "10.3.10.202",
                                 "YATT": "10.3.10.203",
                                 "ZSATT": "10.3.10.204",
                                 "Epoxy1": "10.3.10.205",
                                 "Epoxy2": "10.3.10.206",
                                 "UVINSP": "10.3.10.207"}
                    }
    def run(self):
        self.msg.emit(f'로그 다운로드를 시작합니다.')
        # 다운받을 설비 정리
        down_mclist = []
        for mc in range(len(self.mc_list)):
            if self.mc_list[mc]:
                down_mclist.append(self.mc_nums[mc])
        # 다운받을 프로세스 종류 정리
        down_processlist = []
        for p in range(len(self.process_list)):
            if self.process_list[p]:
                down_processlist.append(self.process_names[p])
        # 다운받을 로그파일 종류 정리
        down_loglist = []
        for l in range(len(self.log_list)):
            if self.log_list[l]:
                down_loglist.append(self.log_names[l])
        ########################################################
        count = 0
        total_count = len(down_mclist)*len(down_processlist)*len(self.date_list)*len(down_loglist)
        self.prog.emit(True, total_count)
        for mc in down_mclist:
            for process in down_processlist:
                for date in self.date_list:
                    yyyy = date.split('-')[0]
                    mm =  date.split('-')[1]
                    dd =  date.split('-')[2]
                    for log in down_loglist:
                        if log == "SECSGEM":
                            filepath = f'/log/{yyyy}{mm}{dd}'
                            self.find_copy(date, mc, process, log,r'\\' + self.iplist[mc][process] + filepath)
                        if log == "SeqLog":
                            filepath = f'/{log}/{yyyy}/{yyyy}-{mm}/{yyyy}-{mm}-{dd}'
                            self.find_copy(date, mc, process, log,r'\\' + self.iplist[mc][process] + filepath)
                        if log == "MMIOperationLog":
                            filepath = f'/{log}/{yyyy}/{yyyy}-{mm}/{yyyy}-{mm}-{dd}'
                            self.find_copy(date, mc, process, log,r'\\' + self.iplist[mc][process] + filepath)
                        if log == "MachineInfo":
                            filepath = f'/{log}'
                            self.find_copy(date, mc, process, log,r'\\' + self.iplist[mc][process] + filepath)
                        if log == "FiveKeyMatrix":
                            filepath = f'/{log}/{yyyy}-{mm}-{dd}'
                            self.find_copy(date, mc, process, log,r'\\' + self.iplist[mc][process] + filepath)
                        if log == "SubMaterialLog":
                            filepath = f'/{log}/{yyyy}-{mm}-{dd}'
                            self.find_copy(date, mc, process, log, r'\\' + self.iplist[mc][process] + filepath)
                        count += 1
                        self.prog.emit(False, count)
                        # print(f'\r진척사항 : {count}/{total_count}   ({round((count/total_count)*100,2)}%)', end="")
    def find_copy(self, date, mc, process, log, path):
        copy_list = []
        if log == "SECSGEM":
            if process != "Handler":
                return
        if log == "MachineInfo" or log == "FiveKeyMatrix" or log == "SubMaterialLog":
            for lotid in self.lotid_list:
                if lotid == "":
                    continue
                if len(self.lotid_list)==1 and lotid == "":
                    if log != "MachineInfo":
                        dst = f'{self.savepath}/{date}_{mc}/{process}/{log}'
                        path_lot = f'{path}'
                        if os.path.exists(path_lot):
                            copy_list.append(f'{path_lot}<:>{dst}')
                elif lotid[0] == 'G' and len(lotid) == 15:
                    dst = f'{self.savepath}/{date}_{mc}/{process}/{log}/{lotid}'
                    path_lot = f'{path}/{lotid}'
                    if os.path.exists(path_lot):
                        copy_list.append(f'{path_lot}<:>{dst}')
        else:
            dst = f'{self.savepath}/{date}_{mc}/{process}/{log}'
            copy_list = [f'{path}<:>{dst}']
        for linedata in copy_list:
            src = linedata.split("<:>")[0]
            dst = linedata.split("<:>")[1]
            try:
                self.msg.emit(f'[복사] {src}')
                copy_tree(src, dst)
            except:
                self.msg.emit(f'[복사 실패] {src}')
    def check_folder(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError:
            self.msg.emit(f'폴더 생성에 실패하였습니다. {path}를 확인해주세요.')


# if self.all_files_size >= 1000000000:
#     f_size = f'{round(self.all_files_size/1000000000,2)}GB'
# elif self.all_files_size >= 1000000:
#     f_size = f'{round(self.all_files_size/1000000,2)}MB'
# elif self.all_files_size >= 1000:
#     f_size = f'{round(self.all_files_size/1000,2)}KB'
# else:
#     f_size = f'{self.all_files_size}Byte'
# print(f'{len(self.all_paths)}개의 파일을 복사합니다. 전체 파일 크기 : {f_size}')
# self.msg.emit(f'{len(self.all_paths)}개의 파일을 복사합니다. 전체 파일 크기 : {f_size}')