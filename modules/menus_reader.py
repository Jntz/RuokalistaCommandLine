# -*- coding: utf-8 -*-
from json_reader import *
from config import *

def get_menus_data():
	old_data = read_json_from_file(filenames["menus"])
	if old_data == None or type(old_data) is not dict: # rewrite old_data and create new recipe dictionary
		# initialize new dict
		old_data = {}
		old_data["menus"] = {}
	elif "menus" not in old_data and type(old_data) is dict: # save other data (maybe worthless)
		# add new row: recipes
		old_data["menus"] = {}
	return old_data
def get_menus(): 
	data = get_menus_data()
	return data["menus"]

def get_menu(index): #get recipe with spesific index
	return get_menus()[index]

def is_week_menu_created(week):
	return week in get_menus()	# True/False