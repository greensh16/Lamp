[TOC]

# 3D Printed Lamp

This is my version of a Voronoi blowball Flower lamp based off the design from [here](https://www.thingiverse.com/thing:2940151). The print was fairly quick and didn't use much material at all. 

![lamp]()

### Here are the parts used

- PLA filament for the printed parts.

- NeoPixel RGBW Mini Button PCB x3. [Link](https://core-electronics.com.au/neopixel-rgbw-mini-button-pcb-pack-of-10.html)

- Thin wire.

- Usb-c cable for power.

- Adafruit QT Py - SAMD21 Dev Board with STEMMA QT. [Link](https://core-electronics.com.au/adafruit-qt-py-samd21-dev-board-with-stemma-qt.html)

or

- Wemos D1 Mini

### Method 1: Using CircuitPython & QT PY

1. Flash the QT Py with the latest verison of [CircuitPython](https://circuitpython.org/downloads). And download the latest [libraries](https://circuitpython.org/libraries).
2. Wire the NeoPixels up in serial, each pcb has a GND, V, IN, and OUT pin. Connect the IN on the 1st NeoPixels to the data pin on the QT Py and the OUT to the IN on the next NeoPixel, and repeat. 
3. Glue the lamp together.
4. Use the lamp.py script.

### Method 2: Using Esphome & Wemos D1 Mini
1. Connect the D1 mini to your Home Assistant device.
2. Use Esphome to create a new device and set up an intial project.
3. Use the neopixel.yaml script after "captive_portal:".