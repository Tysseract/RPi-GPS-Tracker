import math
import time
import SIM868


SIM = SIM868.SIM868()
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
