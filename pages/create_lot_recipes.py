# -*- coding: utf-8 -*-
from modules import *
from classes import *

def main():
	clear()
	print "MONEN RESEPTIN LUONTI (pääset takaisin kirjoittamalla 'exit')"
	print "Tällä sivulla voit luoda monta reseptiä kerralla saman kategorian alle"
	category = read_input("Hyvä. Kirjoitappa sitten mihin kategoriaan se kuuluu?")
	if category == 'exit':
		return
	while True:
		name = read_input("Kirjoita reseptin nimi:")
		if name == 'exit':
			return

		recept = Recipe(name, category, "")
		save_to_file(recept)	
	

def save_to_file(recept):
	old_data = get_recipes_data()
	old_data["recipes"].append(recept.save_data_to_file())
	write_json_to_file(old_data, filenames["recipes"])