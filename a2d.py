from time import sleep
import Adafruit_BBIO.ADC as ADC

ADC.setup()
while(1):
    print(ADC.read("P9_33"))
    sleep(.1)

