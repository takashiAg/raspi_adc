import os
import datetime


class file_write():
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))
        Dir_path = os.path.normpath(os.path.join(base, "data"))
        if not (os.path.isdir(Dir_path)):
            os.mkdir(Dir_path)

        now = datetime.datetime.now()
        filename = "{0:%Y-%m-%d_%H-%M-%S}".format(now)
        name = os.path.normpath(os.path.join(base, "data", filename, ".csv"))
        self.f = open(name, 'w')

    def write(self, time, value):
        self.f.write(str(time))
        self.f.write(",")
        self.f.write(str(value[0]))
        self.f.write(",")
        self.f.write(str(value[1]))
        self.f.write(",")
        self.f.write(str(value[2]))
        self.f.write(",")
        self.f.write(str(value[3]))
        self.f.write(",")
        self.f.write(str(value[4]))
        self.f.write(",")
        self.f.write(str(value[5]))
        self.f.write(",")
        self.f.write(str(value[6]))
        self.f.write(",")
        self.f.write(str(value[7]))
        self.f.write("\n")

    def close(self):
        self.f.close()
