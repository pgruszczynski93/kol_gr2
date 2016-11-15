#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be named "kol_gr2"! 
#
#Delete these comments before commit!
#Good luck.

from Matrix import *

def main():
	print("Macierz 1: ")
	matrix_1 = Matrix(4,5,6,1,2,3,7,8,9)
	matrix_1.show()
	print("Wyswietlam Macierz 1 \"printem\"")
	print(matrix_1)
	matrix_2 = Matrix(1,2,3,4,5,6,7,8,9)
	print("Wyswietlam Macierz 2 \"printem\"")
	print(matrix_2)
	print("Dodaje M1 do M2")
	matrix_3 = matrix_2.add(matrix_1)
	matrix_3.show()
	print("Dodaje operatorem M3 do M1")
	matrix_4 = matrix_3 + matrix_1
	matrix_4.show()
	print("Mnoze operatorem M4*2")
	matrix_4 =  matrix_4 * 2;
	matrix_4.show()
	print("Mnoze operatorem 2*M4")
	matrix_4 = matrix_4 * 0.5 # przywrocenie poprzedniego stanu macierzy4
	matrix_4 =  matrix_4 * 2;
	matrix_4.show()
	print("Sprawdzam rownosc macierzy Czy macierze sa rowne: %d?"%(Matrix.the_same(matrix_4,matrix_1)))
	print("Mnoze operatorem *=2")
	matrix_4 *= 2
	matrix_4.show()
	print("Mnoze macierz przez macierz")
	matrix_5 = matrix_1.mult_matrixes(matrix_2)
	matrix_5.show()
	print("Transpozycja M1")
	mat_1 = matrix_1.transpose_matrix()
	mat_1.show()
	print("Przyklad transpozycji M1 z YIELD - 1 rzad")
	transpose_row = matrix_1.transpose_matrix_yield()
	print(transpose_row.next())
	print("Cala macierz transponowana M2")
	# for i in range(3):
	transposed_matrix = matrix_2.transpose_matrix_yield()
	for i in range(3):
		print(transposed_matrix.next())

	print("Zwracanie macierzy jako kolejnych wektorow")
	mat_vec = matrix_2.matrix_to_vector()
	print("Pierwszy rzad M2 jako wektor")
	print(mat_vec.next())
	print("Pozostale dwa rzedy M2 - dwa kolejne wektory")
	for i in range(2):
		print(mat_vec.next())

if __name__ == "__main__":
	main()
