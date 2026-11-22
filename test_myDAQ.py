from time import sleep

from eaps2000 import eaps2k
import csv
import os
import nidaqmx
import numpy
from nidaqmx.constants import TerminalConfiguration
 
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
 
# Setup channels for the myDAQ
task = nidaqmx.Task()
task.ai_channels.add_ai_voltage_chan(
    "myDAQ1/ai0",
    terminal_config=TerminalConfiguration.DIFF,
    min_val=-2,
    max_val=2,
)
task.timing.cfg_samp_clk_timing(1000)
 
file = open(path, "a", newline="")
writer = csv.writer(file)
 
I_0 = float(input("Lower Current limit "))
I_1 = float(input("Upper Current limit "))
N = int(input("Number of points "))
I_space = numpy.linspace(I_0, I_1, N)
 
#Initialize the supply config
cfg = eaps2k.get_config_template()
cfg['ACK'] = True
cfg['OVP'] = 10.0
cfg['OCP'] = 5.0
cfg['Vset'] = 9.0
 
buffertime = 0.5
 
for I in I_space:
    print(I)
    # First, adjust the config
    cfg['Iset'] = float(I)
    with eaps2k('COM4') as ps:
        ps.configure(cfg)
        # Enable the powersupply and wait
        ps.set_output_state(True)
        sleep(buffertime)
        ps.configure(cfg)
        # Enable the powersupply and wait
        ps.set_output_state(True)
        sleep(buffertime)
        samples = task.read(number_of_samples_per_channel=1000)
        ai0 = sum(samples) / len(samples)
        H_y = I*150*0.7155/0.1975
        # Calculate H_y from the Helmholtz equation
 
    print("Signal (mV):\t\t", ai0 * 1000)
    print("Coil current (A):\t", I)
    print("H_y [A/m]:\t\t", H_y)
 
    writer.writerow([I, ai0, H_y])
    file.flush()


cfg['Vset'] = 0
cfg['Iset'] = 0
ps.configure(cfg)
# Enable the powersupply and wait
ps.set_output_state(True)