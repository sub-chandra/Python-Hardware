import USBSerial
import time
import re

ConnectionTest = USBSerial.usb2serial_init("COM5")


def _get_resistant():
    '''
    Get the voltage and current, calculate resistant.

    Returns:
        Resistant(type float)
    '''
    global ConnectionTest
    if ConnectionTest is False:
        exit()

    b_get_voltage = USBSerial.usb2serial_at("AT+V", result_print=False)
    b_get_current = USBSerial.usb2serial_at("AT+C", result_print=False)
    f_get_voltage = float(re.search(r"[0-9]+\.[0-9]+", str(b_get_voltage)).group())
    f_get_current = float(re.search(r"[0-9]+\.[0-9]+", str(b_get_current)).group())
    if f_get_current > 0:
        f_resistant = f_get_voltage / f_get_current
        f_resistant = round(f_resistant, 3)
    else:
        f_resistant = 0.000
    print(f_resistant, end='', flush=True)
    time.sleep(0.2)
    print("\r", end='', flush=True)
    return f_resistant


# usb2serial_at("AT+V")

if __name__ == "__main__":
    while 1:
        # print(_get_resistant())
        _get_resistant()
