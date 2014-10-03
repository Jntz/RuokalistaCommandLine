# -*- coding: utf-8 -*-
from modules import *

def main():
	clear()
	recipes = get_recipes()
	print "RESEPTIT"
	while True:
		switch = read_input("Kirjoita '1' jos haluat nähdä listan julkaisun mukaan. Kirjoita '2' niin reseptit listataan kategorian mukaan. Kirjoittamalla 'exit' poistuu päävalikkoon.")
		if switch == '1' or switch == '2' or switch == 'exit':
			break
		else:
			print "Väärä komento. Yritä uudelleen"
	if switch == 'exit': return
	elif switch == '1':
		if len(recipes) > 0:
			list_sort_by_created(recipes)
		else:
			print "Yhtään reseptiä ei löytynyt"
	elif switch == '2':
		if len(recipes) > 0:
			list_sort_by_category(recipes)
		else:
			print "Yhtään reseptiä ei löytynyt"
	read_input("Palaa takaisin valikkoon painamalla ENTER", True)	

def list_sort_by_created(recipes): 
	print "Luetellaan luomisjärjestyksessä"
	i = 1
	for recipe in recipes:
		print "%s. %s [%s]" %(i, recipe["name"].encode('utf-8'), recipe["category"].encode('utf-8'))
		i += 1
	print ""
def list_sort_by_category(recipes):
	sortedRecipes = {}
	for recipe in recipes:
		if recipe["category"] not in sortedRecipes:
			sortedRecipes[recipe["category"]] = []
		sortedRecipes[recipe["category"]].append(recipe)

	for category in sorted(sortedRecipes):
		i = 1
		print "---%s---" %(category.encode('utf-8'))
		for recipe in sortedRecipes[category]:
			print "%s. %s" %(i, recipe["name"].encode('utf-8'))
			i += 1
	print ""