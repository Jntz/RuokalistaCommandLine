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
		while not x:
			print output
			try:
				x = int(raw_input())
			except ValueError:
				if(x == 'exit'): return x 
				print 'Et tainnut antaa kokonaislukua? Kokonaisluku on 1,2,3,4 jne.'
	else:
		try:
			x = int(raw_input())
		except Exception:
			if(x == 'exit'): return x 
			print 'Virhe tapahtui'
	return x