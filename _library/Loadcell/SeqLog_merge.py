import os
print('''
# n a m e : SeqLog_Merge.exe
# made by : jylee (jylee@jahwa.co.kr)
# d a t e : 2024-03-14
# update  : 2024-03-14
# version : 0

프로그램이 실행되었습니다''')

while True:
    path = input("SeqLog.log 파일 경로를 입력하세요. \n>>")
    files = os.listdir(path)
    logfile_list = []
    for file in files:
        if file.find("SeqLog") != -1 and file.find(".log") != -1:
            logfile_list.append(os.path.join(path, file))
    if len(logfile_list) == 0:
        print("해당 경로에서 Seq Logfile을 찾지 못했습니다.\n1. 파일명에 SeqLog 포함\n2. 파일확장자 : .log")
        continue
    else:
        break
print('파일 읽기')
buffer = []
for logfile in logfile_list:
    print(f'파일경로 : {logfile}')
    with open(logfile, 'r') as r:
        file_read_lines = r.readlines()
    for line in file_read_lines:
        buffer.append(line)
print('파일 저장')
with open(path+"/SeqLog_merged.csv", 'w') as w:
    w.writelines(buffer)
print('파일 저장 완료')
print('')
input('Press any key to Continue')
os.system('pasue')