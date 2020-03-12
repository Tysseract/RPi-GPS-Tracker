import math
import serial
import time

class SIM868:
    def __init__(self):
        self.sp = serial.Serial('COM5', 115200)

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



SIM = SIM868()
SIM.write("AT+CGNSPWR=1")
SIM.write("AT+CGNSURC=1")

n_cont = "y"
while n_cont != "n":
    SIM.get()
    n_cont = input("continue?")

Command = input("command: ")
while Command is not "":
    SIM.write(Command)
    Command = input("command: ")

# AT+CGNSURC
