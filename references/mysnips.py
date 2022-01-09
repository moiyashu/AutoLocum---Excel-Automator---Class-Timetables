excel_dict = {}
try:
	pass
except Exception as e:
	excel_dict['status'] = {}
	excel_dict['status']['code'] = 0
	excel_dict['status']['expt'] = str(e)