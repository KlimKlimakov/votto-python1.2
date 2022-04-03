from colorama import init
from colorama import Fore, Back, Style
from time import sleep
import os

init()

def Update():
	os.system("cls")

	
def PrintColor(text = str(), color = str()):
	if color == "blue":
		print(Fore.BLUE + text) 
		
	if color == "red":
		print(Fore.RED + text)
		
	if color == "white":
		print(Fore.WHITE + text)
	
	if color == "green":
		print(Fore.GREEN + text)
		
	if color == "yellow":
		print(Fore.YELLOW + text)
	
	if color == "cyan":
		print(Fore.CYAN + text)
	
	if color == "magenta":
		print(Fore.MAGENTA + text)
			
	if color == "black":
		print(Fore.BLACK + text)
		

def PrintBg(text2 = str(), color2 = str()):
	if color2 == "blue":
		print(Back.BLUE + text2)
		
	if color2 == "red":
		print(Back.RED + text2)
	
	if color2 == "white":
		print(Back.WHITE + text2)
	
	if color2 == "green":
		print(Back.GREEN + text2)
	
	if color2 == "yellow":
		print(Back.YELLOW + text2)
	
	if color2 == "cyan":
		print(Back.CYAN + text2)
	
	if color2 == "magenta":
		print(Back.MAGENTA + text2)
	
	if color2 == "black":
		print(Back.BLACK + text2)



def Dim(text3 = str()):
	print(Style.DIM + text3)	

def Normal(text4 = str()):
	print(Style.NORMAL + text4)

def Bright(text5 = str()):
	print(Style.BRIGHT + text5)

def Reset(text6 = str()):
	print(Style.RESET_ALL + text6)	


def PrintVert(print_vert = str(), sec = int()):

	for i in print_vert:
		sleep(sec)
		print(i)

def PrintHor(print_hor = str(), sec2 = int()):

	for j in print_hor:
		sleep(sec2) 
		print(j, end = "", flush = True )