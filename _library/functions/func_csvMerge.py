import os
from PyQt5.QtCore import *
class CSV_Merge(QThread):
    flag = pyqtSignal(bool)
    msg = pyqtSignal(str)
    prog = pyqtSignal(bool, int)
    def __init__(self, pathlist, save_path = "", save_filename='merge.csv'):
        super().__init__()
        self.pathlist = pathlist
        self.save_path = save_path
        self.save_filename = save_filename
    def run(self):
        self.msg.emit('CSV Merge 시작')
        self.prog.emit(True, len(self.pathlist))
        count = 1

        if self.save_path == "":
            savepath = os.path.dirname(self.pathlist[0])
        else:
            savepath = self.save_path
        print(f'{savepath}/{self.save_filename}')
        # File Path 분리
        with open(f'{savepath}/{self.save_filename}', 'w', encoding='utf-8') as outfile:
            for path in self.pathlist:
                filepath = os.path.dirname(path)
                filename = os.path.basename(path)
                self.msg.emit(f'파일을 읽고 있습니다. {filename}')
                try:
                    with open(os.path.join(filepath,filename), 'r', encoding='cp949') as infile:
                        for line in infile:
                            outfile.write(line)
                except:
                    with open(os.path.join(filepath,filename), 'r', encoding='utf-8') as infile:
                        for line in infile:
                            outfile.write(line)
                self.msg.emit(f'{filepath}/{filename}  {len(self.pathlist)} columns')
                self.prog.emit(False, count)
                count += 1
        self.flag.emit(True)


    def run2(self):
        self.msg.emit('CSV Merge 시작')
        self.prog.emit(True, len(self.pathlist))
        count = 1
        # File Path 분리
        for path in self.pathlist:
            filepath = os.path.dirname(path)
            filename = os.path.basename(path)
            self.msg.emit(f'파일을 읽고 있습니다. {filename}')
            try:
                with open(os.path.join(filepath,filename), 'r', encoding='cp949') as r:
                    readlines = r.readlines()
            except:
                with open(os.path.join(filepath,filename), 'r', encoding='utf-8') as r:
                    readlines = r.readlines()
            self.msg.emit(f'파일을 읽었습니다. {filename}')
            temp_data = ""



            linecount = 0
            for line in readlines:
                temp_data += line
                # print(f'\r({linecount}/{len(readlines)})',end="")
                if len(readlines) >= 10000 and linecount == 10000:

                    line_count = 0
                    temp_data = ""
                linecount += 1
            # print("")
            if self.save_path == "":
                savepath = filepath
            else:
                savepath = self.save_path

            if count == 0:
                writetype = 'w'
            else:
                writetype = 'a'
            try:
                with open(f'{savepath}/{self.save_filename}', writetype, encoding='cp949') as a:
                    a.writelines(temp_data)
            except:
                self.msg.emit('[decoder 변환] 한글 데이터는 깨질 수 있음.')
                with open(f'{savepath}/{self.save_filename}', writetype, encoding='utf-8') as a:
                    a.writelines(temp_data)

            self.msg.emit(f'{filepath}/{filename}  {len(self.pathlist)} columns')
            self.prog.emit(False, count)
            count += 1
        self.flag.emit(True)
    def str_strip(self, text) -> str:
        text = text.lstrip()
        return text.rstrip()

# path = "D:/20240303 ForceNG/2024-03-04"
# path = "D:/LogDownloader/20240319_MC1_(1)Handler_/SECSGEM/새 폴더"
# extension = ".LOG"
# a = CSV_Merge(path=path, extension=extension)



#
#
# def loadcell():
#     return '80eadata average'
# loadcell_data_list = []
# while True:
#     # 로드셀 호출 시 80개 평균을 call_loadcell 변수에 저장
#     call_loadcell = loadcell()
#     # 첫 번째 데이터를 원점(zero_data)으로 저장
#     zero_data = loadcell_data_list[0]
#     # 리스트 함수에 loadcell data를 추가
#     loadcell_data_list.append(call_loadcell)
#     # 원점과 현재 값을 비교해서 170 gf를 찾으면 종료
#     if call_loadcell - zero_data >= 170:
#         break
#
# def loadcell():
#     return '80eadata average'
# loadcell_data_list = []
# while True:
#     # 로드셀 호출 시 80개 평균을 call_loadcell 변수에 저장
#     call_loadcell = loadcell()
#     loadcell_data_list.append(call_loadcell)
#     # 데이터가 5개 모였을 시 1~5번 데이터의 메디안 값을 원점(zero_data)으로 저장
#     if len(loadcell_data_list) == 5:
#         zero_data = 메디안(loadcell_data_list[0],loadcell_data_list[1],loadcell_data_list[2],loadcell_data_list[3],loadcell_data_list[4])
#     # 데이터가 6개 이상일 때부터, 원점이 정해지므로 170gf 찾는 시퀀스 실행
#     if call_loadcell - zero_data >= 170:
#         break
#
