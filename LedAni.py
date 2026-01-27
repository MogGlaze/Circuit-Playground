import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    # indexes the first element of the 'pixels' list and points to the 
    # first (and only) Neopixel in the 'pixels' list
    pixels[0]=(0, 255, 0)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    pixels[1]=(0, 200, 0)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    pixels[2]=(160, 255, 0)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    pixels[3]=(150, 255, 70)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    
    pixels[4]=(200, 25, 89)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    
    pixels[5]=(59, 255, 80)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    
    pixels[6]=(59, 255, 90)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    
    pixels[7]=(255, 255, 0)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    
    pixels[8]=(0, 255, 255)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    
    pixels[9]=(255, 25, 0)
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.01)
    
    
    
    
