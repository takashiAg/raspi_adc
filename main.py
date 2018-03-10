# -*- coding: utf-8 -*-
import mcp3208
import time
import file_write


def main():
    print("program started")

    Adc = mcp3208.mcp3208()

    file = file_write.file_write()
    Start_time = time.time()
    Time_sample = 0.020
    Data_number = 0
    while True:
        Mesurement_time = time.time() - Start_time
        if Mesurement_time > Data_number * Time_sample:
            V = Adc.read_all()
            file.write(Mesurement_time, V)
            Data_number += 1


if __name__ == "__main__":
    main()
