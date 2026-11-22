# Opsætning

## Drivere

- [NI-488.2](https://www.ni.com/en/support/downloads/drivers/download.ni-488-2.html) – driver til NI GPIB-USB-HS-adapteren (Keithley 2400)
- [NI-VISA](https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html) – bruges af `pyvisa`
- [EA USB-driver](https://elektroautomatik.com/en/?p=4724) – virtuel COM-port til EA PS 2000 B (installeres ofte automatisk af Windows)

## Python-biblioteker

```bash
python -m pip install eaps2000 pyvisa numpy pyserial
```
