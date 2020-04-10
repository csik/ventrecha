from parts import *

vMasterNC.close()
vReservoirstopNC.close()
vExhaleNO.close()


GPIO.cleanup()
print("All valves should be off")

