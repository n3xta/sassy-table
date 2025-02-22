import serial

arduino = serial.Serial('/dev/cu.usbmodem2101', 9600)

def send_signal(content):
    arduino.write(content.encode())
    
send_signal("1")