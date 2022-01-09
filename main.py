from Modules.functions import other_functions as other_funcs
from Modules.dictionary import dictionary_functions as dict_funcs
from Modules.configuration import configuration_functions as config_funcs

class excel_to_dict():
	"""
	Python program to read the NPS format of excel files
	Parameters :: file: base64 (file bytes)
	NOTE: please use excel 2010 or later
	"""
	def __init__(self, file_bytes):
		self.file_bytes = file_bytes

	def main(self):
		"""
		The main file that a user accesses
		Parameters: None
		"""
		file_bytes_decoded = other_funcs.base64_file_decode(self.file_bytes) 
		excel_file = other_funcs.base64_write(file_bytes_decoded)

		sheet_names=[]
		sheet_titles=[]
		excel_dict = dict_funcs.generate_dict(excel_file)

		# package is called and workbook object is created
		load_workbook = other_funcs.get_openpyxl()
		wb = load_workbook(excel_file)
		for sheet in wb.sheetnames:
			sheet_now = wb[sheet]
			sheet_names.append(sheet_now.title)
			sheet_titles.append(sheet_now.cell(row = 1, column = 1).value)

			row_ids, column_ids = config_funcs.rows_and_columns()

			class_name = other_funcs.get_class(sheet_now.cell(row = 1, column = 1).value)


			# weekdays = ['mon', 'tue', 'wed', 'thu', 'fri']
			excel_dict[class_name] = {}
			for row_id in row_ids:
				day = (sheet_now.cell(row = row_id, column = 1).value).upper()
				excel_dict[class_name][day] = {}
				for period_index, col_id in enumerate(column_ids, start=1):
						excel_dict[class_name][day][period_index] = dict_funcs.rename_period(
							(
								sheet_now.cell(row = row_id, column = col_id).value
							).replace(' ', '')
						)
						
			excel_dict['all_sheets'] = sheet_names
			
			json_write_file_status = dict_funcs.write_to_json_file(excel_dict)
			print("json file write success=" + str(json_write_file_status))

		deletion_status_0 = other_funcs.erase_file(excel_file)
		print('Deletion success=' + str(deletion_status_0))
		print('Completion='+str(True))
		return excel_dict

# test 
if __name__ == '__main__':
	# accessing sample
	file_name = '9E.xlsx'
	copy_of_input_file = './inputs/'+file_name
	from shutil import copyfile
	copyfile('./test_files/'+file_name, copy_of_input_file)
	# bytes
	bytes_str = other_funcs.base64_file_encode(copy_of_input_file)
	# core test
	excel_dict = excel_to_dict(bytes_str).main()
