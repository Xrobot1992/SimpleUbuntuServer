import os
import ServerInfo
ru = lambda text: text.decode('utf-8', 'ignore')
ur = lambda text: text.encode('utf-8', 'ignore')
name = '%s.conf' % ServerInfo.Info('name').get_info().replace(' ', '')
path = '/'
conf = '%s%s%s' % (os.getcwd(), path, name)

class Sets:

    def __init__(self):
        self.LHOST = '127.0.0.1'
        self.LPORT = 8080
        self.FQUERY = ''
        self.MQUERY = ''
        self.BQUERY = ''
        self.RQUERY = ''
        self.CQUERY = ''
        self.IQUERY = ''
        self.ADBLOCKER = 0
        self.IMETHOD = 1
        self.ILINE = 0
        self.ISPLIT = 5
        self.RPORT = 0
        self.RPATH = 0
        self.ADMODE = 0
        self.CUSHDR0 = ''
        self.VALHDR0 = ''
        self.CUSHDR1 = ''
        self.VALHDR1 = ''
        self.CUSHDR2 = ''
        self.VALHDR2 = ''
        self.CUSHDR3 = ''
        self.VALHDR3 = ''
        self.KEEP = ''
        self.RHTTP = 0
        self.RHTTPS = 1
        self.SBUFF = 2048
        self.TIMEOUT = 60
        self.PHOST = ''
        self.PPORT = 0
        self.PTYPE = 0
        self.LOGS = 1
        self.load()

    def load(self):
        try:
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)

        except:
            self.save()
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)

    def save(self):
        data = ''
        for name in self.__dict__.keys():
            line = name + ' = ' + repr(self.__dict__[name]) + '\r\n'
            data += line

        open(conf, 'wb').write(ur(data))
        del data
