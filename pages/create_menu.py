# -*- coding: utf-8 -*-
from modules import *
import random, datetime

def main(): 
	recipes = get_recipes()
	max_recipes = len(recipes)
	how_many = read_int("Kuinka monta ruokaa tehdään tällä viikolla? (kirjoita exit jos haluat edelliseen valikkoon)")
	if how_many == "exit": return

	if how_many <= 0: 
		read_int("Valitsit 0 tai vähemmän ruokaa, et siis halua tehdä ruoka listaa. Palaa päävalikkoon painamalla ENTER", True)
		return
	menu = []	
	categories = []
	previous_indexes = []
	current_week = datetime.date.today().isocalendar()[1]

	if len(recipes) <= 0:
		read_int("Reseptejä ei ole, mahdoton tehdä ruokalistaa. Palaa päävalikkoon painamalla ENTER", True)
		return
	elif len(recipes) < how_many:
		print("Haluat tehdä ruokia enemmän kuin ruokalistalla on vaihtoehtoja (emme arvo liian usein samaa ruokaa). Ei onnistu.")
		main()
		return

	while how_many > 0:
		while True: 
			index = random.randint(0, len(recipes) - 1)
			if index not in previous_indexes and recipes[index]["category"] not in categories:
				previous_indexes.append(index)
				break
		menu.append({"name": recipes[index]["name"], "category": recipes[index]["category"]})
		categories.append(recipes[index]["category"])
		how_many -= 1

	for item in menu:
		print item["name"].encode('utf-8'), " ", item["category"].encode('utf-8')

	save_menu_to_file(menu)

	read_input("Paina jatkamalla ENTER", True)