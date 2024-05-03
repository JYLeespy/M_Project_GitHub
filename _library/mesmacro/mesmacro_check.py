import psutil
class Process:
    def __init__(self):
        self.GMES = 'LGIT.GMES.SFU.MainFrame.exe'
        self.LAS = 'Jahwa LAS.exe'
        self.OUTLOOK = 'OUTLOOK.EXE'
    def check_program_on(self):
        check_GMES = False
        check_LAS = False
        check_OUTLOOK = False
        for p in psutil.process_iter():
            print(p.name())
            if p.name() == self.OUTLOOK:
                check_OUTLOOK = True
            if p.name() == self.GMES:
                check_GMES = True
            if p.name() == self.LAS:
                check_LAS = True
        return check_OUTLOOK, check_GMES, check_LAS

    def check_on_screen(self, imgpath, program):
        imgfile = f'{imgpath}p_{program}.png'

