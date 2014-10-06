# -*- coding: utf-8 -*-
from modules import *
from classes import *

def main():
	clear()
	print "RESEPTIN LUONTI (pääset takaisin kirjoittamalla 'exit')"
	print "Kirjoita 1 jos haluat luoda yhden reseptin"
	print "Kirjoita 2 jos haluat luoda useamman reseptin samalla kategorialla"
	print "Kirjoita 3 jos haluat luoda useamman reseptin eri kategorioilla (samoja voi myös käyttää)"
	select = read_int("Pääset reseptin luonnista pois kirjoittamalla 'exit'")
	if select == 'exit': return
	elif select == 1:
		single_recipe()
	elif select == 2:
		multiple_recipe_with_same_category()
	elif select == 3:
		multiple_recipe_with_different_category()

def single_recipe():
	name = read_input("Kirjoita reseptin nimi:")
	if name == 'exit':
		return
	category = read_input("Hyvä. Kirjoitappa sitten mihin kategoriaan se kuuluu?")
	if category == 'exit':
		return
	recept = Recipe(name, category)
	save_recept_to_file(recept)
	print "Talennus onnistui!"
	print "Haluatko lisätä uuden reseptin?"
	print "Kirjoita 'K', jos haluat tehdä uuden"
	select = read_input("Muutoin palataan pääsivulle", True)
	if select == 'K': single_recipe()

def multiple_recipe_with_same_category():
	category = read_input("Mihin kategoriaan reseptit kuuluu?")
	if category == 'exit':
		return
	while True:
		name = read_input("Kirjoita reseptin nimi:", True)
		if name == 'exit':
			return
		elif name == '':
			print "tyhjä"
			return
		recept = Recipe(name, category)
		save_recept_to_file(recept)
		press_to_continue("Talennus onnistui! (pääset päävalikkoon kirjoittamalla 'exit')")

def multiple_recipe_with_different_category():
	while True:
		name = read_input("Kirjoita reseptin nimi:")
		if name == 'exit':
			return
		category = read_input("Hyvä. Kirjoitappa sitten mihin kategoriaan se kuuluu?")
		if category == 'exit':
			return
		recept = Recipe(name, category)
		save_recept_to_file(recept)
		press_to_continue("Talennus onnistui! (pääset päävalikkoon kirjoittamalla 'exit')")
