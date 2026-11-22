import pyvisa

k = pyvisa.ResourceManager().open_resource("GPIB0::24::INSTR")
k.timeout = 20000  # ms

k.write("*RST")
k.write(":SOUR:FUNC CURR")
k.write(":SOUR:CURR 0")
k.write(':SENS:FUNC "VOLT"')
k.write(":SENS:VOLT:RANG 0.2")     # 200 mV range
k.write(":SENS:VOLT:NPLC 10")      # 200 ms per reading, cancels 50 Hz hum
k.write(":FORM:ELEM VOLT")
k.write(":OUTP ON")
print(float(k.query(":READ?")), "V")
k.write(":OUTP OFF")
