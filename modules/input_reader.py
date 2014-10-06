# -*- coding: utf-8 -*-
def read_input(output = "Kirjoita jotain", empty_allowed = False):
	x = None
	if not empty_allowed:
		while not x:
			try:
				x = raw_input(output + ' ').strip()
			except Exception:
				print 'Virhe tapahtui'
	else:
		try:
			x = raw_input(output + ' ').strip()
		except Exception:
			print 'Virhe tapahtui'
	return x;

def read_int(output = "Anna kokonaisluku", empty_allowed = False):
	x = None
	if not empty_allowed:
		while x is None:
			print output
			try:
				temp_x = raw_input()
				x = int(temp_x)
			except ValueError:
				if(temp_x == 'exit'): return temp_x
				print 'Et tainnut antaa kokonaislukua? Kokonaisluku on 1,2,3,4 jne.'
	else:
		try:
			temp_x = raw_input(output + ' ')
			x = int(temp_x)
		except Exception:
			if(temp_x == 'exit'): return temp_x
			print 'Virhe tapahtui'
	return x