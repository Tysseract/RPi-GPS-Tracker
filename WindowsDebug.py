import math
import serial
import time

class SIM868:
    def __init__(self):
        self.sp = serial.Serial('COM5', 9600)

    def get(self):
        return_string = ""
        read_next = True
        while read_next:
            text = str(self.sp.readline().decode('UTF-8').strip())
            print('SIM868: ' + text)
            return_string += text
            if text == 'OK' or text == 'ERROR':
                read_next = False
        return return_string

    def write(self, command):
        command = str(command)
        print("You   : " + command)
        self.sp.write(command.encode())
        self.sp.write("\n".encode())
        self.get()



SIM = SIM868()
SIM.write("AT+CGNSPWR=1")
SIM.write("AT+CGNSURC=0")

n_cont = "y"
while n_cont != "n":
    SIM.get()
    n_cont = input("continue?")

Command = input("command: ")
while Command is not "":
    SIM.write(Command)
    Command = input("command: ")

# AT+CGNSURC
