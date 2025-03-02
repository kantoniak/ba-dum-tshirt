# Ba-Dum-Tshirt

A T-shirt embroidered with conductive thread that plays sounds when the pads are touched.

## Required hardware

- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- Pimoroni's [Pico Audio Pack](https://pimoroni.com/audiopack)
- Any MPR121 touch sensor board, such as the [Adafruit #4830](https://www.adafruit.com/product/4830)
- A speaker with a mini-jack input

### Optional add-ons

For convenience and minimal soldering, the following were also used:
- Pimoroni's [Pico Omnibus](https://shop.pimoroni.com/products/pico-omnibus)
- [Adafruit PiCowbell Proto](https://www.adafruit.com/product/5200)
- A JST SH 4-pin cable

## Firmware setup

1. Install [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) on your Pico.
2. Copy [CircuitPython 9.x libraries](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20250228) to your pico. You only need a subset of files if you want to save on some space. Copy to `lib/` at least the following:
    * `adafruit_bus_device`
    * `adafruit_debouncer.mpy`
    * `adafruit_mpr121.mpy`
    * `adafruit_ticks.mpy`

## Acknowledgements

Sounds adapted from [*Ba-Dum-Tss* recording](https://freesound.org/people/VeinAdams/sounds/713649/) by [VeinAdams](https://freesound.org/people/VeinAdams/).
