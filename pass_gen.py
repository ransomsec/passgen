#! /usr/bin/python3
#created by @ransomsec

import os
import string
from time import sleep
from random import randint, choice

os.system("clear")
interval = 0.05

character = string.ascii_letters + string.digits + string.punctuation
lower_case = string.ascii_lowercase 
upper_case = string.ascii_uppercase
mix_ascii = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

def banner():
    print("\n\t██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗");sleep(interval)
    print("\t██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║");sleep(interval)
    print("\t██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║");sleep(interval)
    print("\t██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║");sleep(interval)
    print("\t██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║");sleep(interval)
    print("\t╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝");sleep(interval)
    print("\t         Password generator Created by: @ransomsec   v1.1.1");sleep(interval)
banner()
def asking():
    print("\n    >> All mixup                 >  A");sleep(interval)
    print("    >> For LowerCase             >  L");sleep(interval)
    print("    >> For UpperCase             >  U");sleep(interval)
    print("    >> Upper/Lower Mixup         >  M");sleep(interval)
    print("    >> For Numbers               >  N");sleep(interval)
    print("    >> For Punctuation           >  P");sleep(interval)
    print("    >> For Exit                  >  E");sleep(interval)
asking()

your_choice = input("\n    *> choose your option: ")
if str(your_choice) == "A" or str(your_choice) == 'a':
    ask = int(input("Type your password lenght: "))
    password = "".join(choice(character) for i in range(ask))
    print(f"{ask} words password generated:🤓️ \n\t\t\t  └─>",password,'\n')
elif str(your_choice) == 'L' or str(your_choice) == 'l':
    ask = int(input("Type your password lenght: "))
    password = "".join(choice(lower_case) for i in range(ask))
    print(f"{ask} words password generated:🤓️ \n\t\t\t  └─>",password,'\n')
elif str(your_choice) == 'U' or str(your_choice) == 'u':
    ask = int(input("Type your password lenght: "))
    password = "".join(choice(upper_case) for i in range(ask))
    print(f"{ask} words password generated:🤓️ \n\t\t\t  └─>",password,'\n')
elif str(your_choice) == "M" or str(your_choice) == 'm':
    ask = int(input("Type your password lenght: "))
    password = "".join(choice(mix_ascii) for i in range(ask))
    print(f"{ask} words password generated:🤓️ \n\t\t\t  └─>",password,'\n')
elif str(your_choice) == "N" or str(your_choice) == 'n':
    ask = int(input("Type your password lenght: "))
    password = "".join(choice(numbers) for i in range(ask))
    print(f"{ask} words password generated:🤓️ \n\t\t\t  └─>",password,'\n')
elif str(your_choice) == "P" or str(your_choice) == 'p':
    ask = int(input("Type your password lenght: "))
    password = "".join(choice(punctuation) for i in range(ask))
    print(f"{ask} words password generated:🤓️ \n\t\t\t  └─>",password,'\n')
elif str(your_choice) == 'E' or str(your_choice) == 'e':
    print("Thanks for using :-)\n")
    exit()
else:
    os.system('exec passgen')

repeat = input("Repeat? y or n: ")

if str(repeat) == 'Y' or str(repeat) == 'y':
        os.system('exec passgen')
else:
    print("Good byy")
    exit()