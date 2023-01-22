import os.path


class CalcConfig():

    def __init__(self):
        self.rotation = self.get_rotation()
        self.bg = self.get_background()
        self.fc = self.get_fontcolor()
        self.file_path = "presenter/calcconfig.cfg"

    def create_if_not_exist(self):
        if not self.check("presenter/calcconfig.cfg"):
            file = open("presenter/calcconfig.cfg", "w")
            file.write("graph_window=0      # Открывать график в отдельном окне")
            file.write('fonts_color=black   # Цвет шрифта\n')
            file.write('logs_rotation=0     # Период ротации логов в часах\n')
            file.write('bg_color=gray       # Цвет фона\n')
            file.close()

    def check(self, path):
        exist = os.path.exists(path)
        return exist

    def read_config(self):
        self.create_if_not_exist()
        with open("presenter/calcconfig.cfg") as file:
            cmdlist = [row.strip() for row in file]
        return cmdlist[::-1]

    def get_rotation(self):
        conf_array = self.read_config()
        for line in conf_array:
            if line[0:13] == 'logs_rotation':
                line_array = line.split('=')
                value = line_array[1].split('#')
                value = value[0].strip()
        if len(value) > 0:
            return value

    def get_background(self):
        conf_array = self.read_config()
        for line in conf_array:
            if line[0:8] == 'bg_color':
                line_array = line.split('=')
                value = line_array[1].split('#')
                value = value[0].strip()
        if len(value) > 0:
            return value

    def get_fontcolor(self):
        conf_array = self.read_config()
        for line in conf_array:
            if line[0:11] == 'fonts_color':
                line_array = line.split('=')
                value = line_array[1].split('#')
                value = value[0].strip()
        if len(value) > 0:
            return value

    def get_graph_window(self):
        conf_array = self.read_config()
        for line in conf_array:
            if line[0:12] == 'graph_window':
                line_array = line.split('=')
                value = line_array[1].split('#')
                value = value[0].strip()
        if len(value) > 0:
            return value