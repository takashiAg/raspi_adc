# -*- coding: utf-8 -*-

from RPi import GPIO


class mcp3208():
    def __init__(self, SPICLK=11, SPIMOSI=10, SPIMISO=9, SPICS=8):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICS, GPIO.OUT)
        self.cs = SPICS
        self.ck = SPICLK
        self.mosi = SPIMOSI
        self.miso = SPIMISO

    def read(self, adcnum):
        if adcnum > 7 or adcnum < 0:
            return -1
        GPIO.output(self.cs, GPIO.HIGH)
        GPIO.output(self.ck, GPIO.LOW)
        GPIO.output(self.cs, GPIO.LOW)

        commandout = adcnum
        commandout |= 0x18
        commandout <<= 3
        for i in range(5):
            if commandout & 0x80:
                GPIO.output(self.mosi, GPIO.HIGH)
            else:
                GPIO.output(self.mosi, GPIO.LOW)
            commandout <<= 1
            GPIO.output(self.ck, GPIO.HIGH)
            GPIO.output(self.ck, GPIO.LOW)
        adcout = 0
        # 13ビット読む（ヌルビット＋12ビットデータ）
        for i in range(13):
            GPIO.output(self.ck, GPIO.HIGH)
            GPIO.output(self.ck, GPIO.LOW)
            adcout <<= 1
            if i > 0 and GPIO.input(self.miso) == GPIO.HIGH:
                adcout |= 0x1
        GPIO.output(self.cs, GPIO.HIGH)
        return adcout

    def read_all(self):
        read_adc = []
        for i in range(7):
            read_adc.append(self.read(i))
        return read_adc
