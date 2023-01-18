import os
import pytz
import datetime
tz_moscow = pytz.timezone('Europe/Moscow')

class CalcLogs():

    def __init__(self,
                 file_path='logs'):
        self.file_path = file_path
        self.current_logfile = self.check()

    def clean_old_logs(self, hours):
        self.create_new_logfile()
        h = datetime.datetime.now(tz_moscow).strftime('%H')
        h = str(int(h) - hours)
        m = str(datetime.datetime.now(tz_moscow).strftime('%M'))
        s = str(datetime.datetime.now(tz_moscow).strftime('%S'))
        current_date = datetime.datetime.now(tz_moscow).strftime("%d-%m-%Y")
        rotation = datetime.datetime.strptime(current_date + ' ' + h + ':' + m + ':' + s, '%d-%m-%Y %H:%M:%S')
        rotation = tz_moscow.localize(rotation)
        rotation = rotation.strftime('%d-%m-%Y %H:%M:%S')
        rotation = str(rotation).replace(' ', '-').replace(':', '-')
        rotation = 'logs_' + rotation
        for root, dirs, files in os.walk("logs"):
            for filename in files:
                if filename < rotation:
                    os.remove('logs/' + filename)
        lastlog = self.check()
        if lastlog != rotation:
            self.write_current_logfile(rotation)

    def check(self):
        filepath = str(self.file_path + '/system_logfile.txt')
        file = open(filepath, 'r')
        lastlog = file.read()
        lastlog = lastlog[0:24]
        return lastlog

    def create_filetime(self):
        h = datetime.datetime.now(tz_moscow).strftime('%H')
        m = str(datetime.datetime.now(tz_moscow).strftime('%M'))
        s = str(datetime.datetime.now(tz_moscow).strftime('%S'))
        current_date = datetime.datetime.now(tz_moscow).strftime("%d-%m-%Y")
        rotation = datetime.datetime.strptime(current_date + ' ' + h + ':' + m + ':' + s, '%d-%m-%Y %H:%M:%S')
        rotation = tz_moscow.localize(rotation)
        rotation = rotation.strftime('%d-%m-%Y %H:%M:%S')
        rotation = str(rotation).replace(' ', '-').replace(':', '-')
        return rotation

    def create_new_logfile(self):
        filepath = str(self.file_path) + '/logs_' + str(self.create_filetime())
        file = open(filepath, "a")
        file.write("")
        file.close()
        self.current_logfile = filepath
        return filepath

    def write_current_logfile(self, value):
        file = open(self.file_path + '/system_logfile.txt', "w")
        file.write(str(value) + '\n')
        file.close()

    def write_file(self, value):
        filepath = str(self.file_path + '/' + self.current_logfile)
        print(filepath)
        file = open(filepath, 'a')
        file.write(str(value) + "\n")
        file.close()