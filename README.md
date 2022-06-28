[TOC]

# 3D Printed Lamp

This is my version of a Voronoi blowball Flower lamp based off the design from [here](https://www.thingiverse.com/thing:2940151). The print was fairly quick and didn't use much material at all. 

![lamp](https://lh3.googleusercontent.com/StYr8McF1exLjC96acgAbXRflF-i-5PvHABdRBYxDT725wmqV5I4Mly6hz0aQabBD4xalUi-IHfzuwtgUlO00l7iVq10b0s_0cSSSP5fE2Ui5IOP-RR1NIPZhFt3rfdkbWHnUUK9qdHPlmNBwiMdTWw3HoqellWy87Zcil1RK-DAwqVYJrTUnjfW9gIgr2EmQBCI0yj6WCdOK4d3LerVIEt0nbJtvTwXQh4fMUgZBBP3M-M1BAZPQEFgWRypfuDl7ywG_AnhzJZn4sk_I6zpVEGW7dmTEVfRLQRFKkA6Ply-jmLl7AJFIfvb8P7AIBWnapo4T_122E-LWqZtyfUkV4wHr1mBeCI_H4CaLt-ZRw9kOV8y2LDCccPf4WFDh05pQH_1RBpOA8aOftc9M6SOyXE-e9maZ0iTJgM6HaLq_ZcyiUFDR-4U38Kk0oDeup4Kh2Et6ioOxJua7QI0QnZZHTXDShVzJ__zPDWoKBvVkHZ1IfKmc5Cq2HxwbkotQKBmytP0AkxzYMJxEpNmraOWQ0En8Ycz8AIQVwL548niQ6fxQYJHgt_a56_TBZg_KGdWeIMkiZRHpbIOsO10idHBN7ZbNBLSXzcMUCSeOIiHw_YR4fK8NqQ206XwOUyOtDka_Y3hwrscWSQRk-oon_-KRcNfAdueuhNEJUOfzntwacBOkHs9L79ZoIbsDNxc7R6wQlpdKoHFU4woUTe8it4kEwNbuYV9mOqMs-_2fKBITwWJvFla-oJAUsD6QebrG9LWsXxMZcfWi-c1tQCdejpnms7JFU3yTUyCkgUS=w1062-h1416-no?authuser=2)

### Here are the parts used

- PLA filament for the printed parts.

- Adafruit QT Py - SAMD21 Dev Board with STEMMA QT. [Link](https://core-electronics.com.au/adafruit-qt-py-samd21-dev-board-with-stemma-qt.html)

- NeoPixel RGBW Mini Button PCB x3. [Link](https://core-electronics.com.au/neopixel-rgbw-mini-button-pcb-pack-of-10.html)

or

- Wemos D1 Mini

- Thin wire.

- Usb-c cable for power.

### Method 1: Using CircuitPython & QT PY

1. Flash the QT Py with the latest verison of [CircuitPython](https://circuitpython.org/downloads). And download the latest [libraries](https://circuitpython.org/libraries).
2. Wire the NeoPixels up in serial, each pcb has a GND, V, IN, and OUT pin. Connect the IN on the 1st NeoPixels to the data pin on the QT Py and the OUT to the IN on the next NeoPixel, and repeat. 
3. Glue the lamp together.
4. Use the lamp.py script.

### Method 2: Using Esphome & Wemos D1 Mini