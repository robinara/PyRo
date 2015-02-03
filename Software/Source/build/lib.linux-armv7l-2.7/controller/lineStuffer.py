def write_line(self,data):
	stuffing=" "	
	for i in range(0,20-len(data)):
		data+=stuffing
	return data
