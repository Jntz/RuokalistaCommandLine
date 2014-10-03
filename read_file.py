# -*- coding: utf-8 -*-
from modules import *
from classes import *

import re

"""
Just for reading recipes quick in txt file
"""
def save_to_file(recept):
	old_data = get_recipes_data()
	old_data["recipes"].append(recept.save_data_to_file())
	write_json_to_file(old_data, filenames["recipes"])

regex = '<.*>'

f = open('ruuat.txt', 'r')

category = ""
counter = 0

for line in f:
	l = line.rstrip('\n')
	if not l: continue
	if re.search(regex, l):
		category = l.strip('<>')			
	else:
		recept = Recipe(l, category, "")
		save_to_file(recept)
		counter += 1

print "Kaikki reseptit luettiin onnistuneesti!"
print "Yhteensä %s reseptiä luotiin kategorioineen" %(counter)