# -*- coding: utf-8 -*-
from modules import *
from classes import *

import re

"""
Just for reading recipes quick in txt file
Syntax in your recipe file:
<Category>
Recipename1
Recipename2
<Category2>
Recipemane3
...

Example:
<Fish>
Fish and Chips
Fish soup
<Pork>
Pulled pork
...
"""

regex_for_category = '<.*>'
category = ""
counter = 0

try:
	filename = read_input("Anna tiedostonimi päätteineen. Jos tiedosto ei sijaitse samassa kansiossa, absoluuttinen polku. Esim: ruuat.txt")
	f = open(filename, 'r')
except:
	print "Tiedostoa ei löydy tai jokin muu meni vikaan"
	raise

for line in f:
	l = line.rstrip('\n')
	if not l: continue
	if re.search(regex_for_category, l):
		category = l.strip('<>')			
	else:
		recept = Recipe(l, category)
		save_to_file(recept)
		counter += 1

print "Kaikki reseptit luettiin onnistuneesti!"
print "Yhteensä %s reseptiä luotiin kategorioineen" %(counter)