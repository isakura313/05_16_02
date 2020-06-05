import numpy as np #импортируем наш numpy
matrix = np.array([[1, 3, 4],
                   [2, 4, 5]])

matrix2 = np.array([[3, 4, 5],
                    [4, 5, 6]])
matrix2 = matrix2.T #транспонирование
print(matrix2)
print(f" количество элементов {matrix.size}")
print(f" форма первой матрицы {matrix.shape}")  # традиционно сначала говорится количество строк потом столбцов
print(f" пространств у первой матрицы {matrix.ndim}")  # традиционно сначала говорится количество строк потом столбцов
print(matrix[1][2])
# matrix3 = matrix * matrix2 #просто нескалярное перемножение
print(np.dot(matrix, matrix2))
