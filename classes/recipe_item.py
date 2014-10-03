# -*- coding: utf-8 -*-
class Recipe_Item:
	def __init__(self, amount, name):
		self.amount = amount
		self.name = name.capitalize()

	# Set/modify methods
	def rename(self, name):
		self.name = name.capitalize()
	def change_amount(self, amount):
		self.amount = amount

	# Get methods
	def to_string(self):
		return "%s %s" %(self.amount, self.name)

	def save_data_to_file(self):
		return {'recipe_item': {'name': self.name, 'amount': self.amount}}

