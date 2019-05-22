import os


class FileManupulation:

    def __init__(self):
        pass

    def __init__(self, filename):
        self.filename = filename
        f = self.filename
       # i=0
       # while(i<len(f)):
        #    if(f[i]=='\\'):
        #       f[i]='/'

   # def __del__(self):
    #    self.file.close()

    def set_filename(self, filename):
        self.filename = filename
        f = self.filename
        i = 0
        while(i < len(f)):
            if(f[i] == '\\'):
                f[i] = '/'

    def get_filename(self):
        return self.filename

    def replace_all(self, value, newvalue):
        with open(self.filename) as file:
            content = file.read()
            content = content.replace(value, newvalue)
            del file
            file = open(self.filename, "w")
            file.write(content)

    def show_file(self):
        with open(self.filename)as file:
            return file.read()

    def append_file(self, filename):
        file1 = open(filename)
        str = file1.read() + "\n"
        file1 = open(self.filename, "a")
        file1.write(str)
        file1.close()

    def delete_content(self):
        file = open(self.filename, "w")
        file.truncate(32)

    def append_content(self, data):
        file = open(self.filename, "a")
        data = "\n" + data
        file.write(data)

    def write_content(self, data):
        file = open(self.filename, "w")
        file.write(data)

    @staticmethod
    def delete_file(filename):
        os.remove(filename)

    @classmethod
    def create_file(cls, filename):
        return open(filename, "w")
