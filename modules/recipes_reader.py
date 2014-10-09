# -*- coding: utf-8 -*-
from json_reader import *
from config import *
from helpers import *

def get_recipes_data():
	old_data = read_json_from_file("data.json")
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

def get_recipe(index): # get recipe with spesific index
	return get_recipes()[index]

def get_recipes_for_menu(menus): # get recipe that allowed add to menu
	not_allowed = []
	i = 1
	while i <= reuse_weeks: # default reuse_weeks: 4
		week = current_week - i # example: 51 - 1, 51 - 2, 51 - 3, 51 - 4
		if week <= 0: # week number 0 is not allowed => 2, 1, 52, 51,...
			week = 52
		week = str(week)
		if week not in menus: break

		for recipe in menus[week]:
			not_allowed.append(recipe["name"])
		i += 1
	
	all_recipes = get_recipes() # get all recipes
	i = 0
	while i < len(all_recipes):
		if all_recipes[i]["name"] in not_allowed:
			not_allowed.pop(not_allowed.index(all_recipes[i]["name"]))
			item = all_recipes.pop(i)
			if len(not_allowed) <= 0: break # not_allowed list is empty => no need to remove any recepts
		else:
			i += 1

	return all_recipes

def get_recipe_category_count():
	recipes = get_recipes()
	categories = []

	for recipe in recipes:
		if recipe["category"] not in categories:
			categories.append(recipe["category"])

	return len(categories)