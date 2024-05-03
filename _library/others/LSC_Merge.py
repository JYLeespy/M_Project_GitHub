import os
import datetime

with open('LSC_Settings.txt', 'r', encoding='utf-8') as r:
    options = r.readlines()

def str_strip(text):
    text = text.lstrip()
    return text.rstrip()

fromdate = str_strip(options[0])[6:]
todate =  str_strip(options[1])[6:]
path =   options[2].replace("\n","")[6:]
save_path = options[3][7:]
# print(fromdate, todate, path, savepath)

# fromdate = '2024-02-21'
# todate = '2024-02-22'

def date_convert(dt):
    dateinfo = dt[0:10]
    y = int(dateinfo.split("-")[0])
    mm = int(dateinfo.split("-")[1])
    d= int(dateinfo.split("-")[2])

    timeinfo = dt[11:]
    h = int(timeinfo.split(":")[0])
    m = int(timeinfo.split(":")[1])
    s = int(timeinfo.split(":")[2])

    return datetime.datetime(y,mm,d,h,m,s)

fromdate_split = fromdate.split('-')
fromdate_y = int(fromdate_split[0])
fromdate_m = int(fromdate_split[1])
fromdate_d = int(fromdate_split[2])
dt_fromdate = datetime.datetime(fromdate_y,fromdate_m,fromdate_d,hour=8,minute=20,second=0)

todate_split = todate.split('-')
todate_y = int(todate_split[0])
todate_m = int(todate_split[1])
todate_d = int(todate_split[2])
dt_todate = datetime.datetime(todate_y,todate_m,todate_d,hour=8,minute=20,second=0)


# path='V:/구미생산운영팀(현장포함)\기술1팀/2. LSC/0. 양산 로그/2024_2월/0221~0222'
# save_path = 'D:/새 폴더 (2)'


init_row = "MagaZineSN_Pick,MagaZineSN_Put,CoilSN,Spindle,CWLA,LSC,ProductType,ProductIndex,Versions,CarrierSN,CaveScanResult,Result,FailInFo,Time_In,Time_Out,CT,HG_OuterLeadPosition,HG_InnerLeadPosition,InnerLeadPosition,OuterLeadPosition,Inner Lead cutting length,Outer Lead cutting length,MCO position Lnner_X,MCO position Lnner_Y,MCO position Outer_X,MCO position Outer_Y,F1,Distance,CuttingLead Speed,CuttingLead Frequency(KHZ),CuttingLead Pulse Width,CuttingLead Turn on delay,CuttingLead Power,CuttingLnner Speed,CuttingLnner Frequency(KHZ),CuttingLnner Pulse Width,CuttingLnner Turn on delay,CuttingLnner Power,Image_RecheckLocationImagePath,Lead Power,Linner Power,Measure Time\n"
# path 내 folder list 가져와서 folder_list 변수에 저장
folder_list = os.listdir(path)

with open(save_path + f'/AF_{todate}.csv', 'w') as w:
    w.write(init_row)
with open(save_path + f'/OIS_{todate}.csv', 'w') as w:
    w.write(init_row)

for mc in folder_list:
    mc_type = "" # mc_type 초기화
    if mc == '2-1' or mc == '3-1' or mc == '4-1':
        mc_type = 'AF'
    elif mc == '2-2' or mc == '2-3' or mc == '3-2' or mc == '3-3' or mc == '4-2' or mc == '4-3':
        mc_type = 'OIS'
    else:
        continue
    in_mc_folder_path = os.path.join(path,mc)
    in_mc_folder = os.listdir(in_mc_folder_path)
    for logfile in in_mc_folder:
        if 'Laser' in logfile and logfile[-4:] == '.csv':
            print(f'\rLSC#{mc} >> filename : {logfile} reading...', end="")
            filepath = os.path.join(in_mc_folder_path,logfile)
            with open(filepath, 'r') as r:
                readfile = r.readlines()
            temp_list = []
            for line in readfile:
                col_list = line.split(',')
                temp_text = ""
                count = 0
                start_time = ""
                end_time = ""
                count2 = 0
                for cols in col_list:

                    remove_double_quotation_marks = cols.replace('"','')
                    if remove_double_quotation_marks == init_row[0]:
                        break
                    else:
                        temp_text += remove_double_quotation_marks + ","
                    if count == 2:
                        temp_text += f"{remove_double_quotation_marks[-3:]},{remove_double_quotation_marks[-3:-1]},'{mc},"
                    count += 1
                temp_text = temp_text[0:-1]
                temp_text += "\n"
                try:
                    start_time = temp_text.split(",")[10+3]
                    end_time = temp_text.split(",")[11+3]
                    dt_st = date_convert(start_time)
                    dt_et = date_convert(end_time)
                    # print(f'{dt_et} {dt_fromdate} {dt_todate}' )
                    if dt_fromdate <= dt_et and dt_todate > dt_et:
                        temp_text = temp_text[0:-1]
                        temp_list.append(temp_text)
                        count += 1
                except:
                    pass
            print(f'\rLSC#{mc} >> filename : {logfile} saving', end="")
            with open(save_path + f'/{mc_type}_{todate}.csv', 'a') as w:
                w.writelines(temp_list)
        os.startfile(save_path)