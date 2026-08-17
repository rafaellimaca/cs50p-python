import sys
from pyfiglet import Figlet
import random

message =  input("Write a string: ")
if len(sys.argv) == 1:
    fig = Figlet()
    fig = Figlet(font=random.choice(fig.getFonts()))
    final_text = fig.renderText(message)
    print(final_text)
elif len(sys.argv) == 3:
    fig = Figlet(font=sys.argv[2])
    final_text = fig.renderText(message)
    print(final_text)