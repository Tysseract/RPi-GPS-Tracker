#!/usr/bin/python3
# GNSS Logger and Reporter

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