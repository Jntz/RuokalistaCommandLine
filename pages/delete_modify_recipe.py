# -*- coding: utf-8 -*-
from modules import *

def main():
	print "MUOKKAA TAI POISTA RESEPTI (pääset takaisin aloitusvalikkoon kirjoittamalla 'exit')"
	print ""
	recipes = get_recipes()
	if len(recipes) > 0:
		print "Reseptit:"
		i = 1
		for recipe in recipes:
			print "%s. %s [%s]" %(i, recipe["name"].encode('utf-8'), recipe["category"].encode('utf-8'))
			i += 1
		print "---"
		print ""
	else:
		print "Reseptejä ei löytynyt"
		read_input("Palaa takaisin päävalikkoon painamalla ENTER", True)
		return

	while(True):
		try:
			which_one = read_input("Valitse resepti kirjoittamalla reseptin numero ja painamalla ENTER:")
			if which_one == 'exit':
				return 
			which_one = int(which_one)
			which_one -= 1 # list starting to index 0
			if which_one < len(recipes) and which_one >= 0:
				break
			else:
				print "Valitsit numeron, jota ei ole listalla (isompi kuin lista tai alle yksi) TAI et kirjoittanut numeroa. Yritä uudelleen."
		except:
			print "Virhe tapahtui"
	recipe = recipes[which_one]

	print "Valitsit reseptin: %s [%s]" %(recipe["name"].encode('utf-8'), recipe["category"].encode('utf-8'))

	while(True):
		case = read_input("Jos haluat muokata reseptiä kirjoita '1' ja paina ENTER. Jos haluat poistaa reseptin kirjoita '2' ja paina ENTER. Jos haluat palata edelliseen valintaan kirjoita '3' ja paina ENTER:")
		if case == 'exit' or case == '1' or case == '2' or case == '3':
			break
		else:
			print "Annoit tuntemattoman käskyn, yritä uudelleen."
		
	if case == 'exit':
		return
	elif case == '1':
		modify_recipe(recipes, recipe, which_one)
	elif case == '2':
		remove_recipe(recipes, recipe, which_one)
	else: 
		clear()
		main()

def remove_recipe(recipes, recipe, index):
	old_data = {"recipes": recipes}
	if(read_input("Oletko varma? Kirjoita 'K' varmistaaksesi poiston.") == "K"):		
		old_data["recipes"].pop(index) # pop out old recipe
		write_json_to_file(old_data, filenames["recipes"])
		read_input("Resepti poistettu onnistuneesti. Jatka takaisin aloitusvalikkoon painamalla ENTER", True)
		return
	else:
		print "Et halunnut sittenkään poistaa. Palataan takaisin edelliseen valintaan.."
		main()
	
def modify_recipe(recipes, recipe, index):
	old_data = {"recipes": recipes}
	print "Haluat siis muokata reseptiä"
	print "Kenttän sisältöä ei muokata jos painat vain ENTER"
	name = read_input("Kirjoita uusi nimi:", True).capitalize()
	category = read_input("Kirjoita uusi kategoria:", True).capitalize()
	sub_categories = read_input("Kirjoita uudet alakategoriat:", True).capitalize()
	if name == "" or name == recipe["name"] and category == "" or category == recipe["category"] and sub_categories == "" or sub_categories == recipe["sub_categories"]: 
		print "Et muuttanut mitään."
		read_input("Palaa takaisin päävalikkoon painamalla ENTER", True)
		return
	if name != "":
		recipe["name"] = name
	if category != "":
		recipe["category"] = category
	if sub_categories != "":
		recipe["sub_categories"] = sub_categories 
	old_data["recipes"][index] = recipe
	write_json_to_file(old_data, filenames["recipes"])
