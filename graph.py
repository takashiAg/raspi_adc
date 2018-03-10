# -*- coding: utf-8 -*-

import make_axis
import Realtime_plot
import csv
import os


def current_file_path():
    base = os.path.dirname(os.path.abspath(__file__))
    current_file = os.path.normpath(os.path.join(base, "data", "current_file"))
    f = open(current_file, 'w')
    Data_file = f.readline()
    f.close()
    return Data_file


def main():
    file_path = current_file_path()

    Time_sample = 0.020
    Data_number = 0
    x = make_axis.axis(sample=100)
    y = make_axis.axis_array(sample=100)
    while True:
        for line in csv.reader(file_path)[-100:]:
            print(line)


if __name__ == "__main__":
    main()
