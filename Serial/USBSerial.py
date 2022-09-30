"""
This file is the Serial Communications
@Author: Chandrasekhar
@Package: pyserial == 3.5
"""

import serial
import time
import re

SerialDic = {}


# Check Enable Port
# import serial.tools.list_ports
# port_list = list(serial.tools.list_ports.comports())
# print(port_list)
# if len(port_list) == 0:
#    print('\033[1;31mENABLE PORT IS NONE\33[0m')
# else:
#     for i in range(0,len(port_list)):
#         print(port_list[i])
# portx = 0
# baud =9600, outtime=0.4


def usb2serial_init(portx, baud=9600, outtime=0.4, *args, **kwargs):
    """
    This is the initialization of the USB to Serial.

    Parameters:
        portx: the port, e.g. /dev/ttyUSB0" in Linux"; "COM5" in Windows
        baud:
            Default: 9600
            Option: 9600,19200,38400,57600,115200
        outtime: timeout
            Default: 0.4

    Return:
        Return the state of the connection
    """

    global SerialDic
    SerialDic = {'portx':portx, 'baud':baud, 'outtime':outtime}
    if kwargs:
        SerialDic.update(kwargs)
    try:
        ser = serial.Serial(portx, baud, timeout=outtime)
        print("\033[1;33mThe port is Open\033[0m")
        ser.close()
        return True
    except Exception as err:
        print(f"\033[1;31m ====== Initialization Error ====== \n {err}\033[0m""")
        return False


def usb2serial_at(string, result_print=True):
    """
    This is the Test of the Serial, Command: AT

    Parameters:
        string: the word want to write
        result_print: whether print the value
    """

    global SerialDic
    try:

        # portx = "COM5"
        # #
        # bps = 9600
        # # Timeout: NONE(forever); UNIT: s(second)
        # outtime = 0.4
        # # 打开串口，并得到串口对象
        ser = serial.Serial(SerialDic['portx'], SerialDic['baud'], timeout=SerialDic['outtime'])
        ser.flushInput()  # Clean Cache
        ser.write(f"{string}\r\n".encode())

        SerialReturn_1 = ser.readline()

        # print(type(SerialReturn_1))
        # SerialReturn_2 = ser.readline()
        # SerialReturn = str(SerialReturn, encoding='gbk')
        # print(str(SerialReturn_1) + "\n" + str(SerialReturn_2))
        if result_print:
            print(str(SerialReturn_1)+"  Re:"+(re.search(r'[0-9]+\.[0-9]+', (str(SerialReturn_1))).group())+"    ", end="", flush=True)
        ser.close()
        return SerialReturn_1

    except Exception as err:
        print(f"\033[1;31m ====== Error ====== \n {err}\033[0m""")


if __name__ == "__main__":
    usb2serial_init("COM5")
    # usb2serial_at("AT+V")
    while 1:
        get_Voltage = usb2serial_at("AT+V")
        get_Current = usb2serial_at("AT+C")
        time.sleep(0.3)
        print("\r\r", end='', flush=True)