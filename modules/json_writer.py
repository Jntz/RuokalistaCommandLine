# -*- coding: utf-8 -*-
import io, json

def write_json_to_file(json_content, filename):
	with io.open(filename, 'w', encoding="utf-8") as f:
		f.write(unicode(json.dumps(json_content)))
	f.closed