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
    realtime = Realtime_plot.realtime(Quantity_data=5)
    while True:
        f = open(file_path, "r")
        data_string = [line for line in csv.reader(f)][-201:-1]
        f.close()
        data = np.float64([d for d in data_string]).T
        x_data = data[0]
        speaker_voltage = data[1] - data[2]
        input1 = data[3]
        input2 = data[4]
        input3 = data[5]
        y_data = [speaker_voltage, input1, input2, input3]
        realtime.plot(x_data, y_data, pause_time=0.1)

    if __name__ == "__main__":
        main()
