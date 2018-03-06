# -*- coding: utf-8 -*-
from mcp3208 import mcp3208

import time


def main():
    Adc = mcp3208()
    Start_time = time.time()
    f = open('text.txt', 'w')

    Time_sample = 0.100
    i=1
    while True:
        times = time.time()
        if Start_time < times + i:
            V = Adc.read(0)
            f.write(str(times))
            f.write("\n")
            i += Time_sample


    f.close()

if __name__ == "__main__":
    main()
