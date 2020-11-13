import serial

ser = serial.Serial('/dev/ttyACM0', timeout=2)
ser.setRTS(True)
ser.setRTS(False)
while 1:
    line = ser.readline()
    print(line)
ser.close
