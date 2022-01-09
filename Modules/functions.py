class other_functions:
	def get_openpyxl():
		try:
			from openpyxl import load_workbook
		except:
			from os import system
			system("pip install openpyxl")
			from openpyxl import load_workbook
		return load_workbook

	def base64_file_encode(file_path: str):
		from base64 import b64encode
		with open(file_path, "rb") as file:
			bytes_str = b64encode(file.read())
		return bytes_str

	def base64_file_decode(base64_bytes: str):
		from base64 import b64decode
		decrypted = b64decode(base64_bytes)
		return decrypted

	def base64_write(decoded_bytes: str):
		import datetime
		now = datetime.datetime.now()
		filename = ("%2i%2i%2i%4i" % (now.hour, now.minute, now.second, now.year)).replace(' ', '0')
		path = './outputs/{0}.xlsx'.format(filename)
		with open(path, 'wb') as excel_file:
			excel_file.write(decoded_bytes)
		return path.replace('..', '.')

	def erase_file(file_path: str):
		import os
		try:
			os.remove(file_path)
			return True
		except:
			return False

	def get_class(title):
		class_name0 = title.upper().replace(' ', '').replace('TIMETABLEFORCLASS', '')
		try: 
			int(class_name0[:2])
			class_name = class_name0[:3]
		except:
			class_name = class_name0[:2]
		return class_name
