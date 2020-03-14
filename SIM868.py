import math
import sys
import serial
import time

class SIM868:
    def __init__(self):
        port = '/dev/ttyAMA0'
        if sys.platform.startswith('win'):
            port = 'COM5'
        self.sp = serial.Serial(port, 115200)

    def get(self):
        return_string = ""
        while self.sp.in_waiting > 0:
            text = str(self.sp.readline().decode('UTF-8').strip())
            print('SIM868: ' + text)
            return_string += text
        return return_string

    def write(self, command):
        command = str(command)
        print("You   : " + command)
        self.sp.write(command.encode())
        self.sp.write("\n".encode())
        self.get()