# -*- coding: utf-8 -*-
from Realtime_plot import realtime
from sample_thread import sample_thread
import time


def main():

    print("program started")

    Realtime = realtime(Quantity_data=8)
    Sample_thread = sample_thread()
    Sample_thread.start(Realtime)


    time.sleep(5)

    while True:
        Realtime.pause()



if __name__ == "__main__":
    main()
