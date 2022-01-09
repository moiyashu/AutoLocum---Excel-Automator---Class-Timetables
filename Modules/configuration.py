class configuration_functions:
	def rows_and_columns():
		rows = [ # rows to check
			6, 
			7, 
			8, 
			9, 
			10
		]
		
		# will have to chgange this to numbers, stays this way for convinence for now. later numbers only and no for loop fr it
		columns_chartype_id = [ # columns to check
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

		columns = [] # creating a int type of the letters location from ^ columns_chartype_id ^
		for char in columns_chartype_id: 
			char = char.upper()
			columns.append(ord(char)-64) # converting into the int type and appeading to it
			# ord converts it to ASCII value and (caps letter - 64) is the location in english letters
		return rows, columns

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
		return _dict.keys(), _dict.values(), _dict
