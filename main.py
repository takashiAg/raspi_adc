# -*- coding: utf-8 -*-
from mcp3208 import mcp3208

import time


def main():
    Adc = mcp3208()
    Start_time = time.time()
    f = open('text.txt', 'w')

    Time_sample = 0.020
    i=1
    while True:
        times = time.time()
        if Start_time < times - i:
            V = Adc.read_all()
            f.write(str(times))
            f.write(",")
            f.write(str(V[0]))
            f.write(",")
            f.write(str(V[1]))
            f.write(",")
            f.write(str(V[2]))
            f.write(",")
            f.write(str(V[3]))
            f.write(",")
            f.write(str(V[4]))
            f.write(",")
            f.write(str(V[5]))
            f.write(",")
            f.write(str(V[6]))
            f.write(",")
            f.write(str(V[7]))
            f.write("\n")
            i += Time_sample


    f.close()

if __name__ == "__main__":
    main()
