# -*- coding: utf-8 -*-

import make_axis
import Realtime_plot
import csv
import os
import numpy as np


def current_file_path():
    base = os.path.dirname(os.path.abspath(__file__))
    current_file = os.path.normpath(os.path.join(base, "data", "current_file"))
    f = open(current_file, 'r')
    Data_file = f.readline()
    f.close()
    return Data_file


def main():
    file_path = current_file_path()
    realtime = Realtime_plot.realtime()
    while True:
        f = open(file_path, "r")
        data = [line for line in csv.reader(f)][-100:]
        f.close()
        x_data = [float(d[0]) for d in data]
        y_data = [
            [float(d[1]) - float(d[2]) for d in data],
            [float(d[3]) for d in data],
            [float(d[4]) for d in data],
            [float(d[5]) for d in data],
        ]
        realtime.plot(x_data, y_data, pause_time=0.1)


if __name__ == "__main__":
    main()
