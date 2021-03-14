import os
import sys
import random
import webbrowser
import urllib3
import requests
import ctypes
import string

with open("4bytecodes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print("\033[1;31;40m Valid | {} \n".format(line.strip("\n")))
            break
        else:
            print("\033[1;31;40m Invalid | {} \n".format(line.strip("\n")))
