from parts import *

while(1):
     vMasterNC.open()
     vReservoirstopNC.close()
     print("filling reservoir") 
     sleep(.7) 
     vMasterNC.close()
     vExhaleNO.close()    
     vReservoirstopNC.open()
     print("inhalation")
     sleep(2)
     vExhaleNO.open()
     vReservoirstopNC.close()
     print("exhalation")
     sleep(2)

