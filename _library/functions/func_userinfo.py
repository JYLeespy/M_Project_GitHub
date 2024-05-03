class USER:
    def ip(self) -> tuple:
        import socket
        return socket.gethostbyname_ex(socket.getfqdn())# - (3)
    def mac(self) -> list:
        import re
        from uuid import getnode
        mac = ""
        for i in re.findall('..', '%012x' % getnode()):
            mac += i
        return mac
    def user_name(self) -> str:
        import getpass
        return getpass.getuser()
    def user_name2(self):
        import os
        return os.getlogin()
    def user_pcSerialNo(self):
        # get user-info:
        import subprocess
        pc_serial = subprocess.check_output('wmic bios get serialnumber')

        return_pc_serial = ""
        for i in range(len(pc_serial)):
            text = pc_serial[i]

            if text == 32 or text == 13 or text == 10:
                pass
            else:
                return_pc_serial += chr(text)

        return_pc_serial = return_pc_serial[12:]
        # pc_serial = pc_serial.decode('utf-8').rstrip()
        # pc_serial = pc_serial.replace('SerialNumber','')
        # pc_serial = pc_serial.strip()
        # self.pc_serial = pc_serial.replace('\n','')
        # a = a.decode('utf-8').replace('\r\r\n', '\r\n')
        return return_pc_serial
# user = USER()
# a, b, c = user.info_ip()
# print(a)
# user.mac()
# user.user_name()
# import os
# print(os.getlogin())

