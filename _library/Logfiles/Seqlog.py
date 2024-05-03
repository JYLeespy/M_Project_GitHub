import os


class SEQLOG:
    def __init__(self):
        self.path = 'H:/archiving folder/이진영 (임시폴더)/SEQ TEST.log'
        self.savepath = 'H:/archiving folder/이진영 (임시폴더)/SEQ TEST save.csv'
        with open(self.path, 'r') as r:
            readline = r.readlines()

        save_list =[]
        for line in readline:
            print(self.split_line(line))
            save_list.append(self.split_line(line))

        save_list.insert(0, "'1','2','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','\n'")
        with open(self.savepath, 'w') as w:
            w.writelines(save_list)

    def str_strip(self, text) -> str:
        text = text.rstrip()
        return text.lstrip()

    def row_convert(self, key):
        rows ={'LotID':3,
                'TrayID':4,
                'PocketID':5,
                'ModuleID':6,
                'PosX':7,
                'PosY':8,
                'PosZ':9,
                '_subCycleStep':10,
                'X':11,
                'Y':12
        }
        return rows[key]

    def split_line(self, line):
        log_date = line.split(' ')[0]
        log_info = line.split(' ')[1]
        log_time = line.split(' ')[2]

        log_cycle = line[line.find('['):line.find(']')+1]
        log_cycle = log_cycle.replace('[','')
        log_cycle = log_cycle.replace(']','')
        log_cycle = log_cycle.replace(' : ','/')

        log_data = self.str_strip(line[line.find(']')+1:])
        log_data_list = log_data.split(',')

        temp_list = []
        for i in range(30):
            temp_list.append("")

        for d in log_data_list:
            try:
                print(d)
                key = d.split("=")[0]
                value = d.split("=")[1]
                index = self.row_convert(key)
                temp_list[index] = value

            except:
                print(f'Text Split Error : split("=") {d}')


        temp_line = ''
        for t in temp_list:
            temp_line += f'{t},'
        temp_line = temp_line[:-1]
        return f'{log_info},{log_date} {log_time},{log_cycle},{temp_line}'

s = SEQLOG()

