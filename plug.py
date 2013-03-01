#!/usr/bin/env python

import factory
import calib
import serial
import cPickle

a = Calibrator()
readingList = []

port = str(raw_input("Serial Port: "))
baudrate = str(raw_input("Baud Rate: "))
ser = serial.Serial(port, baudrate)

while True:
    while count in range(a.maxVal):
        readingList.append(int(ser.readline().strip('\x00\r\n')))
        readingList = zip(readingList, [0] * len(readingList))
        ref = cPickle.load(open('dataset.p', 'rb'))
        ref = ref.values()
        ref = zip(ref, [0] * len(ref))
        scaled = factory.scale([factory.retSimilarity(ref, readingList, 1), \
                                factory.retSimilarity(ref, readingList, 2), \
                                factory.retSimilarity(ref, readingList, 3)])
        
        print classify(scaled)