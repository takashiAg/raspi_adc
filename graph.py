# -*- coding: utf-8 -*-

import make_axis
import Realtime_plot
import csv
import os
import numpy as np
import time


def current_file_path():
    base = os.path.dirname(os.path.abspath(__file__))
    current_file = os.path.normpath(os.path.join(base, "data", "current_file"))
    f = open(current_file, 'r')
    Data_file = f.readline()
    f.close()
    return Data_file


def main():
    time.sleep(10)
    file_path = current_file_path()
    realtime = Realtime_plot.realtime()
    while True:
        f = open(file_path, "r")
        data_string = [line for line in csv.reader(f)][-201:-1]
        f.close()
        data = np.float64([d for d in data_string]).T
        realtime.plot(data[0], data[1:], pause_time=0.1)


if __name__ == "__main__":
    main()
