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
def main():
    def asking():
        print("\n    >> All mixup                 >  A");sleep(interval)
        print("    >> For LowerCase             >  L");sleep(interval)
        print("    >> For UpperCase             >  U");sleep(interval)
        print("    >> Upper/Lower Mixup         >  M");sleep(interval)
        print("    >> For Numbers               >  N");sleep(interval)
        print("    >> For Punctuation           >  P");sleep(interval)
        print("    >> For Exit                  >  E");sleep(interval)
    asking()
    

    def all():
        ask = int(input("Type your password lenght: "))
        password = "".join(choice(character) for i in range(ask))
        print(ask,"words password generated:🤓️ \n\t\t\t  └─>",password,'\n')

    def lower():
        ask = int(input("Type your password lenght: "))
        password = "".join(choice(lower_case) for i in range(ask))
        print(ask,"words password generated:🤓️ \n\t\t\t  └─>",password,'\n')

    def upper():

    
        ask = int(input("Type your password lenght: "))
        password = "".join(choice(upper_case) for i in range(ask))
        print(ask,"words password generated:🤓️ \n\t\t\t  └─>",password,'\n')

    def mix():
    
        ask = int(input("Type your password lenght: "))
        password = "".join(choice(mix_ascii) for i in range(ask))
        print(ask,"words password generated:🤓️ \n\t\t\t  └─>",password,'\n')

    def num():

    
        ask = int(input("Type your password lenght: "))
        password = "".join(choice(numbers) for i in range(ask))
        print(ask,"words password generated:🤓️ \n\t\t\t  └─>",password,'\n')

    def punc():

    
        ask = int(input("Type your password lenght: "))
        password = "".join(choice(punctuation) for i in range(ask))
        print(ask,"words password generated:🤓️ \n\t\t\t  └─>",password,'\n')

    def exit():

    
        print("Thanks for using :-)\n")
        exit()
    
    
    repeat = input("Repeat? y or n: ")
    
    if str(repeat) == 'Y' or str(repeat) == 'y':
            os.system("exec passgen")
    else:
        print("Good byy")
        exit()



your_choice = input("\nchoose your option: ")
if str(your_choice) == "A" or str(your_choice) == 'a':
    all('add')
elif str(your_choice) == 'L' or str(your_choice) == 'l':
    lower()
elif str(your_choice) == 'U' or str(your_choice) == 'u':
    upper()
elif str(your_choice) == "M" or str(your_choice) == 'm':
    mix()
elif str(your_choice) == "N" or str(your_choice) == 'n':
    num()
elif str(your_choice) == "P" or str(your_choice) == 'p':
    punc()
elif str(your_choice) == 'E' or str(your_choice) == 'e':
    exit()
else:
    main()