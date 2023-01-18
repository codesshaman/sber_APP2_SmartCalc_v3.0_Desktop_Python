import os
import pytz
import time
import datetime
tz_moscow = pytz.timezone('Europe/Moscow')


class CalcLogs():

    def __init__(self,
                 file_path='logs'):
        self.file_path = file_path
        self.current_logfile = self.check()

    def clean_old_logs(self, hours):
        hour = datetime.datetime.now(tz_moscow).strftime('%H')
        h = str(int(hour) - hours)
        curr_h = str(int(hour))
        m = str(datetime.datetime.now(tz_moscow).strftime('%M'))
        s = str(datetime.datetime.now(tz_moscow).strftime('%S'))
        current_date = datetime.datetime.now(tz_moscow).strftime("%d-%m-%Y")
        current_time = datetime.datetime.strptime(current_date + ' ' +
                                                  curr_h + ':' +
                                                  m + ':' +
                                                  s, '%d-%m-%Y %H:%M:%S')
        current_time = tz_moscow.localize(current_time)
        current_file = current_time.strftime('%d-%m-%Y %H:%M:%S')
        current_time = str(current_file).replace(' ', '-').replace(':', '-')
        current_file = 'logs_' + current_time
        rotation_time = datetime.datetime.strptime(current_date + ' ' +
                                                   h + ':' +
                                                   m + ':' +
                                                   s, '%d-%m-%Y %H:%M:%S')
        rotation_time = tz_moscow.localize(rotation_time)
        rotation_timestamp = time.mktime(rotation_time.timetuple())
        print(rotation_timestamp)
        rotation_time = rotation_time.strftime('%d-%m-%Y %H:%M:%S')
        rotation = str(rotation_time).replace(' ', '-').replace(':', '-')
        rotation = 'logs_' + rotation
        last_timestamp = self.lastlog_to_timestamp()
        diff = int(last_timestamp) - int(rotation_timestamp)
        if diff <= 0:
            self.write_current_logfile(current_file)
            self.create_new_logfile(current_time)
            self.current_logfile = self.check()

    def check(self):
        self.create_if_not_exist()
        filepath = str(self.file_path + '/system_logfile.txt')
        file = open(filepath, 'r')
        lastlog = file.read()[0:24]
        return lastlog

    def lastlog_to_timestamp(self):
        lastlog = self.check()
        lastlog = lastlog[5:24]
        date = datetime.datetime.strptime(lastlog, '%d-%m-%Y-%H-%M-%S')
        date_string = tz_moscow.localize(date)
        restored_timestamp = time.mktime(date_string.timetuple())
        return restored_timestamp

    def create_if_not_exist(self):
        exist = os.path.exists(self.file_path + '/system_logfile.txt')
        if not exist:
            file = open(self.file_path + '/system_logfile.txt', "w")
            file.write("logs_12-12-2012-12-12-12" + '\n')
            file.close()

    def create_new_logfile(self, current_time):
        filepath = str(self.file_path) + '/logs_' + str(current_time)
        file = open(filepath, "a")
        file.write("")
        file.close()
        self.current_logfile = filepath
        return filepath

    def write_current_logfile(self, value):
        file = open(self.file_path + '/system_logfile.txt', "w")
        file.write(str(value) + '\n')
        file.close()
        self.current_logfile = self.check()

    def write_file(self, value):
        filepath = str(self.file_path + '/' + self.current_logfile)
        print(filepath)
        file = open(filepath, 'a')
        file.write(str(value) + "\n")
        file.close()
