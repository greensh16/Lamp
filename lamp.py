# CircuitPython
import neopixel
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixel_pin = board.A3
num_pixels = 3

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False,
                           pixel_order=(1, 0, 2, 3))

WHITE = (255, 255, 255, 255)

while True:
    
    if switch.value == False:
        counter += 1

    if counter == 0:
        pixels.fill(OFF)
        pixels.show()
        
    elif counter == 1:
        pixels.fill(WHITE)
        pixels.show()
        
    elif counter == 3:
        counter = 0

    time.sleep(0.2)