# -*- coding: utf-8 -*-
import sys
from modules import *
from pages import *

options = {
		'1': create_menu.main,
		'2': show_current_menu.main,
		'3': create_recipe.main,
		'4': print_recipes.main,
		'5': delete_modify_recipe.main,
		'6': menu_log.main,
		'7': create_lot_recipes.main
		#, 'q': finished program
}
def menu():
	print "%s" %(project_name.upper())
	print "---"
	print "VALIKKO"
	print "1: Luo viikon ruokalista"
	print "2: Näytä viikon ruokalista"
	print "3: Luo resepti"
	print "4: Luettele reseptit"
	print "5: Muokkaa/Poista resepti"
	print "6: Luettele edellisten viikkojen ruokalistoja"
	print "7: Luo monia reseptejä yhden kategorian alle"
	print "q: Sulje sovellus"
	print ""
	print "Jatkaaksesi ohjelmassa kirjoita valitsemasi numero (tai sulkiessasi 'q') ja paina ENTER"

clear()
menu()
while True:
	try:
		i = read_input("Mitä haluat tehdä?")
		if i == 'q' or i =='exit':	# Close the application
			print "Suljetaan ohjelma..."
			break
		if i in options:
			clear()
			options[i]()	# Move to the page
			clear()			
			print "Takaisin valikkoon..."
			menu()
		else:
			print "Annoit tuntemattoman komennon. Yritä uudelleen"

	except KeyError:
		print "Annoit tuntemattoman komennon. Yritä uudelleen"
	except:
		print sys.exc_info()
		raise



