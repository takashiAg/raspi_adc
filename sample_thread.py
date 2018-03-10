import threading
import mcp3208
import time
import file_write
from make_axis import axis, axis_array


class sample_thread(threading.Thread):

    """docstring for TestThread"""

    def __init__(self):
        super(sample_thread, self).__init__()

    def run(self,Realtime):
        Adc = mcp3208.mcp3208()

        file = file_write.file_write("a")
        Start_time = time.time()
        x = axis()
        y = axis_array(Array_length=8)
        Time_sample = 0.020
        Data_number = 0
        while True:
            Mesurement_time = time.time() - Start_time
            if Mesurement_time > Data_number * Time_sample:
                V = Adc.read_all()
                file.write(Mesurement_time, V)
                x.update(Mesurement_time)
                y.update(V)
                Realtime.plot(x.axis, y.axis)