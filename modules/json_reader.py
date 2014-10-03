# -*- coding: utf-8 -*-
import json, io

def read_json_from_file(filename):
	with open(filename, 'r') as f:
		read_data = f.read()
	f.closed
	try:
		json_data = json.loads(read_data)
	except:
		json_data = None

	return json_data