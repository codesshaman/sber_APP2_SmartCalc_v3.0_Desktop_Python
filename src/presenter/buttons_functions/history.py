import os.path

class CalcHistory():

    def __init__(self, file_path='presenter/buttons_functions/.temp/history.txt'):
        self.file_path = file_path

    def check(self):
        exist = os.path.exists(self.file_path)
        return  exist

    def create_if_not_exist(self):
        if not self.check():
            file = open(self.file_path, "w")
            file.close()

    def read_file(self):
        self.create_if_not_exist()
        with open(self.file_path) as file:
            cmdlist = [row.strip() for row in file]
        return cmdlist[::-1]

    def write_file(self, operation):
        self.create_if_not_exist()
        file = open(self.file_path, "a")
        file.write(str(operation) + '\n')
        file.close()

result = CalcHistory()
print(result.read_file())