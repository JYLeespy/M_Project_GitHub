#
# a = ['a', 'b', 'c']
#
# b = 'a'
#
# if b in a:
#     print(True)
# else:
#     print(False)

count = 0
repeat = 5
while count < repeat:
    print(count)
    count += 1

#
# a = [40 * 5]
# print(a)

# column_trans = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#                 'V', 'W', 'X', 'Y', 'Z']
#
# cell = 'B5'  #705
# digit = len(cell)
#
# col_num = 0
# for c in range(len(cell)):
#     r = len(cell)-c-1
#     col_num += (26**c)*(column_trans.index(cell[r])+1)
# return col_num


# insertcount = 3
# col = 2 # B
# row = 5 # 5
# imagedatas = 60
# insert_col = col
# insert_row = row
# for i in range(imagedatas):
#     col_num = i%insertcount
#     col = insert_col + col_num
#     if col_num == 0:
#         row += 1
#     print(f'col:{col}  row:{row},  insert_col:{insert_col}   col_num:{col_num}')


# import os
#
# path = 'D:/ProgramData/Project/M_Project/_logdownload/2024-03-16_MC4/UVINSP/FiveKeyMatrix'
# savepath = 'D:/ProgramData/_project/M_Project/_logdownload'
#
# files = os.listdir(path)
#
# print(files)
# temp = ""
#
# for i in files:
#     filepath = f'{path}/{i}/TrayInOutLog.txt'
#     with open(filepath, 'r', encoding='utf-8') as r:
#         read_line = r.readlines()
#     for line in read_line:
#         temp += line
#
# print(temp)
#
# with open(f'{savepath}/merge.txt', 'a') as a:
#     a.write(temp)
# # import os
# path = '\\\\'+'10.3.15.98/FiveKeyMatrix/2024-04-01'
# topath = 'D:/ProgramData/_project/M_Project/2024-04-01'
#
# l = os.listdir(path)
# print(l)
# # import shutil
# from distutils.dir_util import copy_tree
# copy_tree(path,topath)
# # copy2(path,topath)


# import os
# class A:
#     def __init__(self, path):
#         las_files = os.listdir(path)
#
#         for las_file in las_files:
#             if las_file[-4:] == ".csv":
#                 pass
#             else:
#                 continue
#             mc = ''
#             if "BCR" in las_file:
#                 mc = "BCR"
#             elif "XAT" in las_file:
#                 mc = "XAT"
#             elif "YAT" in las_file:
#                 mc = "YAT"
#             elif "ZAT" in las_file:
#                 mc = "ZAT"
#
#             with open (path + "/" + las_file, 'r') as r:
#                 datas = r.readlines()
#                 # print(f'datas : {datas}')
#
#             index = [0, 1, 8, 9, 11, 12, 13, 16, 17, 18, 21]
#             newdata = []
#             for data in datas:
#                 newdatas = data.split(",")
#                 if newdatas[0] == "TIME":
#                     continue
#                 tempdata = ""
#                 for i in index:
#                     if i == 21:
#                         tempdata += newdatas[i] + "\n"
#                     else:
#                         tempdata += newdatas[i] + ","
#                 newdata.append(tempdata)
#
#
#             with open(f'{mc}.txt', 'a' ) as a:
#                 a.writelines(newdata)
#             # self.savefile(self.path_las_merged, f'{mc}.txt', newdata, 'a')
# path = "D:/ProgramData/_project\M_Project/_download/새 폴더/2024-02-26_2024-02-27/"
# a = A(path)