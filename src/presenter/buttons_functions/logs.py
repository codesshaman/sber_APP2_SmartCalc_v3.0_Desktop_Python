import os
import time
import datetime


class CalcLogs():

    def __init__(self,
                 file_path='logs/logs.py'):
        self.file_path = file_path

    def clean_old_logs(self, h):
        if h < 1:
            h = 1
        else:
            h = 1 * 1000000
        nowtime = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        rotation_time = datetime.datetime.now()
        for root, dirs, files in os.walk("logs"):
            for filename in files:
                if filename < nowtime:
                    now_h = int(time.time_ns() - (3600000 * h))
                    now_ms = (now_h / 1000000000)
                    print(datetime.datetime.utcfromtimestamp(now_ms).strftime('%Y-%m-%d-%H-%M-%S'))
                    # print(now_ms)
                    # print(filename)

    def check(self):
        exist = os.path.exists(self.file_path)
        return exist

    def del_history(self):
        file = open(self.file_path, "w")
        file.close()

    def create_if_not_exist(self):
        if not self.check():
            file = open(self.file_path, "w")
            file.write("0" + '\n')
            file.close()

    def read_file(self):
        self.create_if_not_exist()
        with open(self.file_path) as file:
            cmdlist = [row.strip() for row in file]
        return cmdlist[::-1]

    def write_file(self, value):
        self.create_if_not_exist()
        file = open(self.file_path, "a")
        file.write(str(value) + '\n')
        file.close()

func = CalcLogs()
func.clean_old_logs(0)
