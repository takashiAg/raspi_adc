# -*- coding: utf-8 -*-
from mcp3208 import mcp3208
import time
import file_write


def main():
    Adc = mcp3208()
    Start_time = time.time()

    file=file_write.file_write("a")

    Time_sample = 0.020
    i=1
    while True:
        times = time.time()
        if Start_time < times - i:
            V = Adc.read_all()
            file.write(times,V)
            i += Time_sample

    file.close()

if __name__ == "__main__":
    main()
