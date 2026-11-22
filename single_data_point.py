from time import sleep

import csv
import os
import numpy
import pyvisa
 
# Ask for a CSV file name, relative to this script's folder
script_dir = os.path.dirname(os.path.abspath(__file__)) + "\\data"
print(script_dir)
while True:
    name = input("CSV file name: ")
    path = os.path.join(script_dir, name)
    if not os.path.exists(path):
        break
    answer = input(f"{name} already exists. Append to the end of it? (y/n) ")
    if answer.lower() == "y":
        break
 
file = open(path, "a", newline="")
writer = csv.writer(file)

# How many measurements
N = input("How many measuremnts?: ")

# Setup the Keithley
k = pyvisa.ResourceManager().open_resource("GPIB0::24::INSTR")
k.timeout = 60000  # ms

k.write("*RST")
k.write(":SOUR:FUNC CURR")
k.write(":SOUR:CURR 0")
k.write(":SOUR:DEL 0")
k.write(':SENS:FUNC "VOLT"')
k.write(":SENS:VOLT:RANG 0.2")     
k.write(":SENS:VOLT:NPLC 0.01")    
k.write(":SYST:AZER OFF")          
k.write(":DISP:ENAB OFF")          
k.write(":FORM:ELEM VOLT,TIME")    
k.write(":TRIG:DEL 0")
k.write(f":TRIG:COUN {N}")

k.write(":OUTP ON")
data = k.query_ascii_values(":READ?")
k.write(":OUTP OFF")
k.write(":DISP:ENAB ON")
 
v = data[0::2]
t = [x - data[1] for x in data[1::2]]  # Delta timestamps; the Keithley ouputs voltage, time, voltage, time, voltage, time...

for ti, vi in zip(t, v):
    writer.writerow([ti, vi])