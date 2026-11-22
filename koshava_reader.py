import serial
import serial.tools.list_ports

# List all COM ports so you can find the Koshava
for p in serial.tools.list_ports.comports():
    print(p.device, "-", p.description)
