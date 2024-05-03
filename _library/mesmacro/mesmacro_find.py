import os

class EMPTY:
    def __init__(self, basic_filename, mes_filename, mes_data_path, las_path, filename_las_image):
        super().__init__()
        self.filename = basic_filename

        self.mes_filename = mes_filename

        self.path_las = las_path
        # self.path_las = "./_data/LAS Data/"

        self.path_las_merged = self.path_las+'/merged/'
        # self.path_las_merged = "./_data/LAS Data/merged/"

        self.path_las_image = self.path_las
        # self.path_las_image = "./_data/LAS Image Data/"

        self.las_image_filename = filename_las_image

        self.path_mes = mes_data_path
        # self.path_mes = "./_data/MES Data/"
    def paths(self):
        # self.path_las = "./_data/LAS Data/"
        # self.path_las_merged = "./_data/LAS Data/merged/"
        # self.path_las_image = "./_data/LAS Image Data/"
        # self.path_mes = "./_data/MES Data/"
        # self.path_las = "./_data/RESULT/"

        # 아웃룩 저장 주소
        self.outlook_result = './_data/Outlook Data/'

    # Global Function       ########################################################################################################################################################################################
    # 파일 읽기
    def openfile(self, path):
        with open(path, 'r', encoding="utf-8") as f:
            return f.readlines()
    def savefile(self, path, filename, data, writetype):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError:
            print(f'폴더 생성에 실패하였습니다. {path}를 확인해주세요.')
        try:
            with open(path + filename, writetype, encoding="utf-8") as f:
                return f.writelines(data)
        except:
            print("파일저장에 실패하였습니다. 파일이 열려 있는 지 확인하세요.")

    def str_strip(self, text):
        strip = text.lstrip()
        text = strip.rstrip()
        return text

    def data_inspection(self, data, data_type):
        empty_index_name = ["ZTRAY", "ZPOCKET", "XMGZ", "XTRAY", "XPOCKET", "YID", "YMGZ", "YTRAY", "YPOCKET", "ZSMGZ",
                            "ZSTRAY", "ZSPOCKET"]

    ########################################################################################################################################################################################
    # 1. MES Data 정리 비어 있는 정보 정리
    def mes_data_arrange(self) -> list:
        print('#1 mes_data_arrange')
        filename = self.mes_filename
        if filename == "" or filename[-4:] != ".csv":
            print("파일명 확인 !!")
        else:
            # 파일 읽기 (MES 에서 다운 받은 파일)
            read_mesQuery = self.openfile(self.path_mes + filename)

            #파일명이 잘못 됐을 경우 self.openfile 에서 "" return.
            if read_mesQuery == "":
                return []

            print(f'MES 파일 읽기 성공')
            print(f'{len(read_mesQuery)}줄의 데이터 행을 읽었습니다.')

            # 1-1 파일에서 누락된 행만 추출하기
            empty_datas = self.check_empty_datas(read_mesQuery)  # 1-1
            print("MES 파일에서 누락된 행만 추출 완료")
            print(f'{len(empty_datas)}의 누락된 행을 찾았습니다.')
            # Lot id저장
            print("LOT ID를 수집합니다.")
            list_lots = []
            for empty_data in empty_datas:
                lotid = empty_data.split(",")[1] + "\n"
                if lotid != "":
                    if "LOT ID" in lotid:
                        pass
                    else:
                        list_lots.append(lotid)
            # 중복값제거
            list_lots = list(set(list_lots))
            self.savefile(self.path_las_image, "lotid.txt", list_lots, "w")

            print(f'누락된 Lot 번호만 분류하여 저장 : LAS Image Data/lotid.txt')

            # 1-2 MES에서 Export한 결과를 누락된 항목만 분류하고, 잘못 들어가있는 경우에는 빼서 MES Data 폴더에 result 문구를 붙여서 새로 저장함.
            empty_datas = self.check_empty_datas(empty_datas)  # 1-2
            self.savefile(self.path_mes, "filter_" + filename, empty_datas, 'w')
        return empty_datas
    def check_empty_datas(self, datas) -> list:
        print('check_empty_datas')
        result = []
        # 한 줄씩 데이터
        for data in datas:
            split_datas = data.split(",")
            new_data = ""
            for i in range(len(split_datas)):
                split_data = self.str_strip(split_datas[i])

                # print(f'{i} : {split_datas[i]}')
                if split_datas[i] != "" and self.check_cols(self.col_no[i], split_data):
                    new_data += split_data
                else:
                    new_data += ""

                if i == 17:
                    new_data += "\n"
                    # print(f'new_data : {new_data}')
                    result.append(new_data)
                else:
                    new_data += ","

        return result
    def check_cols(self, data_type, data) -> bool:
        filter_dict = {'MODULEID': {'len': 18, 'text': 'GP8'},
                       'LOTID': {'len': 15, 'text': 'GP4'},
                       'OISID': {'len': 21, 'text': 'TCA'},
                       'MGZ': {'len': 9, 'text': 'ABX'},
                       'YMGZ': {'len': 9, 'text': 'ABU'},
                       'ZTRAY1': {'len': 6, 'text': 'FX'},
                       'ZTRAY2': {'len': 6, 'text': 'FQ'},
                       'XTRAY': {'len': 6, 'text': 'FH'},
                       'YTRAY': {'len': 6, 'text': 'FG'},
                       'ZSTRAY': {'len': 6, 'text': 'FJ'}}

        data = self.str_strip(data)
        try:
            if data_type == "ZTRAY":
                data_len1 = len(filter_dict['ZTRAY1']['text'])
                data_text1 = filter_dict['ZTRAY1']['text']
                data_len2 = len(filter_dict['ZTRAY2']['text'])
                data_text2 = filter_dict['ZTRAY2']['text']
                if len(data) == filter_dict['ZTRAY1']['len'] and data[0:data_len1] == data_text1:
                    # print(f'True : {data_type},  {data}')
                    return True
                elif len(data) == filter_dict['ZTRAY2']['len'] and data[0:data_len2] == data_text2:
                    # print(f'True : {data_type},  {data}')
                    return True
                else:
                    # print(f'False : {data_type},  {data}')
                    return False
            else:
                data_len = len(filter_dict[data_type]['text'])
                data_text = filter_dict[data_type]['text']
                if len(data) == filter_dict[data_type]['len'] and data[0:data_len] == data_text:
                    # print(f'True : {data_type},  {data}')
                    return True
                else:
                    # print(f'False : {data_type},  {data}')
                    return False
        except:
            # print(f'False : {data_type},  {data}')
            return True


    # 2. LAS Image Data 정리
    def lasimg_data_arrange(self) -> dict:
        print('#2 lasimg_data_arrange')
        dict_for_save = {}
        with open(self.path_las_image + self.las_image_filename, 'r', encoding='utf-8') as r:
            lasimage_copydata_list = r.readlines()

        for data in lasimage_copydata_list:
            split_data = data.split('\t')


            if split_data[0] == 'Checked':
                mc = self.str_strip(split_data[2])
                lotid = self.str_strip(split_data[4])
                inspection = self.str_strip(split_data[6])
                moduleid = self.str_strip(split_data[7])

                filter1 = inspection.find("Sub")
                filter2 = inspection.find("#4#0")
                if filter1 == -1 and filter2 != -1:
                    if inspection[0:2] == "FX" or inspection[0:2] == "FQ":
                        ztray = inspection[0:6]
                        zpocket = inspection[7:9]
                        key = f'{lotid}_{ztray}_{zpocket}'
                        try:
                            temp_list = dict_for_save[key]
                        except:
                            dict_for_save[key] = ["", "", "", ""]
                            temp_list = dict_for_save[key]

                        if len(moduleid) >= 20:
                            temp_list[0] = moduleid

                        end_index = inspection.find("#4#0")
                        if "X-Stage" in mc:
                            temp_list[1] = inspection[12:end_index].replace("#", ",")

                        elif "Y-Stage" in mc:
                            temp_list[2] = inspection[12:end_index].replace("#", ",")

                        elif "Z-Stopper" in mc:
                            temp_list[3] = inspection[12:end_index].replace("#", ",")

                        dict_for_save[key] = temp_list

        list_for_save = []
        for i in dict_for_save:
            lotid = i.split("_")[0]
            zTRAY = i.split("_")[1]
            zPOCKET = i.split("_")[2]

            module = dict_for_save[i][0]

            # init
            xMGZ = ""
            xTRAY = ""
            xPOCKET = ""
            yMGZ = ""
            yTRAY = ""
            yPOCKET = ""
            yMODULE = ""
            zsMGZ = ""
            zsTRAY = ""
            zsPOCKET = ""

            # X
            x_info = dict_for_save[i][1]
            try:
                xMGZ = x_info.split(',')[0]
                xTRAY = x_info.split(',')[1]
                if xTRAY.find("TRAY") != -1:
                    xTRAY = ""
                xPOCKET = x_info.split(',')[2]
            except:
                pass
            # Y
            y_info = dict_for_save[i][2]
            try:
                yMGZ = y_info.split(',')[0]
                yTRAY = y_info.split(',')[1]
                if yTRAY.find("TRAY") != -1:
                    yTRAY = ""
                yPOCKET = y_info.split(',')[2]
                yMODULE = y_info.split(',')[3]
            except:
                pass
            # ZS
            zs_info = dict_for_save[i][3]
            try:
                zsMGZ = zs_info.split(',')[0]
                zsTRAY = zs_info.split(',')[1]
                if zsTRAY.find("TRAY") != -1:
                    zsTRAY = ""
                zsPOCKET = zs_info.split(',')[2]
            except:
                pass

            zsPOCKET += "\n"
            result = f'{lotid},{module},{zTRAY},{zPOCKET},{xMGZ},{xTRAY},{xPOCKET},{yMODULE},{yMGZ},{yTRAY},{yPOCKET},{zsMGZ},{zsTRAY},{zsPOCKET}'
            # print(result)
            list_for_save.append(result)

        self.savefile(self.path_las_image, 'result.txt', list_for_save, 'w')

        lasimg_datas_dict = {}
        for data in list_for_save:
            split_datas = data.split(",")
            lotid = split_datas[0]
            oisid = split_datas[1]
            ztray = split_datas[2]
            zpocket = split_datas[3]
            if oisid != "":
                key = oisid
            else:
                key = f'{lotid}_{ztray}_{zpocket}'

            # OIS ID로 key 생성해서 데이터 저장
            lasimg_datas_dict[key] = {"ZTRAY": split_datas[2],
                                      "ZPOCKET": split_datas[3],
                                      "XMGZ": split_datas[4],
                                      "XTRAY": split_datas[5],
                                      "XPOCKET": split_datas[6],
                                      "YID": split_datas[7],
                                      "YMGZ": split_datas[8],
                                      "YTRAY": split_datas[9],
                                      "YPOCKET": split_datas[10],
                                      "ZSMGZ": split_datas[11],
                                      "ZSTRAY": split_datas[12],
                                      "ZSPOCKET": split_datas[13]}

        return lasimg_datas_dict

    # 3. MES Data 누락항목 LAS Image DATA에서 정보 찾기
    def search_on_lasimg_data(self, data_lines, lasimg_datas_dict):
        print('#3 search_on_lasimg_data')
        # data 순서
        new_data = []
        new_data_line = ""
        empty_index_name = ["ZTRAY", "ZPOCKET", "XMGZ", "XTRAY", "XPOCKET", "YID", "YMGZ", "YTRAY", "YPOCKET", "ZSMGZ",
                            "ZSTRAY", "ZSPOCKET"]
        # "PROD_MODULEID	LOT ID	모듈ID	일자	JUDGE	OISASSY_MGZID	OISASSY_TRAYID	OISASSY_POCKETID	XSTAGE_MGZID	XSTAGE_TRAYID	XSTAGE_POCKETID	YSTAGE_MODULEID	YSTAGE_MGZID	YSTAGE_TRAYID	YSTAGE_POCKETID	Z-Stopper_MGZID	Z-Stopper_TrayID	Z-Stopper_PocketID
        print("search_on_lasimg_data")
        for data_line in data_lines:
            strip_data = self.str_strip(data_line)
            split_datas = strip_data.split(",")

            if split_datas[0] != "":
                # 새로운 데이터에 기존 데이터를 일단 넣어준다.
                new_data_line = f'{split_datas[0]},{split_datas[1]},{split_datas[2]},{split_datas[3]},{split_datas[4]},{split_datas[5]}'
                # 한줄 한줄씩 진행, 한 줄 내 비어있는 index 조사
                empty_count = 0
                for i in range(6, len(split_datas)):
                    if split_datas[i] == "" or split_datas[i].find("\n") != -1:
                        empty_name = empty_index_name[i - 6]
                        # define index
                        lotid = split_datas[1]
                        oisid = split_datas[2]
                        oistrayid = split_datas[6]
                        oispocketid = split_datas[7]

                        key1 = oisid
                        key2 = f'{lotid}_{oistrayid}_{oispocketid}'
                        try:
                            try:
                                # print(f'{i} : {self.lasimg_datas_dict[key1]}')
                                new_data_line += self.lasimg_data_filtering(i, lasimg_datas_dict[key1][empty_name])
                                # new_data_line += f',{lasimg_datas_dict[key1][empty_name]}'
                            except:
                                # print(f'{i} : {self.lasimg_datas_dict[key2]}')
                                # new_data_line += f',{lasimg_datas_dict[key2][empty_name]}'
                                new_data_line += self.lasimg_data_filtering(i, lasimg_datas_dict[key2][empty_name])
                        except:
                            new_data_line += ","
                            # print(f'Data not found : {key1}  {key2}')
                    else:
                        new_data_line += f',{split_datas[i]}'
                    new_data_line = self.str_strip(new_data_line)
                    # print(new_data_line)
            else:
                # 초기화
                new_data_line = ""
            new_data_line += "\n"
            new_data.append(new_data_line)
            new_data_line = ""

        self.result_filename = f'result1_{self.filename}.csv'
        self.savefile(self.path_las, self.result_filename, new_data, 'w')

    # 3-1 LAS 이미지 데이터를 넣기 전에 필터링한다.
    def lasimg_data_filtering(self, i, data) -> str:
        filter_dict = {'Moudle': {'len': 21, 'text': 'TCAD'},
                       'Magazine': {'len': 9, 'text': 'ABX'},
                       'YMagazine': {'len': 9, 'text': 'ABU'},
                       'ZTray1': {'len': 6, 'text': 'FX'},
                       'ZTray2': {'len': 6, 'text': 'FQ'},
                       'XTray': {'len': 6, 'text': 'FH'},
                       'YTray': {'len': 6, 'text': 'FG'},
                       'ZSTray': {'len': 6, 'text': 'FJ'}}

        key = ""
        if i == 2 or i == 11:
            key = 'Module'
        elif i == 5 or i == 8 or i == 15:
            key = 'Magazine'
        elif i == 12:
            key = 'YMagazine'
        elif i == 9:
            key = 'XTray'
        elif i == 13:
            key = 'YTray'
        elif i == 16:
            key = 'ZSTray'

        if i == 6:
            digit = len(filter_dict['ZTray1']['text'])
            if len(data) == filter_dict['ZTray1']['len'] and data[0:digit] == filter_dict['ZTray1']['text']:
                return f',{data}'
            elif len(data) == filter_dict['ZTray2']['len'] and data[0:digit] == filter_dict['ZTray2']['text']:
                return f',{data}'
            else:
                return ','

        digit = len(filter_dict[key]['text'])
        # 지정한 글자수와 시작 텍스트를 맞추는 과정.
        if len(data) == filter_dict[key]['len'] and data[0:digit] == filter_dict[key]['text']:
            # print(f'okay {key} : {data}')
            return f',{data}'
        else:
            # print(f'fail {key} : {data}')
            return ','

    # 4. #3에서 완료된 file 기반으로, LAS Data에서 한 번 더 누락된 항목 찾아서 기입하기
    def search_on_las_data(self):
        print('#4 search_on_las_data')
        import time
        print('Wait 3 ...')
        time.sleep(1)
        print('Wait 2 ...')
        time.sleep(1)
        print('Wait 1 ...')
        time.sleep(1)

        self.dict_BCR = {}
        self.dict_XAT = {}
        self.dict_YAT = {}
        self.dict_ZAT = {}

        path = self.path_las_merged
        submaterials = ['BCR', 'XAT', 'YAT', 'ZAT']

        # "D:\ProgramData\_project\M_Project\_data\mesmacro\las\20240305_\merged"
        # 'D:\ProgramData\_project\M_Project\_data/mesmacro/las/20240305_/merged/BCR.txt'
        # fail_count = 0
        # while True:
        #     try:
        #         read_test = self.openfile(f'{path}{submaterials[0]}.txt')
        #         print(f'path : {path}')
        #         break
        #     except:
        #         print(f'{fail_count} ')
        #         fail_count += 1
        #         time.sleep(1)
        #         pass

        for submaterial in submaterials:
            print(self.path_las)
            self.las_getFilelist(self.path_las)
            try:
                read_las_log = self.openfile(f'{path}{submaterial}.txt')
                print(f'try {submaterial} : {len(read_las_log)}')
            except:
                # self.las_getFilelist(self.path_las)
                read_las_log = self.openfile(f'{path}{submaterial}.txt')
                print(f'except {submaterial} : {len(read_las_log)}')

            # make dict
            for las_log in read_las_log:
                lotid = las_log.split(",")[2]
                oisid = las_log.split(",")[3]
                zmgz = las_log.split(",")[4]
                ztray = las_log.split(",")[5]
                zpocket = las_log.split(",")[6]

                if oisid == "":
                    key = f'{lotid}_{ztray}_{zpocket}'
                else:
                    key = oisid

                if submaterial != "BCR":
                    submgz = las_log.split(",")[7]
                    subtray = las_log.split(",")[8]
                    subpocket = las_log.split(",")[9]
                    subid = las_log.split(",")[10]

                if submaterial == 'BCR':
                    text = f'{zmgz},{ztray},{zpocket},{oisid}'
                    self.dict_BCR[key] = text
                elif submaterial == 'XAT':
                    text = f'{submgz},{subtray},{subpocket}'
                    self.dict_XAT[key] = text
                elif submaterial == 'YAT':
                    text = f'{subid},{submgz},{subtray},{subpocket}'
                    self.dict_YAT[key] = text
                elif submaterial == 'ZAT':
                    text = f'{submgz},{subtray},{subpocket}'
                    self.dict_ZAT[key] = text

        # self.result_filename = "result_4.csv"

        # result 파일읽기
        print('result 파일 읽기')
        read_result_file = self.openfile(self.path_las + "/" + self.result_filename)

        new_data = []
        new_line = ""
        for i in range(len(read_result_file)):

            find_empty_cols = read_result_file[i].split(",")

            if len(find_empty_cols) < 18:
                continue

            lotid = find_empty_cols[1]
            tray = find_empty_cols[6]
            pocket = find_empty_cols[7]
            oisid = find_empty_cols[2]
            if oisid == "":
                key = f'{lotid}_{tray}_{pocket}'
            else:
                key = oisid

            new_line = f'{find_empty_cols[0]},{find_empty_cols[1]},{find_empty_cols[2]},{find_empty_cols[3]},{find_empty_cols[4]}'
            for col in range(6, len(find_empty_cols)):

                data = self.str_strip(find_empty_cols[col])

                if data == "":
                    try:
                        data, minus = self.dict_search(self.data_range(col), key)
                        # print(f'key : {key}   data : {data},   {col-minus}    {data.split(",")[col-minus]} ')
                        new_line += f',{data.split(",")[col - minus]}'
                    except:
                        new_line += f',{data}'
                else:
                    new_line += f',{data}'

            filtering = new_line.find('\n')
            if filtering != -1:
                new_line = new_line.replace('\n', '')
            new_line += "\n"

            # new_line = find_empty_cols[0]
            # for col in range(1,len(find_empty_cols)):
            #     new_line += f',{find_empty_cols[col]}'
            # new_line += "\n"

            new_data.append(new_line)

        self.savefile(self.path_las, f'result2_{self.filename}OIS Assembly.csv', new_data, 'w')
        os.startfile(self.path_las)
        print("실행 완료")

    # 2. LAS 로그 합치기 ###################
    def las_getFilelist(self, path):
        las_files = os.listdir(path)
        print(f'las_files : {las_files}')
        for las_file in las_files:
            if las_file[-4:] == ".csv":
                pass
            else:
                continue
            mc = ''
            if "BCR" in las_file:
                mc = "BCR"
            elif "XAT" in las_file:
                mc = "XAT"
            elif "YAT" in las_file:
                mc = "YAT"
            elif "ZAT" in las_file:
                mc = "ZAT"

            datas = self.openfile(path + "/" + las_file)
            # print(f'datas : {datas}')

            index = [0, 1, 8, 9, 11, 12, 13, 16, 17, 18, 21]
            newdata = []
            for data in datas:
                newdatas = data.split(",")
                if newdatas[0] == "TIME":
                    continue
                elif len(newdatas) > 5:
                    tempdata = ""
                    for i in index:
                        # print(f'{i}, {len(newdatas)}')
                        try:
                            if i == 21:
                                tempdata += newdatas[i] + "\n"
                            else:
                                tempdata += newdatas[i] + ","
                        except:
                            pass
                    newdata.append(tempdata)

            self.savefile(self.path_las_merged, f'{mc}.txt', newdata, 'a')

    def dict_search(self, process, oisid):

        if process == "BCR":
            return self.dict_BCR[oisid], 5
        elif process == "XAT":
            return self.dict_XAT[oisid], 8
        elif process == "YAT":
            return self.dict_YAT[oisid], 11
        elif process == "ZAT":
            return self.dict_ZAT[oisid], 15

    def data_range(self, no):
        if no >= 5 and no <= 7:
            return 'BCR'
        elif no >= 8 and no <= 10:
            return 'XAT'
        elif no >= 11 and no <= 14:
            return 'YAT'
        elif no >= 15 and no <= 17:
            return 'ZAT'

    ########################################################################################################################################################################################

    def run(self):
        print('[찾기] 시퀀스 시작 ################################################')

        # data 순서
        self.col_no = ["MODULEID", "LOTID", "OISID", "DATETIME", "JUDEGE", "MGZ", "ZTRAY", "ZPOCKET", "MGZ", "XTRAY",
                       "XPOCKET", "YID", "YMGZ", "YTRAY", "YPOCKET", "MGZ", "ZSTRAY", "ZSPOCKET"]

        # 순서 재 정립.
        # 1. MES Data 정리 비어 있는 정보 정리
        mes_empty_datas = self.mes_data_arrange()
        if mes_empty_datas == []:
            return
        # 2. LAS Image Data 정리
        lasimg_datas_dict = self.lasimg_data_arrange()

        # 3. MES Data 누락항목 LAS Image DATA에서 정보 찾기
        self.search_on_lasimg_data(mes_empty_datas, lasimg_datas_dict)

        # 4. LAS Data 정리 (Merge 등)
        self.search_on_las_data()

        # 5. #4 완료 후 비어있는 항목 las DATA에서 정보 찾기



        print('[찾기] 시퀀스 완료 ################################################')

    def convertData(self, copydata):
        # print(f'convertData : {copydata}')
        splitdatas = copydata.split("\n")
        # data = {'zInfo':'', 'subMaterial':''}
        data = {}
        for splitdata in splitdatas:
            try:
                category = splitdata.split('\t')
                mc = category[2]
                lotid = category[4]
                subMaterial = category[6]
                barcode = category[7]
                if barcode == "BarcodeID":
                    barcode = ""
                # Z-Stopper Log의 경우 LAS-검사항목이 ALIG1 에 SubMaterial 정보가 남음.
                inspectionFilter = ""
                if "T03" in mc or "T06" in mc:
                    inspectionFilter = "INSP1"
                if "T07" in mc:
                    inspectionFilter = "ALIG1"
                # Z-Stopper Log의 경우 불필요한 로그도 같이 남음... 이 경우에는 필터링 하도록
                if "SubMaterialsID" in subMaterial or lotid[0] != "G" or subMaterial[0] != 'F':
                    continue

                if inspectionFilter in subMaterial:
                    if subMaterial[0:6] == "검사항목":
                        continue

                    subMaterialsplit = subMaterial.split("-")

                    z_tray = subMaterialsplit[0]
                    z_pocket = subMaterialsplit[1]
                    keydata = f'{z_tray}-{z_pocket}'

                    subMaterialInfo = subMaterialsplit[2]
                    subMaterialInfo = subMaterialInfo.split("#")
                    subMGZ = subMaterialInfo[1]
                    subTray = subMaterialInfo[2]
                    subPocket = subMaterialInfo[3]

                    if "#" in subPocket:
                        subPocket = subPocket[0]

                    try:
                        oldList = data[keydata]
                        # print(len(oldList))
                    except:
                        data[keydata] = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                        oldList = data[keydata]

                    if "T03" in mc:
                        oldList[0] = lotid
                        oldList[1] = barcode
                        oldList[2] = z_tray
                        oldList[3] = z_pocket
                        oldList[4] = subMGZ
                        oldList[5] = subTray
                        oldList[6] = subPocket
                        data[keydata] = oldList

                    elif "T06" in mc:
                        # subMaterial = "FX9393-09-3#ABU90311K#FG8009#20#TCAD30103ELKY+101C4+M#4#0-00ATTT-INSP1-OK"
                        sindex = int(subMaterial.find("TCAD"))
                        eindex = sindex + 21
                        oldList[7] = subMaterial[sindex:eindex]
                        oldList[8] = subMGZ
                        oldList[9] = subTray
                        oldList[10] = subPocket
                        data[keydata] = oldList
                    elif "T07" in mc:
                        oldList[11] = subMGZ
                        oldList[12] = subTray
                        oldList[13] = subPocket
                        data[keydata] = oldList
            except:
                pass

        result = ""
        for da in data:
            getdictlist = data[da]
            for getdictitem in getdictlist:
                result += getdictitem + ","
            result += "end\n"

        # print(result)
        return result


