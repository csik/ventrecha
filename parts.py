import Adafruit_BBIO.GPIO as GPIO 
from time import sleep as sleep
import machine as machine_cfg

class Valve: 
    def __init__(self, pin, no_or_nc): 
        self.pin = pin 
        self.no_or_nc = no_or_nc 
        GPIO.setup(self.pin, GPIO.OUT) 
    
    def open(self): 
        GPIO.output(self.pin, self.no_or_nc & 1) 
    
    def close(self): 
        GPIO.output(self.pin, self.no_or_nc & 0) 

class Hall:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def get():
        return GPIO.input(self.pin)



vMasterNC = Valve(machine_cfg.vMasterNC, machine_cfg.vMasterNC_state)
vReservoirstopNC = Valve(machine_cfg.vReservoirstopNC, machine_cfg.vReservoirstopNC_state)
vExhaleNO = Valve(machine_cfg.vExhaleNO, machine_cfg.vExhaleNO_state)

hUp = Hall(machine_cfg.hUp)
hDown = Hall(machine_cfg.hDown)


