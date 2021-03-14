import os
import sys
import random
import webbrowser
import urllib3
import requests
import ctypes
import string

# Stage 1 #
with open("16bytecodes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print("\033[1;31;40m Valid | {} \n".format(line.strip("\n")))
            break
        else:
            print("\033[1;31;40m Invalid | {} \n".format(line.strip("\n")))
input("press enter 4 times to close")
input("4")
input("3")
input("2")
input("1")
