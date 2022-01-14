from Modules.configuration import configuration_functions as cf

class dictionary_functions:
	def rename_period(name: str):
		replacements_dict = cf.get_values_to_replace()
		keys = replacements_dict.keys()
		if name in keys:
			for key in keys:
				if name == key:
					replaced_name = replacements_dict[key]
		else:
			replaced_name = name
		return replaced_name

	def write_to_json_file(_dict: dict):
		with open('./outputs/dict.json', 'w') as json_file:
			import json
			json.dump(_dict, json_file, indent=4, sort_keys=True)
		return True
