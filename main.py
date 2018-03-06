# -*- coding: utf-8 -*-
from mcp3208 import mcp3208

import time


def main():
    Adc=mcp3208()
    Start_time=time.time()
    while Start_time+10>time.time():
        inputVal0 = Adc.read(0)
        print(time.time(),inputVal0)
    print(time.time()-Start_time)
    Start_time=time.time()
    while Start_time+10>time.time():
        inputVal0 = Adc.read_all()
        print(inputVal0)
    print(time.time()-Start_time)


if __name__=="__main__":
    main()
