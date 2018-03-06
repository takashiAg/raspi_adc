# -*- coding: utf-8 -*-
from mcp3208 import mcp3208


def main():
    Adc=mcp3208()
    while True:
        inputVal0 = Adc.read(0)
        print(inputVal0)

if __name__=="__main__":
    main()
