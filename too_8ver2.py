#!/usr/bin/env python3
"""
Programm, mis arvutab mingi suvalise arvu ruutjuure
"""

__author__ = "Heidi Lees"
__copyright__ = "Copyright 2015, Minufirma"
__credits__ = ["Heidi Lees", "Taaniel Jakobson", "Tiina Aid"]
__version__ = "0.001"
__email__ = "heidi_lees@hotmail.com"



from math import sqrt

def ruutjuur(n):  #arvutab mingi arvu ruutjuure
	return sqrt(n)
	
def main():
	print("arvu n ruutjuur")
	n = int(input())
	ruutjuur(n)
	text_file = open("Vastus.txt", "w")
	text_file.write(str(ruutjuur(n)))
	text_file.close()

if __name__ == "__main__":
	main()
	

