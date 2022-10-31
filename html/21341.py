import serial


ser = serial.Serial('/dev/ttyAMA0',9600)

ser.write(b'SO05')
#ser.write(b'SC00')
