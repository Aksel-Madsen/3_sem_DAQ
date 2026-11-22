import serial, time

PORT = "" # For Gaussmeter
baud = 9600

with serial.Serial(PORT, baud, timeout=1) as s:
    s.reset_input_buffer()
    time.sleep(1.5)
    data = s.read(200)
    print(baud, repr(data))