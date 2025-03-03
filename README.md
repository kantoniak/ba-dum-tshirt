# Ba-Dum-Tshirt

A T-shirt embroidered with conductive thread that plays sounds when the pads are touched.

<p align="center">
  <img src="readme/project-preview.jpg" width="200" />
</p>

## Embroidery

<p align="center">
  <img src="embroidery/tshirt-rev1-export.svg" width="200" />
</p>

Choose your preferred garment and embroider it using a compatible machine.
The design was created in Inkscape for a 200x280 mm hoop and can be digitized with [Ink/Stich](https://inkstitch.org/).
To fit the working area of the Janome MC400E, I had to split the design into two 200x200 mm sections.

Embroider the red areas with conductive thread and use regular embroidery thread for the black areas.
After assembling hardware, sew the touch-sensing board to the garment.
Use thick conductive thread to connect the conductive areas to the corresponding pads on the board.

## Hardware

### Required hardware

- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- Pimoroni's [Pico Audio Pack](https://pimoroni.com/audiopack)
- Any MPR121 touch sensor board, such as the [Adafruit #4830](https://www.adafruit.com/product/4830)
- A speaker with a mini-jack input

### Optional add-ons

For convenience and minimal soldering, the following were also used:
- Pimoroni's [Pico Omnibus](https://shop.pimoroni.com/products/pico-omnibus)
- [Adafruit PiCowbell Proto](https://www.adafruit.com/product/5200)
- A JST SH 4-pin cable

## Firmware

1. Install [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) on your Pico.
2. Copy [CircuitPython 9.x libraries](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20250228) to your pico. You only need a subset of files if you want to save on some space. Copy to `lib/` at least the following:
    * `adafruit_bus_device`
    * `adafruit_debouncer.mpy`
    * `adafruit_mpr121.mpy`
    * `adafruit_ticks.mpy`

## Enclosure

<p align="center">
  <img src="readme/enclosure-preview.png" width="200" />
</p>

This is currently more of a backplate and is entirely optional.
Cut the backplate (`laser-outline-rev1.pdf`) from 3 mm acrylic using a laser cutter.
Print two copies each of `holder-top.3mf` and `holder-bottom.3mf` using a 3D printer.
Sandwich the PCB under the clamps and secure it with four M3x13 mm screws.
Thread 1-inch webbing through the loops in the bottom parts and attach a side-release buckle to the free ends.
You can finish the ends of the webbing on a sewing machine.


## Acknowledgements

* I couldn't find the author of [the meme](https://knowyourmeme.com/memes/rimshot-ba-dum-tss)'s picture.
* Sounds adapted from [*Ba-Dum-Tss* recording](https://freesound.org/people/VeinAdams/sounds/713649/) by [VeinAdams](https://freesound.org/people/VeinAdams/).
