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
	sub_category = read_input("Selvän teki. Kirjoitappa sitten mihin alakategoriaan resepti kuuluu (ei pakollinen, voi jättää tyhjäksi)", True)
	if sub_category == 'exit':
		return
	recept = Recipe(name, category, sub_category)
	save_to_file(recept)

def save_to_file(recept):
	old_data = get_recipes_data()
	old_data["recipes"].append(recept.save_data_to_file())
	write_json_to_file(old_data, filenames["recipes"])