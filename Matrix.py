import math

class Matrix(object):

	def __init__(self, *matrix_elems):
		j = 0
		self.matrix = []
		for val in matrix_elems: 
			self.matrix.append(val)


	@staticmethod
	def the_same(matrix_a,matrix_b):
		return matrix_a==matrix_b

	def show(self):
		j = 1
		elem = self.matrix
		new_line = math.sqrt(len(elem))

		for i in elem:
			print("%d"%(i)),
			if j% new_line == 0: print
			j+=1
		print 

	def add(self, tmp_matrix):
		new_matrix = Matrix()
		a = self.matrix
		b = tmp_matrix.matrix

		if(len(a) == len(b)):
			for i in range(len(a)):
				new_matrix.matrix.append((a[i] + b[i]))

		return new_matrix

	def mult_matrixes(self, tmp_matrix):
		new_matrix = Matrix()
		a = self.matrix
		b = tmp_matrix.matrix
		sum_el = 0
		dim = (int)(math.sqrt(len(a)))
		for i in range(dim):
			for j in range(dim):
				row = a[i*dim:i*dim+dim]
				col = b[:]
				for k in range(dim):
					sum_el += row[k] * col[k*dim+j]
				new_matrix.matrix.append(sum_el)
				sum_el = 0

		return new_matrix 

	def transpose_matrix(self,val = -1):
		a = self.matrix
		dim = (int)(math.sqrt(len(a)))
		copy = Matrix()
		for i in range(dim):
			for j in range(dim):
				copy.matrix.append(a[j*dim+i])
		return copy

	def transpose_matrix_yield(self,val = -1):
		a = self.matrix
		dim = (int)(math.sqrt(len(a)))
		# row = []
		for i in range(dim):
			row = []
			for j in range(dim):
				row.append(a[j*dim+i])
			yield row

	def matrix_to_vector(self):
		j = 1
		vector = []
		dim = math.sqrt(len(self.matrix))
		for elem in self.matrix:
			vector.append(elem)
			if j%dim==0:
				yield vector
				vector = []
			j += 1

	def __add__(self, tmp_matrix):
		return self.add(tmp_matrix);

	def __iadd__(self, tmp_matrix):
		return self.add(tmp_matrix);

	def __mul__(self, val):
		self.matrix[:] = [x*val for x in self.matrix]
		return self 

	def __rmul__(self, val):
		self.matrix[:] = [x*val for x in self.matrix]
		return self 

	def __imul__(self, val):
		self.matrix[:] = [x*val for x in self.matrix]
		return self 

	def __eq__(self, tmp_matrix):
		return set(self.matrix) == set(tmp_matrix.matrix)

	def __str__(self):
		return str(self.matrix)+"\n"
