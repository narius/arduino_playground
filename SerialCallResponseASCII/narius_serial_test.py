import serial
import code
import io
import time

ser = serial.Serial('/dev/cu.usbserial-1410', timeout=10, baudrate=9600)
print("hej")
i = 0
time.sleep(3)

while i < 10:
    print("blue_on")
    ser.write(b'blue_on')
    #response = ser.readline()
    #code.interact(banner="While", local=locals())
    #print(str(response))
    time.sleep(5)
    print("blue off")
    ser.write(b'blue_off')
    time.sleep(5)
    i = i+1

ser.close()
