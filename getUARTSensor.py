# Each command or return：
# Contains 9 bytes (byte 0 ~ 8)
# starting byte fixed 0 XFF
# command contains sensor number (factory default to 0 x01)
# to check and end
#
#
# Command List:
# 0x86 Gas concentration
# 0x87 Calibrate zero point（ZERO）
# 0x88 Calibrate span point（SPAN）
#
################################ SEND COMMAND ##########################
# Byte0   Byte1   Byte2   Byte3   Byte4   Byte5   Byte6   Byte7   Byte8
# --------------------------------------------------------------------
# Start  |Sensor |Command|-       -       -       -       -       Check
# ing    |No.    |       |      |       |       |       |       | value
# byte
# 0XFF   |0x01   |0x86   |0x00  |0x00   |0x00   |0x00   |0x00   |0x79
#
############################## RETURND COMMAND ##########################
# Byte0   Byte1   Byte2   Byte3   Byte4   Byte5   Byte6   Byte7   Byte8
# --------------------------------------------------------------------
# Start  |Command|High   |Low    | -     | -     | -     | -     |Check
# ing    |No.    |Level  |Level  |       |       |       |       |value
# byte   |       |Contrn |Contrn |
# 0XFF   |0x86   |0x86   |0x00   |0x00   |0x00   |0x00   |0x00   |0xD1




import Adafruit_BBIO.UART as UART
import serial
from time import sleep

UART.setup("UART2")

ser = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
    print("Serial is open!")
    packet = (b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79')
    while(1):
        ser.write(packet)
        result = b''
        while(len(result)<9):
            result = ser.read(9)
            print(result)
        result = result[2]*256+result[3]
        print(result)
        sleep(1)


ser.close()
