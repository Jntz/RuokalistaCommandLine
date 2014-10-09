# -*- coding: utf-8 -*-
from modules import *
from classes import *

menus = get_menus()
recipes = get_recipes()
new_data = {"recipes": recipes, "menus": menus }

write_json_to_file(new_data, "data.json")
print "Siirto onnistui"