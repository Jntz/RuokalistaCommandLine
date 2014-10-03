# -*- coding: utf-8 -*-
from modules import *
import random

def main(): 
	how_many = read_int("Kuinka monta ruokaa tehdään tällä viikolla? (kirjoita exit jos haluat edelliseen valikkoon)")
	if how_many == "exit": return
	recipes = get_recipes()
	menu = []	
	categories = []
	previous_indexes = []

	while how_many > 0:
		while True: 
			index = random.randint(0, len(recipes) - 1)
			if index not in previous_indexes and recipes[index]["category"] not in categories:
				previous_indexes.append(index)
				break
		menu.append(recipes[index]["name"] + " <" + recipes[index]["category"] + ">")
		categories.append(recipes[index]["category"])
		how_many -= 1

	for item in menu:
		print item.encode('utf-8')
	read_input("Paina jatkamalla enter", True)