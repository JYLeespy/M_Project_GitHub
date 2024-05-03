from _library.functions.func_Excel import *
import time


class NID_REPORT:
    def __init__(self, path="", basefilename="", logfilename="" , savepath=""):
        if path == "" or logfilename == "":
            # self.path = "D:/ProgramData/_project/M_Project/_download/2024-03-25_2024-03-26"
            self.path = "D:/ProgramData/새 폴더/2024-03-28_2024-03-29"
            self.logfile = '2024-03-28 0820_2024-03-29 0820 NG List Result.csv'
            self.filename = 'D:/ProgramData/새 폴더/기본양식파일.xlsm'
            self.savepath = '2024-03-28 0820_2024-03-29 0820 NG List Result.csv'
        else:
            self.path = path
            self.logfile = logfilename
            self.filename = basefilename
            self.savepath = savepath

        filepath = os.path.join(self.path, self.filename)
        self.excel = ExcelWings(filepath)
        self.get_ngnames_for_add_sheets("[EXCEL REPORT] #1 로그파일 읽고 불량명으로 시트 추가")
        # self.excel.save(saveas=new_file)
        self.image_insert("[EXCEL REPORT] #2 로그파일 읽기")
        self.excel.save(saveas=self.savepath)

    # [EXCEL REPORT] #1 초기설정
    def initial_sheets(self, sheetnames):
        first_row = ["생산 모듈","LOT ID","설비명","일자","예비용","모듈","판정","사유명","MGZ_Z","CARRIERID_Z","POCKET_Z","X_STAGE_PNP_CARRIER_MLOTID","MGZ_X","CARRIERID_X","POCKET_X","MODULE_Y","Y_STAGE_PNP_CARRIER_MLOTID","MGZ_Y","CARRIERID_Y","POCKET_Y","Z_STOPPER_PNP_CARRIER_MLOTID","MGZ_ZS","CARRIERID_ZS","POCKET_ZS","불량발생설비","불량코드","불량명"]
        cells_width = [20, 17, 11, 7, 2, 24, 6, 30, 10, 7, 2, 17, 10, 7, 2, 24, 17, 10, 7, 2, 17, 10, 7, 2, 18, 9, 32]
        cells_width_image = 56

        for sheetname in sheetnames:
            # 불량명으로 sheet 생성
            sheetadd_result = self.excel.sheetadd(sheetname, zoom=70)
            if sheetadd_result:
                self.excel.insert(sheetname, 'A1', first_row)
                #시트 생성 후 열 너비 설정
                for c in range(len(cells_width)):
                    self.excel.coumns_width(sheetname, f'{self.excel.convert_cols(c)}:{self.excel.convert_cols(c)}', cells_width[c])
                self.excel.coumns_width(sheetname,f'{self.excel.convert_cols(26)}:{self.excel.convert_cols(55)}',56)


        # 데이터종합시트
        sheetadd_result = self.excel.sheetadd("데이터 종합", zoom=70, showGrid=False)
        self.excel.insert("데이터 종합", 'A1', first_row)
        if sheetadd_result:
            for c in range(len(cells_width)):
                self.excel.coumns_width("데이터 종합", f'{self.excel.convert_cols(c)}:{self.excel.convert_cols(c)}', cells_width[c])

        # Summary Page
        # self.ngname_count = 0
        # self.excel.sheetadd("Summary", zoom=70, showGrid=False)
        # nglist = list(set(sheetnames))
        # zeropoint_qty = (1, 2) # A2
        # self.excel.insert("Summary", f'{self.excel.convert_cols(zeropoint_qty[0])}2', nglist)
        # for j in range(5):
        #     for i in range(len(nglist)):
        #         if i == 0:
        #             self.excel.inputdata("Summary",f'{self.excel.convert_cols(zeropoint_qty[0] - 1)}{zeropoint_qty[1] + j + 1} ',f"MC#{j + 1}")
        #         self.excel.formula("Summary",f"{self.excel.convert_cols(zeropoint_qty[0]+i)}{zeropoint_qty[1]+j+1}", f"=COUNTIF('{nglist[i][0:31]}'!C:C,"+f'"OIS Assy & Retainer Clip Attach #0{j+1}"')
        # self.excel.chart("Summary",f"{self.excel.convert_cols(zeropoint_qty[0]-1)}{zeropoint_qty[1]}:{self.excel.convert_cols(zeropoint_qty[0]-1+len(nglist))}{zeropoint_qty[1]+5}",f"{self.excel.convert_cols(zeropoint_qty[0]-1)}{zeropoint_qty[1]+6}",chart_height=200,chart_width=800)
        # self.excel.border("Summary",f"{self.excel.convert_cols(zeropoint_qty[0]-1)}{zeropoint_qty[1]}:{self.excel.convert_cols(zeropoint_qty[0]-1+len(nglist))}{zeropoint_qty[1]+5}")

    # [EXCEL REPORT] #2 LOGFILE 읽기
    def get_ngnames_for_add_sheets(self, description):
        print(description)
        filepath = os.path.join(self.path, self.logfile)
        ngnames = []
        with open(filepath, 'r') as r:
            read_lines = r.readlines()
        for i in range(len(read_lines)):
            line = read_lines[i]
            split_datas = line.split(',')
            moduleid = split_datas[0]
            if moduleid == "생산 모듈":
                continue
            ngnames.append(split_datas[7]) # sheet name
        # return ngnames
        self.initial_sheets(ngnames)
    # [EXCEL REPORT] #3 Image Insert
    def image_insert(self, description):
        print(description)
        filepath = os.path.join(self.path,self.logfile)
        with open(filepath, 'r') as r:
            read_lines = r.readlines()
        nglist_dict = {}
        for i in range(len(read_lines)):
            line = read_lines[i]
            split_datas = line.split(',')
            moduleid = split_datas[0]
            lotid = split_datas[1]
            mc = split_datas[2]
            oisid = split_datas[5]
            ngname = split_datas[7] # sheet name

            if moduleid == "생산 모듈" or oisid == "NoneModuleID":
                continue
            try:
                ng_count = nglist_dict[ngname]
                nglist_dict[ngname] = ng_count + 1
            except:
                self.excel.sheetadd(ngname)
                nglist_dict[ngname] = 1

            self.excel.insert(ngname, f'A{nglist_dict[ngname] + 1}', split_datas)
            self.excel.insert("데이터 종합", f'A{i+1}', split_datas)

            image_file_list = os.listdir(f'{self.path}/#{mc[-1:]}/{ngname}/{oisid}')
            mc_Barcode = []
            mc_Grease1 = []
            mc_Ball1 = []
            mc_XATT = []
            mc_Grease2 = []
            mc_Ball2 = []
            mc_YATT = []
            mc_ZSATT = []
            mc_Epoxy1 = []
            mc_Epoxy2 = []
            mc_UVInsp = []

            for image_file in image_file_list:
                if image_file.find('H01.jpg') != -1:
                    mc_Barcode.append(image_file)
                elif image_file.find('T01.jpg') != -1:
                    mc_Grease1.append(image_file)
                elif image_file.find('T02.jpg') != -1:
                    mc_Ball1.append(image_file)
                elif image_file.find('T03.jpg') != -1:
                    mc_XATT.append(image_file)
                elif image_file.find('T04.jpg') != -1:
                    mc_Grease2.append(image_file)
                elif image_file.find('T05.jpg') != -1:
                    mc_Ball2.append(image_file)
                elif image_file.find('T06.jpg') != -1:
                    mc_YATT.append(image_file)
                elif image_file.find('T07.jpg') != -1:
                    mc_ZSATT.append(image_file)
                elif image_file.find('T08.jpg') != -1:
                    mc_Epoxy1.append(image_file)
                elif image_file.find('T09.jpg') != -1:
                    mc_Epoxy2.append(image_file)
                elif image_file.find('T10.jpg') != -1:
                    mc_UVInsp.append(image_file)

            image_files_lists = mc_Barcode + mc_Grease1 + mc_Ball1  +mc_XATT +mc_Grease2+mc_Ball2+mc_YATT+mc_ZSATT+mc_Epoxy1+mc_Epoxy2+mc_UVInsp
            self.temp_dict = {}
            for i in range(len(image_files_lists)):
                image = image_files_lists[i]
                # self.get_data_from_filename(ngname, nglist_dict[ngname]+1, image)
                img_file = os.path.join(f'{self.path}/#{mc[-1:]}/{ngname}/{oisid}',image)

                # Image 넣기
                try:
                    self.excel.image_insert(img_file=img_file, sheetname=ngname, row=f'{self.excel.convert_cols(i + 28)}', col=nglist_dict[ngname] + 1, resize=['h', 400])
                except:
                    pass

                # Image 경로 넣기
                self.excel.insert(ngname, f'{self.excel.convert_cols(i+28)}{nglist_dict[ngname]+1}', [img_file])

            # Data 넣기
            # read_data = self.excel.readdata(ngname, f'A{nglist_dict[ngname]+1}:X{nglist_dict[ngname]+1}')
            # print(f'sheetname : {ngname} cell: A{nglist_dict[ngname]+1}:X{nglist_dict[ngname]+1}  read_data : {read_data}')