#
# class SEQLOG:
#     def __init__(self, folderpath="", filename=""):
#         if folderpath == "" or filename == "":
#             self.folderpath = 'D:/LogDownloader/20240329_MC1_(8)ZSATT_GP430450E3V0VHA/Sequence'
#             self.filename = 'SeqLog.log-2024-03-30-04.log'
#         else:
#             self.folderpath = folderpath
#             self.filename = filename
#         self.logtype()
#
#
#         # filelist = os.listdir(self.folderpath)
#         #
#         # for file in filelist:
#         #     self.filepath = os.path.join(self.folderpath,file)
#         #     self.readline()
#
#         basicpath = 'D:/LogDownloader'
#         basicfolders = os.listdir(basicpath)
#         self.p_dict = {}
#         for i in basicfolders:
#             processname = i.split(")")[1]
#             self.cycle_list = []
#             filepath_join = os.path.join(basicpath,f'{i}/Sequence')
#             filelist = os.listdir(filepath_join)
#             for file in filelist:
#                 self.filepath = os.path.join(filepath_join,file)
#                 self.readline()
#                 savepath = "D:/"
#
#                 if processname.find("Handler_") != -1:
#                     self.p_dict = self.cycle_Handler
#                 if processname.find("Ball") != -1:
#                     self.p_dict = self.cycle_Ball
#                 if processname.find("Grease") != -1:
#                     self.p_dict = self.cycle_Grease
#                 if processname.find("ATT") != -1:
#                     self.p_dict = self.cycle_ATT
#                 if processname.find("Epoxy") != -1:
#                     self.p_dict = self.cycle_Epoxy
#                 if processname.find("UVINSP") != -1:
#                     self.p_dict = self.cycle_UV
#
#                 savefilename = f'{processname}.csv'
#                 savefilepath = os.path.join(savepath,savefilename)
#                 cycle_list = set(self.cycle_list)
#                 with open(savefilepath, 'w') as w:
#                     w.writelines(cycle_list)
#         self.filepath = os.path.join(self.folderpath, self.filename)
#     def str_strip(self, text) -> str:
#         text = text.rstrip()
#         return text.lstrip()
#     def readline(self):
#         # print(self.filepath)
#         with open(self.filepath, 'r') as r:
#             readline = r.readlines()
#
#         # print(f'{self.filepath} {len(readline)}')
#         for line in readline:
#             # 기본정보 좌측 날짜 / 종류 / 시간 분류
#             log_date = line.split(" ")[0]
#             log_type = line.split(" ")[1]
#             log_time = line.split(" ")[2]
#             # 기본정보 제외한 우측 로그파일
#             startpoint = len(log_date)+len(log_type)+len(log_time)+3
#             logline = line[startpoint:]
#             if logline.find("subCycleStep") == -1:
#                 log_cycletype = 'print'
#             else:
#                 log_cycletype = 'active'
#
#             # log_index_lotid = self.find_index(logline, 'LOT ID')
#
#             for item in self.p_dict:
#                 if logline.find(item) == -1:
#                     print(logline[:logline.find(item)])
#                     newline = logline[:logline.find(item)]+"\n"
#                     self.cycle_list.append(newline)
#
#     def find_index(self, text, findtext):
#         return text.find(findtext)
#
#     def logtype(self):
#         self.cycle_Handler = {  "LeftRailIndex : FlyingAlignVisionCycle() : ":"",
#                                 "SetBoatLotEndFlag() : ":"",
#                                 "[MzBarcodeReadingCycle] Data: Mes.ResultParam.Receive":"",
#                                 "Barcode : BarcodeReadingCycle() :": "",
#                                 "[Occured Tray ID Setting Form] - ": "",
#                                 "Station = Barcoder": "",
#                                 "TopFlyingAlign Start ": "",
#                                 "[MzBarcodeReadingCycle]": "",
#                                 "AutoRun":"",
#                                 "TRAY ID FAIL - ":"",
#                                 "Show Lot End Message":"",
#                                 "XYSubMagazine : MzLoadingCycle() : ":"",
#                                 "MzLoader : MzBarcodeReadingCycle() : ":"",
#                                 "MES - CTQ 모드 시작":""}
#         self.cycle_Ball =  {"Attach(Right) : PlaceCycle() :[Place Start] :":"",
#                             "AttachVision : TopInspectionCycle() : TopInspectionCycle():":"",
#                             "Attach(Left) : TopAlignCycle() : [AttachTopAlignStart] ":"",
#                             "Attach(Left) : PlaceCycle() :[Place Start] :":"",
#                             "PickupVision(Left) : TopAlignCycle() : [Pickup Vision Start]":"",
#                             "PickupVision(Right) : TopAlignCycle() : [Pickup Vision Start] ":"",
#                             "Attach(Left) : PlaceCycle() :[Place&Shift Down Start] :":"",
#                             "Attach(Left) : PlaceCycle() :[Place&Shift Position Down End] :":"",
#                             "Attach(Right) : PlaceCycle() :[Place Completed] :":"",
#                             "Attach(Right) : TopAlignCycle() : [AttachTopAlignStart]":"",
#                             "Attach(Left) : PlaceCycle() :[Place Completed] :":"",
#                             "Attach(Right) : PlaceCycle() :[Place&Shift Down Start] :":"",
#                             "Attach(Right) : PlaceCycle() :[Place&Shift Position Down End] :":""}
#         self.cycle_Grease = {
#                             "Dispenser1: FlyingAlignVisionCycle(): DispFlyingAlignVisionCycle_Top():":"",
#                             "Dispenser2: FlyingAlignVisionCycle(): DispFlyingAlignVisionCycle_Top():":"",
#                             "Dispenser1: DispOneChipProbeAlignCycle():ProbeValue:":"",
#                             "Dispenser2: DispOneChipProbeAlignCycle(): ProbeValue:":"",
#                             "Dispenser1: DispOneChipDPInspectionCycle(): Inspection Start:":"",
#                             "Dispenser2: DispOneChipDPInspectionCycle(): Inspection Start:":""}
#         self.cycle_ATT = {
#             "Attach : PlaceCycle() :[Place&Shift Position Down End] :": "",
#             "PickupVision : TopAlignCycle() : [PickupVision Start] ": "",
#             "AttachVision : TopInspectionCycle() : AttachInspectionStart ": "",
#             "Attach : PlaceCycle() :[Place&Shift Down Start] :": "",
#             "Attach : PlaceCycle() :[Attach Completed] :": "",
#             "Attach : PlaceCycle() :[Place Start] :": "",
#             "Attach :PlaceCycle() :Place Position - ": "",
#             "AttachVision : TopAlignCycle() : AttachTopAlignStart ": "",
#             "PickupVision : BufferAlignCycle() : PickupAlignStart ": "",
#             "PickupVision(Right) : TopAlignCycle() : ": "",
#             "PickupVision(Right) : BufferAlignCycle() : BufferPickupAlign ": "",
#             "PickupVision(Left) : BufferAlignCycle() : BufferPickupAlign ": "",
#             "PlaceCycle() : LoadCell Start : ": "",
#             "PickupVision(Left) : TopAlignCycle() : ": "",
#             "Attach(Right) : TopAlignCycle() : [Attach TopAlign Start] ": "",
#             "Attach(Left) : TopAlignCycle() : [Attach TopAlign Start] ": "",
#             "Attach(Right) : TopInspectionCycle() : [Inspection Start] ": "",
#             "Attach(Right) : PlaceCycle() :Place Position - ": "",
#             "Attach(Left) : TopInspectionCycle() : [Inspection Start] ": "",
#             "Attach(Left) : PlaceCycle() :Place Position - ": ""}
#         self.cycle_Epoxy = {
#             "Dispenser1 : FlyingAlignVisionCycle() : DispFlyingAlignVisionCycle_Top(): ": "",
#             "Dispenser2 : FlyingAlignVisionCycle() : DispFlyingAlignVisionCycle_Top(): ": "",
#             "Dispenser1 : DispOneChipDPInspectionCycle() : ": "",
#             "Dispenser2 : DispOneChipDPInspectionCycle() : ": "",
#             "Dispenser1 : DispOneChipProbeAlignCycle() :": "",
#             "Dispenser2 : DispOneChipProbeAlignCycle() :": "",
#             "OneChipProbeAlignCycle() :Probe Value :": "",
#             "RejectVisionCycle(): ": "",
#             "InspectionCycle() : [Inspection Start] ": "",
#             "OneChipProbeMultiAlignCycle() :[Probe Value Error] : ": "",
#             "UvCycle() : [UVStart] ": "",
#             "UvCycle() : [UVEnd] ": ""}
#         self.cycle_UV = {
#             "UvCycle() : ": "",
#             "InspectionCycle() : ": "",
#             "OneChipProbeAlignCycle() :": "",
#             "OneChipProbeMultiAlignCycle() :[Probe Value Error] : ": "",
#             "[TRAY PROCESSING COMPLETED] - ": "",
#             "[TRAY APD] - ": "",
#             "RejectVisionCycle(): ": "",
#             "AutoRunStop - ErrorName = ": "",
#             "OneChipMultiProbeCycle() : ": "",
#             "AutoRun Start": ""}
# # s = SEQLOG()
#
#
#
#
# basicpath = "D:/LogDownloader"
# b_paths = os.listdir(basicpath)
# filecount = 0
#
# for b in b_paths:
#     path = os.path.join(basicpath,b)
#     files = os.listdir(f'{path}/Sequence')
#
#     s = b[b.find(")") + 1:]
#     if s.find('Handler') != -1:
#         temp_dict = {  "LeftRailIndex : FlyingAlignVisionCycle() : ":"",
#                                 "SetBoatLotEndFlag() : ":"",
#                                 "[MzBarcodeReadingCycle] Data: Mes.ResultParam.Receive":"",
#                                 "Barcode : BarcodeReadingCycle() :": "",
#                                 "[Occured Tray ID Setting Form] - ": "",
#                                 "Station = Barcoder": "",
#                                 "TopFlyingAlign Start ": "",
#                                 "[MzBarcodeReadingCycle]": "",
#                                 "AutoRun":"",
#                                 "TRAY ID FAIL - ":"",
#                                 "Show Lot End Message":"",
#                                 "XYSubMagazine : MzLoadingCycle() : ":"",
#                                 "MzLoader : MzBarcodeReadingCycle() : ":"",
#                                 "MES - CTQ 모드 시작":""}
#     elif s.find('Ball') != -1:
#         temp_dict =  {"Attach(Right) : PlaceCycle() :[Place Start] :":"",
#                             "AttachVision : TopInspectionCycle() : TopInspectionCycle():":"",
#                             "Attach(Left) : TopAlignCycle() : [AttachTopAlignStart] ":"",
#                             "Attach(Left) : PlaceCycle() :[Place Start] :":"",
#                             "PickupVision(Left) : TopAlignCycle() : [Pickup Vision Start]":"",
#                             "PickupVision(Right) : TopAlignCycle() : [Pickup Vision Start] ":"",
#                             "Attach(Left) : PlaceCycle() :[Place&Shift Down Start] :":"",
#                             "Attach(Left) : PlaceCycle() :[Place&Shift Position Down End] :":"",
#                             "Attach(Right) : PlaceCycle() :[Place Completed] :":"",
#                             "Attach(Right) : TopAlignCycle() : [AttachTopAlignStart]":"",
#                             "Attach(Left) : PlaceCycle() :[Place Completed] :":"",
#                             "Attach(Right) : PlaceCycle() :[Place&Shift Down Start] :":"",
#                             "Attach(Right) : PlaceCycle() :[Place&Shift Position Down End] :":""}
#     elif s.find('Grease') != -1:
#         temp_dict = {
#                     "Dispenser1: FlyingAlignVisionCycle(): DispFlyingAlignVisionCycle_Top():":"",
#                     "Dispenser2: FlyingAlignVisionCycle(): DispFlyingAlignVisionCycle_Top():":"",
#                     "Dispenser1: DispOneChipProbeAlignCycle():ProbeValue:":"",
#                     "Dispenser2: DispOneChipProbeAlignCycle(): ProbeValue:":"",
#                     "Dispenser1: DispOneChipDPInspectionCycle(): Inspection Start:":"",
#                     "Dispenser2: DispOneChipDPInspectionCycle(): Inspection Start:":"",
#                     "Dispenser1 : DispProfileSubCycle() :": "",
#                     "Dispenser1 : DispOneChipDPInspectionCycle() : ": "",
#                     "Dispenser2 : DispProfileSubCycle() :": "",
#                     "Dispenser2 : DispOneChipDPInspectionCycle() : ": "",
#                     "Dispenser1 : BalanceProbeCycle() :": "",
#                     "Dispenser2 : BalanceProbeCycle() :": "",
#                     "Dispenser1-DispOneChipDPInspectionCycle():": "",
#                     "Dispenser2-DispOneChipDPInspectionCycle():": "",
#                     "Rail : ": "",
#                     "Dispenser1 TopFlyingAlign Start ": "",
#                     "Dispenser2 TopFlyingAlign Start ": ""}
#     elif s.find('ATT') != -1:
#         temp_dict = {
#             "Attach : PlaceCycle() :[Place&Shift Position Down End] :": "",
#             "PickupVision : TopAlignCycle() : [PickupVision Start] ": "",
#             "AttachVision : TopInspectionCycle() : AttachInspectionStart ": "",
#             "Attach : PlaceCycle() :[Place&Shift Down Start] :": "",
#             "Attach : PlaceCycle() :[Attach Completed] :": "",
#             "Attach : PlaceCycle() :[Place Start] :": "",
#             "Attach :PlaceCycle() :Place Position - ": "",
#             "AttachVision : TopAlignCycle() : AttachTopAlignStart ": "",
#             "PickupVision : BufferAlignCycle() : PickupAlignStart ": "",
#             "PickupVision(Right) : TopAlignCycle() : ": "",
#             "PickupVision(Right) : BufferAlignCycle() : BufferPickupAlign ": "",
#             "PickupVision(Left) : BufferAlignCycle() : BufferPickupAlign ": "",
#             "PlaceCycle() : LoadCell Start : ": "",
#             "PickupVision(Left) : TopAlignCycle() : ": "",
#             "Attach(Right) : TopAlignCycle() : [Attach TopAlign Start] ": "",
#             "Attach(Left) : TopAlignCycle() : [Attach TopAlign Start] ": "",
#             "Attach(Right) : TopInspectionCycle() : [Inspection Start] ": "",
#             "Attach(Right) : PlaceCycle() :Place Position - ": "",
#             "Attach(Left) : TopInspectionCycle() : [Inspection Start] ": "",
#             "Attach(Left) : PlaceCycle() :Place Position - ": ""}
#     elif s.find('Epoxy') != -1:
#         temp_dict = {
#             "Dispenser1 : FlyingAlignVisionCycle() : DispFlyingAlignVisionCycle_Top(): ": "",
#             "Dispenser2 : FlyingAlignVisionCycle() : DispFlyingAlignVisionCycle_Top(): ": "",
#             "Dispenser1 : DispOneChipDPInspectionCycle() : ": "",
#             "Dispenser2 : DispOneChipDPInspectionCycle() : ": "",
#             "Dispenser1 : DispOneChipProbeAlignCycle() :": "",
#             "Dispenser2 : DispOneChipProbeAlignCycle() :": "",
#             "OneChipProbeAlignCycle() :Probe Value :": "",
#             "RejectVisionCycle(): ": "",
#             "InspectionCycle() : [Inspection Start] ": "",
#             "OneChipProbeMultiAlignCycle() :[Probe Value Error] : ": "",
#             "UvCycle() : [UVStart] ": "",
#             "UvCycle() : [UVEnd] ": "",
#             "Dispenser1-DispOneChipDPInspectionCycle():": "",
#             "Dispenser2-DispOneChipDPInspectionCycle():": "",
#             "Dispenser1 : BalanceProbeCycle() :": "",
#             "Dispenser2 : BalanceProbeCycle() :": "",
#             "Dispenser1 TopFlyingAlign Start ": "",
#             "Dispenser2 TopFlyingAlign Start ": "",
#             "Dispenser1 : DispProfileSubCycle() :": "",
#             "Dispenser2 : DispProfileSubCycle() :": "",
#             "Rail : ": "",
#             "Prebuffer : TrayIDReportCycle() :": "",
#             "AutoRun Start": "",
#             "AutoRunStop": ""}
#     elif s.find('UV') != -1:
#         temp_dict = {
#             "UvCycle() : ": "",
#             "InspectionCycle() : ": "",
#             "OneChipProbeAlignCycle() :": "",
#             "OneChipProbeMultiAlignCycle() :[Probe Value Error] : ": "",
#             "[TRAY PROCESSING COMPLETED] - ": "",
#             "[TRAY APD] - ": "",
#             "RejectVisionCycle(): ": "",
#             "AutoRunStop - ErrorName = ": "",
#             "OneChipMultiProbeCycle() : ": "",
#             "AutoRun Start": ""}
#
#     savefilepath = os.path.join("D:/merge",f'{b[b.find(")") + 1:]}.csv')
#     with open(savefilepath, 'w') as w:
#         w.writelines("")
#
#     for file in files:
#         total = len(files)*len(b_paths)
#         print(f'\r[{round((filecount/total)*100,2)}%] {b} / {file}  >> {filecount}/{total}   <1>', end="")
#
#         # filepath = os.path.join(path,f'/Sequence/{file}')
#         filepath = f'{basicpath}/{b}/Sequence/{file}'
#         # print(f'basicpath : {basicpath} b : {b},  b_paths:{b_paths} filepath : {filepath}')
#         with open(filepath, 'r') as r:
#             readline = r.readlines()
#         temp_line =""
#         temp_count = 0
#         for line in readline:
#             a = len(temp_dict)
#             try:
#                 log_date = line.split(" ")[0]
#                 log_type = line.split(" ")[1]
#                 log_time = line.split(" ")[2]
#                 # 기본정보 제외한 우측 로그파일
#                 startpoint = len(log_date) + len(log_type) + len(log_time) + 3
#                 logline = line[startpoint:]
#                 write = True
#                 for i in temp_dict:
#                     if line.find(i) == -1:
#                         write = True
#                         pass
#                     else:
#                         write = False
#                         break
#                 if write:
#                     temp_line += logline
#                     # print(f'[{s}] {write} : {line}')
#             except:
#                 temp_line += line
#             print(f'\r[{round((filecount / total) * 100, 2)}%] {b} / {file}  >> {filecount}/{total}   {temp_count}/{len(readline)} ', end="")
#             temp_count += 1
#         with open(savefilepath, 'a') as w:
#             w.writelines(temp_line)
#         filecount += 1
# # savefilepath2 = os.path.join(path,"Ball1_.csv")
# #
# # with open(savefilepath,'r') as r:
# #     readline = r.readlines()
# #     print(len(readline))
# # for line in readline:
# #     for cycle in temp_dict:
# #         try:
# #             a = line.find(cycle)
# #             break
# #         except:
# #             print(f'False : {line}')