from Modules.configuration import configuration_functions as cf

class dictionary_functions:
	def generate_dict(file_path: str):
		import os
		_dict = {}
		_dict['all_sheets'] = []
		_dict['name'] = os.path.basename(file_path)
		return _dict
	
	def generate_nested_dicts(_dict: dict, class_name):
		
		_dict[class_name]['TUE'] = {}
		_dict[class_name]['wed'] = {}
		_dict[class_name]['thu'] = {}
		_dict[class_name]['fri'] = {}
		return True

	def pydict_to_jsondict(pydict: dict):
		import json
		return json.dumps(pydict)
	
	def write_to_json_file(_dict: dict):
		with open('./outputs/dict.json', 'w') as json_file:
			import json
			json.dump(_dict, json_file, indent=4, sort_keys=True)
		return True

	def rename_period(name: str):
		keys, values, replacements_dict = cf.get_values_to_replace()
		if name in keys:
			for key in keys:
				if name == key:
					replaced_name = replacements_dict[key]
		else:
			replaced_name = name
		return replaced_name
