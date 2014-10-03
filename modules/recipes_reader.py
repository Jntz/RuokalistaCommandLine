# -*- coding: utf-8 -*-
from json_reader import *
from config import *

def get_recipes_data():
	old_data = read_json_from_file(filenames["recipes"])
	if old_data == None or type(old_data) is not dict: # rewrite old_data and create new recipe dictionary
		# initialize new dict
		old_data = {}
		old_data["recipes"] = []
	elif "recipes" not in old_data and type(old_data) is dict: # save other data (maybe worthless)
		# add new row: recipes
		old_data["recipes"] = []
	return old_data
def get_recipes(): 
	data = get_recipes_data()
	return data["recipes"]

def get_recipe(index): #get recipe with spesific index
	return get_recipes()[index]