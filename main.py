# -*- coding: utf-8 -*-
from Realtime_plot import realtime
from make_axis import axis, axis_array
from sample_thread import sample_thread
import time

# import threading
# import mcp3208
# import time
# import file_write


'''
def runner():
    Adc = mcp3208.mcp3208(Voltage_divider=5)

    file = file_write.file_write()
    Start_time = time.time()
    Time_sample = 0.040
    Data_number = 0
    while True:
        Mesurement_time = time.time() - Start_time
        if Mesurement_time > Data_number * Time_sample:
            V = Adc.read_all()
            file.write(Mesurement_time, V)
            x.update(Mesurement_time)
            y.update(V)
            Data_number += 1
'''


def main():
    print("program started")

    x = axis()
    y = axis_array(Array_length=8)
    Realtime = realtime(Quantity_data=8)
    Sample_thread = sample_thread(x, y)
    Sample_thread.start()
    # Sample_thread = threading.Thread(target=runner, name="Sample_thread")
    # Sample_thread.start()

    time.sleep(5)

    while True:
        Realtime.plot(x.axis[:], y.axis[:])
        Realtime.pause()


if __name__ == "__main__":
    main()
