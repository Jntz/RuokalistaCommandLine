# -*- coding: utf-8 -*-
from modules import *
from classes import *

def main():
	clear()
	print "RESEPTIN LUONTI (pääset takaisin kirjoittamalla 'exit')"
	name = read_input("Kirjoita reseptin nimi:")
	if name == 'exit':
		return
	category = read_input("Hyvä. Kirjoitappa sitten mihin kategoriaan se kuuluu?")
	if category == 'exit':
		return
	recept = Recipe(name, category)
	save_to_file(recept)