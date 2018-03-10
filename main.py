# -*- coding: utf-8 -*-
import mcp3208
import time
import file_write
from Realtime_plot import realtime
from make_axis import axis,axis_array


def main():
    Adc = mcp3208.mcp3208()
    Realtime = realtime()

    file = file_write.file_write("a")
    Start_time = time.time()
    x = axis()
    y = axis_array()
    Time_sample = 0.020
    Data_number = 0
    while True:
        Mesurement_time = time.time() - Start_time
        if Mesurement_time > Data_number * Time_sample:
            V = Adc.read_all()
            file.write(Mesurement_time, V)
            x.update(Mesurement_time)
            y.update(V)
            Realtime.plot(x.axis,y.axis)

            Data_number += 1

    file.close()


if __name__ == "__main__":
    main()
