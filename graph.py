# -*- coding: utf-8 -*-

import make_axis
import Realtime_plot
import csv
import os
import time


def current_file_path():
    base = os.path.dirname(os.path.abspath(__file__))
    current_file = os.path.normpath(os.path.join(base, "data", "current_file"))
    f = open(current_file, 'r')
    Data_file = f.readline()
    f.close()
    return Data_file


def main():
    file_path = current_file_path()

    f = open(file_path, "r")
    Time_sample = 0.020
    Data_number = 0
    x = make_axis.axis(sample=100)
    y = make_axis.axis_array(sample=100)
    while True:
        lines = [line for line in csv.reader(f)]
        print(lines[-100:])
        time.sleep(1)


if __name__ == "__main__":
    main()
