from pyfirmata import Arduino, util
import time

print('start')
board = Arduino('/dev/cu.usbserial-1410')
pin3 = board.get_pin('d:4:o')
a = board.get_pin('a:4:i')
print('innan while')
while True:
    print('On')
    print(a.read())
    pin3.write(1)
    time.sleep(2)
    print(a.read())
    print('Off')
    pin3.write(0)
    time.sleep(2)
