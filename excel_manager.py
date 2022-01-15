from os.path import basename

from Modules.functions import other_functions as other_funcs
from Modules.dictionary import dictionary_functions as dict_funcs
from Modules.configuration import configuration_functions as config_funcs

class xldict():
	"""
	Python program to read the NPS format of excel files
	Parameters :: file: base64 (file bytes)
	NOTE: please use excel 2010 or later
	"""
	def __init__(self, file_bytes):
		self.file_bytes = file_bytes

	def class_timetable(self):
		"""
		The class timetable preset
		Parameters: None
		"""
		try:
			file_bytes_decoded = other_funcs.base64_file_decode(self.file_bytes) 
			excel_file = other_funcs.base64_write(file_bytes_decoded)
	
			excel_dict = {'sheets_names' : [], 'name' : basename(excel_file), 'status' : True, 'exception' : 'None'}
	
			# package is called and workbook object is created
			load_workbook = other_funcs.get_openpyxl()
			wb = load_workbook(excel_file)
			for sheet in wb.sheetnames:
				sheet_now = wb[sheet]
				excel_dict['sheets_names'].append(sheet_now.title)
	
				cl_tt_rows_n_cols_dict = config_funcs.class_timetables_rows_n_cols()
				row_ids = cl_tt_rows_n_cols_dict["rows_int"]
				col_ids = cl_tt_rows_n_cols_dict["cols_int"]
	
				try:
					table_reposition_stat = other_funcs.postion_table(sheet_now)
					print("TABLE REPOSITIONING STATUS : " + str(table_reposition_stat))
				except Exception as e:
					f_exception = "TABLE REPOSITIONING STATUS : " + str(False) + " [FATAL FAIL]" + "\n" + str(e)
					print(f_exception)
					excel_dict = {'status' : False, 'exception' : f_exception}
	
				class_name = other_funcs.get_class(sheet_now.cell(row = 1, column = 1).value)
	
				excel_dict[class_name] = {}
				for row_id in row_ids:
					day = (sheet_now.cell(row = row_id, column = 1).value).upper()
					excel_dict[class_name][day] = {}
					for period_index, col_id in enumerate(col_ids, start=1):
							excel_dict[class_name][day][period_index] = dict_funcs.rename_period(
								(
									sheet_now.cell(row = row_id, column = col_id).value
								).replace(' ', '')
							)
			try:
				deletion_status_0 = other_funcs.erase_file(excel_file)
				print("TEMPORARY EXCEL WORKBOOK DELETION : " + str(deletion_status_0))
			except Exception as e:
				f_exception = "TEMPORARY EXCEL WORKBOOK DELETION : " + str(False) + " [FATAL FAIL]" + "\n" + str(e)
				print(f_exception)
				excel_dict = {'status' : False, "exception" : f_exception}
		except Exception as e:
			excel_dict = {'status' : False, "exception" : str(e)}
		try:
			json_write_file_status = dict_funcs.write_to_json_file(excel_dict)
			print("JSON FILE WRITE : " + str(json_write_file_status))
		except Exception as e:
			f_exception = "JSON FILE WRITE : " + str(False) + " [FATAL FAIL]" + "\n" + str(e)
			print(f_exception)
			excel_dict = {'status' : False, "exception" : f_exception}
		return excel_dict

# test 
if __name__ == '__main__':
	# accessing sample
	file_name = '9E - Cell Rearrangement Test.xlsx'
	copy_of_input_file = './inputs/class_timetables/'+file_name
	from shutil import copyfile
	copyfile('./test_files/class_timetables/'+file_name, copy_of_input_file)

	# bytes
	bytes_str = other_funcs.base64_file_encode(copy_of_input_file)

	# core test
	excel_dict = xldict(bytes_str).class_timetable()
