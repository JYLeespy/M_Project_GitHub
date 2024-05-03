import os

"D:/20240303 ForceNG/2024-03-03"
'''
TCAE04701E1AZ+335K5+B
TCAE047058AXZ+437N5+B
TCAE041023FQZ+437N5+B
TCAE04701DL9Z+335K5+B
TCAE04701DS0Z+335K5+B
TCAE0410237FZ+437N5+B
TCAE0410239LZ+437N5+B
'''


class Loadcell:
    def __init__(self, path_merged, oisids):
        self.path_merged = path_merged
        self.oisids = oisids

    def load(self, filepath) -> list:
        with open(filepath, 'r') as r:
            return r.readlines()
    def save(self, savedata):
        print(f'결과 저장 중')
        filepath = os.path.join(os.path.dirname(self.path_merged),"loadcell.csv")
        with open(filepath, 'w') as w:
            w.writelines(savedata)
        print(f'결과 저장 완료')

    def str_strip(self, text) -> str:
        text = text.lstrip()
        return text.rstrip()

    def indexing(self, data, find_text, text_length):
        index_data = data.find(find_text)
        if index_data != -1:
            result = data[index_data + len(find_text):index_data + len(find_text) + text_length]
            result = result.replace("=","")
            result = result.replace(" ", "")

            if find_text == "PlaceZPosition":
                find_condition2 = result.find(",")
                result = result[:find_condition2]
            elif find_text == "LoadCell":
                find_condition2 = result.find(":")
                result = result[:find_condition2]
                find_condition3 = result.find(",")
                result = result[:find_condition3]
            return result
        else:
            return ""
    def matching_oisid(self, dataline):
        for oisid in self.oisids:
            str_strip_oisid = self.str_strip(oisid)
            if dataline.find(str_strip_oisid) != -1:
                return True
        return False

    def run(self):
        print("Merged File 로딩 중...")
        read_file = self.load(self.path_merged)
        print("Merged File 로딩 완료")

        new_ = []
        find_time = ""
        find_moduleid = "ModuleID"
        find_zposition = "PlaceZPosition"
        find_loadcell = "LoadCell"

        self.new_data = []
        for line in read_file:
            if self.matching_oisid(line):
                find_INFO = line.find("INFO")
                find_ERROR = line.find("ERROR")
                datevalue = f'{line[:10]}'
                if find_INFO != -1:
                    timevalue = f"'{line[16:29]}"
                    moduleid = self.indexing(line, find_moduleid, 22)
                    zposition = self.indexing(line, find_zposition, 15)
                    loadcell = self.indexing(line, find_loadcell, 15)
                    if moduleid == "" or zposition == "" or loadcell == "":
                        pass
                    else:
                        new_text = f"{datevalue},{timevalue},INFO,{moduleid},{zposition},{loadcell}\n"#,{line}
                        # print(new_text)
                        self.new_data.append(new_text)
                elif find_ERROR != -1:
                    timevalue = f"'{line[17:30]}"
                    moduleid = self.indexing(line, find_moduleid, 22)
                    zposition = self.indexing(line, find_zposition, 15)
                    loadcell = self.indexing(line, find_loadcell, 15)
                    if moduleid == "" or zposition == "" or loadcell == "":
                        pass
                    else:
                        new_text = f"{datevalue},{timevalue},ERROR,{moduleid},{zposition},{loadcell}\n"#,{line}
                        # print(new_text)
                        self.new_data.append(new_text)


        self.save(self.new_data)


'''
path_seqlogs = "D:/20240303 ForceNG/2024-03-03/merged.csv"
path_seqlogs = "D:/20240303 ForceNG/2024-03-03/SeqLog.log-2024-03-03-00.log"
oisidlist = ['TCAE04701E1AZ+335K5+B\n', 'TCAE047058AXZ+437N5+B\n', 'TCAE041023FQZ+437N5+B\n',
             'TCAE04701DL9Z+335K5+B\n', 'TCAE04701DS0Z+335K5+B\n', 'TCAE0410237FZ+437N5+B\n',
             'TCAE0410239LZ+437N5+B\n']

'''
'''
TCAE047059M5Z+944T5+B
TCAE047046QXZ+944T5+B
TCAE041023FQZ+437N5+B
TCAE04701DL9Z+335K5+B
TCAE04701DS0Z+335K5+B
TCAE0410237FZ+437N5+B
TCAE0410239LZ+437N5+B
'''

print('''
# n a m e : Loadcell_SeqLog.exe
# made by : jylee (jylee@jahwa.co.kr)
# d a t e : 2024-03-14
# update  : 2024-03-14
# version : 0

프로그램이 실행되었습니다''')
while True:
    input_merged = ""
    input_merged = input("검색할 시퀀스로그 합쳐진 파일 경로를 입력하세요.(파일명, 확장자 포함)\n>>")

    while True:
        input("찾으려는 OISID를 복사한 후 엔터를 입력해주세요.\n>>")
        import clipboard
        copydata = clipboard.paste()
        print(copydata)
        oisidlist = copydata.split('\n')
        print(f'복사한 값이 (총 {len(oisidlist)}개) 위 데이터가 맞습니까? ')
        check = input("맞으면 실행(y) 아니면 재시도(n) 입력 후 엔터\n>>")
        if check == "y" or check == "Y":
            print('실행')
            break
    l = Loadcell(input_merged, oisidlist)
    l.run()