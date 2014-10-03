# -*- coding: utf-8 -*-
import io, json, recipes_reader
from recipes_reader import *

def save_to_file(recept):
	old_data = get_recipes_data()
	old_data["recipes"].append(recept.save_data_to_file())
	write_json_to_file(old_data, filenames["recipes"])

def write_json_to_file(json_content, filename):
	with io.open(filename, 'w', encoding="utf-8") as f:
		f.write(unicode(json.dumps(json_content)))
	f.closed