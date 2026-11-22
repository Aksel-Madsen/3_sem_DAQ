import csv
import os
import nidaqmx
from nidaqmx.constants import TerminalConfiguration
 
# Ask for a CSV file name, relative to this script's folder
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, "test_data.csv")

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
 
while True:
    input("Press enter ")
    samples = task.read(number_of_samples_per_channel=1000)
    writer.writerow(samples)
    file.flush()
