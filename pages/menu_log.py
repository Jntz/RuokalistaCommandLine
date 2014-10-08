# -*- coding: utf-8 -*-
from modules import *

def main():
	while True: 
		print "Haluatko menut vanhemmista uusimpaan vai toisinpäin? Kirjoita 1 jos haluat vanhimmasta uusimpaan ja kirjoita 2 jos haluat uusimmasta vanhempaan."
		value = read_int("(kirjoittamalla 'exit' poistut päävalikkoon)")
		if value == "exit" or value == 1 or value == 2: break
		else: print "Kelpaamaton syöte. Yritä uudelleen"
	if value == "exit": return
	elif value == 1:
		print "MENULISTA:"
		menus = get_menus()
		week = min(menus.keys()) # find out smallest week number
		week = int(week)
		week -= 1
		for i in range(len(menus)):
			week += 1
			if week > 52: week = 1
			week_str = str(week)

			if week_str in menus: print_menu(week_str, menus[week_str])
			else: break	
	elif value == 2:
		print "MENULISTA:"
		menus = get_menus()
		for i in range(len(menus)):
			week = current_week - i
			if week <= 0: week = 52
			week = str(week)

			if week in menus: print_menu(week, menus[week])
			else: break

	else: print "Odottamaton virhe tapahtui."
	press_to_continue("Paina ENTER jatkaaksesi pääsivulle.")

def print_menu(week, menu):
	recipes_str = ""
	recipes = []
	for recipe in menu:
		recipes.append(recipe["name"])
	recipes_str = ', '.join(recipes)
	print "Viikko %s: %s"%(week, recipes_str)