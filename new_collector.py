from time import sleep

# Importer biblioteker til at styre strømforsyning og Keithley sourcemeter
from eaps2000 import eaps2k
import csv
import os
import numpy
import pyvisa
 
# Spørg efter et filnavn, så programmet ved hvor filen skal gemmes i data mappen.
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
 
# Åben filen, så python kan tilgå den
file = open(path, "a", newline="")
writer = csv.writer(file)
 
# Spørg hvad den mindste og største strøm til spolen skal være
I_0 = float(input("Lower Current limit "))
I_1 = float(input("Upper Current limit "))
# Spørg hvor mange datapunkter man ønsker
N = int(input("Number of points "))

# Lav et lineært rum mellem de to grænser for strømmen
I_space = numpy.linspace(I_1, I_1, N)
# Læg negative værdier til det rum
I_space = numpy.concatenate((I_space, I_space[-2::-1]))

# Initialiser en konfiguration til strømforsyningen
cfg = eaps2k.get_config_template()
cfg['ACK'] = True
cfg['OVP'] = 10.0
cfg['OCP'] = 5.0
cfg['Vset'] = 20.0

# Opsæt Keithley forbindelse
k = pyvisa.ResourceManager().open_resource("GPIB0::24::INSTR")
k.timeout = 20000  # ms

# Skriv en konfiguration til Keithley
k.write("*RST")
k.write(":SOUR:FUNC CURR")
k.write(":SOUR:CURR 0")
k.write(':SENS:FUNC "VOLT"')
k.write(":SENS:VOLT:RANG 0.2")
k.write(":SENS:VOLT:NPLC 10")      # Langsomste mode; 200ms pr måling
k.write(":FORM:ELEM VOLT")
k.write(":OUTP ON")
 
buffertime = 0.5
 
for I in I_space:
    print(I)
    # Først, juster konfigurationen til den strøm vi er nået til
    cfg['Iset'] = float(I)
    with eaps2k('COM4') as ps:
        # Skriv konfigurationen over i strømforsyningen
        ps.configure(cfg)
        # Tænd for strømforsyningen
        ps.set_output_state(True)
    # Vent på at strømforsyningen har indstillet sig korrekt
    sleep(buffertime)
    H_y = I*150*0.7155/0.1975

    # Læs fra Keithley, gem værdien som "sig"
    sig = float(k.query(":READ?"))

    print("Coil current (A):\t", I)
    print("H_y [A/m]:\t\t", H_y)
    print("Signal [V]:\t\t", sig)
 
    writer.writerow([I, H_y, sig])
    file.flush()

# Negative værdier
input("Swap polarity and press enter:")

for I in I_space[1:]:
    print(I)
    # Først, juster konfigurationen til den strøm vi er nået til
    cfg['Iset'] = float(I)
    with eaps2k('COM4') as ps:
        # Skriv konfigurationen over i strømforsyningen
        ps.configure(cfg)
        # Tænd for strømforsyningen
        ps.set_output_state(True)
    # Vent på at strømforsyningen har indstillet sig korrekt
    sleep(buffertime)
    H_y = I*150*0.7155/0.1975

    # Læs fra Keithley
    sig = float(k.query(":READ?"))

    print("Coil current (A):\t", -I)
    print("H_y [A/m]:\t\t", H_y)
    print("Signal [V]:\t\t", sig)
 
    writer.writerow([-I, -H_y, sig])
    file.flush()

# Don't burn down the lab
print("Setting PS to 0 [A]")
cfg['Iset'] = 0
with eaps2k('COM4') as ps:
    ps.configure(cfg)