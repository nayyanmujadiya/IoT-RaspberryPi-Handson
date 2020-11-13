import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write(str.encode('3’)) # for python 3
