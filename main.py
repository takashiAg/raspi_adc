# -*- coding: utf-8 -*-
from mcp3208 import mcp3208
import time
import file_write
from Realtime_plot import realtime
from make_axis import axis


def main():
    Adc = mcp3208()
    Start_time = time.time()

    file = file_write.file_write("a")

    Realtime = realtime()
    x = axis()
    y = [axis(), axis(), axis(), axis(), axis(), axis(), axis(), axis()]
    Time_sample = 0.020
    Data_number = 0
    while True:
        Mesurement_time = time.time() - Start_time
        if Mesurement_time > Data_number * Time_sample:
            V = Adc.read_all()
            file.write(Mesurement_time, V)
            x.update(Mesurement_time)
            y[0].update(V[0])
            Realtime.plot(x.axis,y[0].axis)

            Data_number += 1

    file.close()


if __name__ == "__main__":
    main()