# report = NID_REPORT()








# def get_data_from_filename(self, ngname, row, filename):
#     # print(f'[get_data_from_filename]  sheetname : {ngname}  A{row}:X{row}')
#     read_data = self.excel.readdata(ngname, f'A{row}:X{row}')
#     # print(f'read_data = {read_data}')
#     oisid = read_data[5]
#
#     if filename.find('T03.jpg') != -1 and filename[37:39] == "2#":
#         column_indexs = [11, 12, 13]
#         for c in range(len(column_indexs)):
#             print(f'[{ngname}_{oisid}] X ATT : {read_data[column_indexs[c]]} / {type(read_data[column_indexs[c]])}')
#             if read_data[column_indexs[c]] == None or read_data[column_indexs[c]] == "":
#                 self.excel.inputdata(sheetname=ngname, cell=f'{self.excel.convert_cols(column_indexs[c] + 1)}{row}',data=filename[39:84].split("#")[c])
#                 print(f'[O] sheetname={ngname} cell={self.excel.convert_cols(column_indexs[c] + 1)}{row} data={filename[39:84].split("#")[c]}')
#             # else:
#             #     print(f'[N] sheetname={ngname} cell={self.excel.convert_cols(column_indexs[c] + 1)}{row} data={filename[39:84].split("#")[c]}')
#     elif filename.find('T06.jpg') != -1 and filename[37:39] == "3#":
#         column_indexs = [17, 18, 19, 15]
#         for c in range(len(column_indexs)):
#             print(f'[{ngname}_{oisid}] Y ATT : {read_data[column_indexs[c]]} / {type(read_data[column_indexs[c]])}')
#             if read_data[column_indexs[c]] == None or read_data[column_indexs[c]] == "":
#                 self.excel.inputdata(sheetname=ngname, cell=f'{self.excel.convert_cols(column_indexs[c] + 1)}{row}',data=filename[39:84].split("#")[c])
#                 print(f'[O] sheetname={ngname} cell={self.excel.convert_cols(column_indexs[c] + 1)}{row} data={filename[39:84].split("#")[c]}')
#             # else:
#             #     print(f'[N] sheetname={ngname} cell={self.excel.convert_cols(column_indexs[c] + 1)}{row} data={filename[39:84].split("#")[c]}')
#     elif filename.find('T07.jpg') != -1 and filename[37:39] == "4#":
#         column_indexs = [21, 22, 23]
#         for c in range(len(column_indexs)):
#             print(f'[{ngname}_{oisid}] ZS ATT : {read_data[column_indexs[c]]} / {type(read_data[column_indexs[c]])}')
#             if read_data[column_indexs[c]] == None or read_data[column_indexs[c]] == "":
#                 self.excel.inputdata(sheetname=ngname, cell=f'{self.excel.convert_cols(column_indexs[c] + 1)}{row}',data=filename[39:84].split("#")[c])
#                 print(f'[O] sheetname={ngname} cell={self.excel.convert_cols(column_indexs[c] + 1)}{row} data={filename[39:84].split("#")[c]}')
#             else:
#                 print(f'[N] sheetname={ngname} cell={self.excel.convert_cols(column_indexs[c] + 1)}{row} data={filename[39:84].split("#")[c]}')
