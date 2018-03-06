class file_write():
    def __init__(self,filename):
        self.f = open(filename, 'w')

    def write(self,time,value):
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
