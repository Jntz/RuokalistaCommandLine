# -*- coding: utf-8 -*-
from recipe_item import *

class Recipe:
	""" Init
		params: 
			name <string> (required)
			category <string>(required)  
	"""
	def __init__(self, name, category):
		self.name = name.capitalize()	
		self.category = category.capitalize()
	 
	def to_string(self):
		return "name: %s category: %s" %(self.name, self.category)

	""" Return data to project json writer
		return:
			dictionary
	""" 
	def save_data_to_file(self):
		return {'name': self.name, 'category': self.category}
