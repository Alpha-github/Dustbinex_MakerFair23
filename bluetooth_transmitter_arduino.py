import serial
import time

print("Start")
port = "COM16"
bluetooth=serial.Serial(port,9600)
print("Connected")
bluetooth.flushInput()
# for i in range(5):
bluetooth.write(b"1")
time.sleep(0.1)
bluetooth.close()
print("Done")