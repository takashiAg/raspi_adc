


class sample_thread(threading.Thread):
    def __init__(self):
        super(sample_thread, self).__init__()

    def run(self):
        Adc = mcp3208.mcp3208(Voltage_divider=5)

        file = file_write.file_write()
        Start_time = time.time()
        Time_sample = 0.020
        Data_number = 0
        while True:
            Mesurement_time = time.time() - Start_time
            if Mesurement_time > Data_number * Time_sample:
                V = Adc.read_all()
                file.write(Mesurement_time, V)
                self.x.update(Mesurement_time)
                self.y.update(V)
                Data_number += 1
