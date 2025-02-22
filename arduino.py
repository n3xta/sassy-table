import serial

arduino = serial.Serial('/dev/cu.usbmodem2101', 9600)

def sendSignal(content):
    arduino.write(content.encode())
    
sendSignal("1")