# -*- coding: utf-8 -*-
from Realtime_plot import realtime
from make_axis import axis, axis_array
from sample_thread import sample_thread
import time


def main():
    print("program started")

    Realtime = realtime(Quantity_data=8)
    x = axis()
    y = axis_array(Array_length=8)
    Sample_thread = sample_thread(x,y,Realtime)
    Sample_thread.start(x,y)

    time.sleep(5)

    while True:
        Realtime.plot(x.axis,y.axis)
        Realtime.pause()


if __name__ == "__main__":
    main()
