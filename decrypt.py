#!/usr/bin/python3
from ciphers import *
from recognize import *
ascii_art = """
________                                      __   
\______ \   ____   ___________ ___.__._______/  |_ 
 |    |  \_/ __ \_/ ___\_  __ <   |  |\____ \   __\\
 |    `   \  ___/\  \___|  | \/\___  ||  |_> >  |  
/_______  /\___  >\___  >__|   / ____||   __/|__|  
        \/     \/     \/       \/     |__|         
""".strip()
import argparse
import sys
from colorama import Fore, Back, Style

parser = argparse.ArgumentParser(
	prog = "decrypt",
	description = "decrypt is a CLI utility to decrypt strings in common encryption methods",
)
parser.add_argument("text", nargs="*", help="Ascii text to decode", type=str)
parser.add_argument('-t',"--target", metavar="str", help="Portion of expected string in decrypted result", type=str)
parser.add_argument("--nostrip", help="Don't strip input text", action="store_true")
args = parser.parse_args()

if args.text == []:
	args.text = ["".join(sys.stdin)]
args.text = " ".join(args.text)
if not args.nostrip:
	args.text = args.text.strip()
	
def style(arg):
	print(arg,end='')

F_WIDTH = 8
def attempt(string, name, func):
	res = func(args.text)
	style(Fore.RED)
	print(f"{name}".ljust(F_WIDTH)+": "+ res)
	style(Style.RESET_ALL)

attempt(args.text, "ROT13", lambda s: caesar(s, 13))