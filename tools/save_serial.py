# 照度計などから送られてくるデータをCSV形式で保存
import sys
import serial
import datetime
import csv

ser = serial.Serial('/dev/cu.usbmodem14101',9600)

while(1):
    value = int(ser.readline().decode('utf-8').rstrip('\n'))
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(date,value)
    with open('/Users/ryotanomura/Documents/Arduino/illuminometer/test.csv', 'a') as f:
        print('{},{}'.format(date,value),file=f)