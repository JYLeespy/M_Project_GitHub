import os
import datetime

class Exploer:
    def __init__(self, basicpath):
        self.folderpathlist = {}
        self.filepathlist = {}
        # for maindir in os.listdir(basicpath):
        #     mainpath = os.path.join(basicpath, maindir)
        #     if os.path.isdir(mainpath):


        # for (root, directories, files) in os.walk(basicpath):
        #     print(root, directories, files)

        # import glob
        # import os
        # all_folder = glob.glob('*')  ## 또는 glob.glob('**')
        # all_file = [x for x in all_folder if os.path.isfile(x)]
        # for file_name in all_file:
        #     print(file_name)

        import glob
        extension = 'png'
        target_str = '에러'
        for f in glob.glob(f'{basicpath}/*{target_str}*.{extension}'):
            print(f)


    def get_infos(self, folderpath):
        for maindir in os.listdir(folderpath):
            check_path = os.path.join(folderpath, maindir)
            size = os.path.getsize(check_path)
            date_make = datetime.datetime.fromtimestamp(os.path.getctime(check_path))
            date_edit = datetime.datetime.fromtimestamp(os.path.getmtime(check_path))
            date_access = datetime.datetime.fromtimestamp(os.path.getatime(check_path))
            if os.path.isfile(check_path):
                extension = maindir.split(".")[-1]
                pathtype = 'file'
                self.filepathlist[check_path] = {'name': maindir, 'pathtype': pathtype, 'extension': extension, 'size': size,
                                             'date_make': date_make, 'date_edit': date_edit, 'date_access': date_access}
                print(self.filepathlist[check_path])

    def icons(self, extension):
        print(extension)
        return

# path = 'P:/0.임시/0 생산기술팀 공용폴더/0 생산기술팀 공용폴더\(공정) 2. OIS'
path = 'P:/0.임시/0 생산기술팀 공용폴더/0 생산기술팀 공용폴더\(공정) 2. OIS\(2) FACA\VARO23\A2.0 LBU 70K BOM Ball 자재 보고 누락'

e = Exploer(path)