# -*- coding: utf-8 -*-
from modules import *

def main():
	menus = get_menus()
	if current_week_str in menus:
		print "VIIKON MENU:"
		print "---"
		for recept in menus[current_week_str]:
			print "%s  <%s>"%(recept["name"].encode('utf-8'), recept["category"].encode('utf-8'))
		print ""
	elif len(menus) <= 0:
		print "Et ole luonut yhtään ruokalistaa vielä." 
	else:
		print "Et ole luonut tämän viikon ruokalistaa."
	press_to_continue("Paina ENTER palataksesi pääsivulle")