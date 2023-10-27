from machine import Pin
from neopixel import NeoPixel
import time
        
class neo8x32:
    def __init__(self, pin):
        self.np = NeoPixel(pin, 256)

    def show(self,dat):
        self.np.fill((0,0,0))
        self.np.write()
        time.sleep(1)

        for y in range(1,9):
            for x in range(0,32):
                d = dat[(y-1)*32+x]
                b=(d)%16
                g=(d>>8)%16
                r=(d>>16)%16

                if y % 2:
                    np = (y-1)*32+x
                    self.np[np]=(r,g,b)
                    #print(np)
                else: 
                    p = (y*32-x)-1
                    self.np[p]=(r,g,b)
                    #print(p)
            

        self.np.write()

np = neo8x32(Pin(0,Pin.OUT))

npdat=[0x000000]
for y in range(0,256):
    npdat.append(0x000000)

for a in range(0,24): npdat[a] = 0xFF0000
for b in range(24,32): npdat[b] = 0x00FF00
for c in range(32,45): npdat[c] = 0xFF00FF
for d in range(64,70): npdat[d] = 0x0000FF

for d in range(192,212): npdat[d] = 0xFFF00

for d in range(224,240): npdat[d] = 0xFFFFF

np.show(npdat)