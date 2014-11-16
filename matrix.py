class Matrix():
	def __init__(self, initial_array):
		self.width = len(initial_array)
		self.height = len(initial_array[0])
		self.columns = []
		for column in initial_array:
			self.columns.append(column)
		
		self.rows = []
		for i in range(len(columns[0])):
			row = []
			for j in range(len(columns)):
				row.append(columns[i][j])
			self.rows.append(row)
				
	def print_columns(self):
		print(self.columns)
		
	def transpose(self):
		new_columns = []
		for i in range(len(self.columns)):
			row = []
			for column in self.columns:
				row.append(column[i])
			new_columns.append(row)
		return Matrix(new_columns)
		
	def multiply(self, other):
		self_height = len(self.columns[0])
		self_width = len(self.columns)
		other_height = len(other.columns[0])
		other_width = len(other.columns)
		new_height = self_height
		new_width = other_width
		if self_width is not self_height:
			return null
		new_columns = []
		
		for 
	

		
my_array = [[1,2,3],[1,2,3],[2,3,4]]
my_matrix = Matrix(my_array)
new = my_matrix.transpose()

new.print_columns()
	