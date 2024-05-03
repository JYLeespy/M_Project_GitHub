from _library.functions.func_Excel import *

import shutil
import os

# ips
mc1_ip = '10.3.15.'
mc1 = 98
mc2_ip = '10.3.10.'
mc2 = 66
fivekey = 'FiveKeyMatrix'
datetime_ = '2024-03-'
datetime_period_from = 18
datetime_period_to = 24
filename = "ErrorLog.txt"
to_path = "D:/ProgramData/FiveKeyMatrix"

# for i in range(11):
#     for j in range(datetime_period_to-datetime_period_from+1):
#         print(f'{mc1_ip}{mc1 + i}/{datetime_}{datetime_period_from+j}/{filename}')
#         filepath = r'//'+f'{mc1_ip}{mc1 + i}/{fivekey}/{datetime_}{datetime_period_from+j}/{filename}'
#         topath = f'{to_path}/{datetime_}{datetime_period_from+j}_{i}설비.txt'
#         shutil.copyfile(filepath, topath)
    # os.listdir()




mclist = {'0':'Handler',
          '1':'Grease1',
          '2':'Ball1',
          '3':'XATT',
          '4':'Grease2',
          '5':'Ball2',
          '6':'YATT',
          '7':'ZSATT',
          '8':'EpoxyDisp1',
          '9':'EpoxyDisp2',
          '10':'UVInsp'}

basic_path = "D:/ProgramData/FiveKeyMatrix"
basic_filename = "계산파일.xlsx"
basic_filepath = os.path.join(basic_path, basic_filename)
excel = ExcelWings(basic_filepath)
for i in range(0,11):
    count = 2
    for j in range(datetime_period_to - datetime_period_from + 1):
        filename = f'{to_path}/{datetime_}{datetime_period_from + j}/{datetime_}{datetime_period_from + j}_{i}설비.txt'
        with open(filename, 'r', encoding='utf-8') as r:
            read_result = r.readlines()
        sheetname = mclist[f'{i}']
        for r in range(len(read_result)):
            data = read_result[r].lstrip()
            data = data.rstrip()
            excel.inputdata(sheetname=sheetname, cell=f'A{count}', data=data)
            count +=1
excel.save(f'{to_path}/NEW.xlsx')
excel.close()

# for j in range(datetime_period_to-datetime_period_from+1):
#     basic_path = "D:/ProgramData/FiveKeyMatrix"
#     basic_filename = "계산파일.xlsx"
#     basic_filepath = os.path.join(basic_path, basic_filename)
#     excel = ExcelWings(basic_filepath)
#
#     folders = os.listdir(f'{to_path}/{datetime_}{datetime_period_from + j}')
#     for infile in folders:
#         mc_number = infile[11]
#         if mc_number == '1' and infile[12] == '0':
#             mc = '10'
#         else:
#             mc = mc_number
#         sheetname = mclist[mc]
#
#         with open(f'{to_path}/{datetime_}{datetime_period_from + j}/{infile}', 'r', encoding='utf-8') as r:
#             read_result = r.readlines()
#
#
#         for r in range(len(read_result)):
#             data = read_result[r].lstrip()
#             data = data.rstrip()
#             excel.inputdata(sheetname=sheetname, cell=f'A{r+2}', data=data)
#
#     excel.save(f'{to_path}/{datetime_}{datetime_period_from + j}.xlsx')
#     excel.close()

# for j in range(datetime_period_to-datetime_period_from+1):
#     basic_path = "D:/ProgramData/FiveKeyMatrix"
#     basic_filename = "계산파일.xlsx"
#     basic_filepath = os.path.join(basic_path, basic_filename)
#     excel = ExcelWings(basic_filepath)
#
#     folders = os.listdir(f'{to_path}/{datetime_}{datetime_period_from + j}')
#     for infile in folders:
#         mc_number = infile[11]
#         if mc_number == '1' and infile[12] == '0':
#             mc = '10'
#         else:
#             mc = mc_number
#         sheetname = mclist[mc]
#
#         with open(f'{to_path}/{datetime_}{datetime_period_from + j}/{infile}', 'r', encoding='utf-8') as r:
#             read_result = r.readlines()
#
#
#         for r in range(len(read_result)):
#             data = read_result[r].lstrip()
#             data = data.rstrip()
#             excel.inputdata(sheetname=sheetname, cell=f'A{r+2}', data=data)
#
#     excel.save(f'{to_path}/{datetime_}{datetime_period_from + j}.xlsx')
#     excel.close()