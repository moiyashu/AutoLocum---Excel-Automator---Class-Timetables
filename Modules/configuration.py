class configuration_functions:
	def class_timetables_rows_n_cols():
		_dict = {
			"rows_int" : [ # rows to check
				6, 
				7, 
				8, 
				9, 
				10
			], "cols_char" : [ # columns to check
				# 'B', - "Cl. Teacher" (period)
				'C', 
				'D', 
				'F', 
				'G', 
				'I', 
				'J',
				'L', 
				'M'
			]
		}

		l = []
		for c in _dict["cols_char"]:
			l.append(ord(c.upper())-64) # converting into the int type and appeading to it
			# ord converts it to ASCII value and (capital letter - 64) is the location in english letters
			# this is to be subtracted by 96 instead of 64 for get the location when in lowercase letters
		_dict["cols_int"] = l
	
		return _dict

	def get_values_to_replace():
		_dict = {			
			# Languages
			'ENG' : 'ENGLISH',
			'HIN(II)' : 'HINDI',
			# Math
			'MATH' : 'MATHEMATICS',
			# Main Sciences
			'PHY' : 'PHYSICS',
			'BIO' : 'BIOLOGY',
			'CHEM' : 'CHEMISTRY',
			# Scocial Sciences
			'H&C' : 'HISTORY-CIVICS',
			'GEO&E' : 'GEOGRAPHY-ECONOMICS',
			# Computers
			'CSC' : 'COMPUTER-SCIENCE',
			# Other Periods
			'ASSEMBLY' : 'CLASS-ASSEMBLY',
			'PE/YOGA' : 'PE-YOGA',
			'LIB/LS' : 'LIBRARY-LIFESKILLS'
		}
		return _dict
