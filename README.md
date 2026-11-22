# Opsætning

## Drivere

- [NI-488.2](https://www.ni.com/en/support/downloads/drivers/download.ni-488-2.html) – driver til NI GPIB-USB-HS-adapteren (Keithley 2400)
- [NI-VISA](https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html) – bruges af `pyvisa`
- [EA USB-driver](https://elektroautomatik.com/en/?p=4724) – virtuel COM-port til EA PS 2000 B (installeres ofte automatisk af Windows)

## Python-biblioteker

```bash
python -m pip install eaps2000 pyvisa numpy pyserial
```

## Sådan bruges programmet
1. Åben filen "new_collector.py"
2. Skriv et filnavn som den kan gemme data i, første gang man kører programmet skal man lave en mappe "data" i samme mappe som programmet ligger.
   Hvis filen allerede findes, vil programmet spørge om du er sikker, hvis du svarer ja, så appender den rows til slutningen af CSV filen.
5. Skriv start- og slutspænding, samt antalet af målepunkter man ønsker.
6. Vent, hvert målepunkt tager ca 0,7 sekunder; indstil "buffertime" variablen, hvis man ønsker det skal gå lidt hurtigere.
7. Til sidst kan CSV filen åbnes og plottes i Matlab, Excel, eller hvad man ønsker.
