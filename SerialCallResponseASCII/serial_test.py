import serial
import code
import io
import time

ser = serial.Serial('/dev/cu.usbserial-1410', timeout=1, baudrate=9600)
print("hej")
i = 0
while i < 10:
    ser.write(b"moist")
    response = ser.readline()#.decode('ascii')
    code.interact(banner="While", local=locals())
    print(str(response))
    i = i+1

ser.close()
