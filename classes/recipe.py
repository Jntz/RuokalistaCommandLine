# -*- coding: utf-8 -*-
from recipe_item import *

class Recipe:
	""" Init
		params: 
			category <string>(required)  
			sub_categories <string>
	"""
	def __init__(self, name, category, sub_category = ""):
		self.name = name.capitalize()	
		self.category = category.capitalize()
		self.sub_categories = sub_category.capitalize() #string (not nesseccary) 
		self.items = []
	
	# Add and modifications methods
	""" Add item to Recipe
		params:
			item <Recipe_Item> (required)
	"""
	def add_item(self, item):
		self.items.append(item)

	""" Add item to Recipe in spesific index
		params:
			index <integer> (required)
			item <Recipe_Item> (required)
	"""
	def insert_item(self, index, item):
		self.items.insert(index, item)

	""" Replace (override) item to Recipe in spesific index
		params:
			index <integer> (required)
			item <Recipe_Item> (required)
	"""
	def replace_item(self, index, item):
		self.items[index] = item;

	# Get methods
	""" Print Recipe items
	"""
	def print_recipe_items(self):
		for item in self.items:
			print item.to_string()
	""" Get Recipe_Item list
		return:
			list <list:string>
	"""
	def get_recipe(self):
		l = ""
		for item in self.items:
			l.append(item.to_string())
		return l
	""" Print to Recipe
	""" 
	def to_string(self):
		return "name: %s category: %s sub-categories: %s items: %s" %(self.name, self.category, self.sub_categories, self.get_recipe())

	""" Return data to project json writer
		return:
			dictionary
	""" 

	def save_data_to_file(self):
		#d = []
		#for item in self.items:
			#d.append(item.save_data_to_file())
		return {'name': self.name, 'category': self.category, 'sub_categories': self.sub_categories} # 'recipe_items' : d}}
