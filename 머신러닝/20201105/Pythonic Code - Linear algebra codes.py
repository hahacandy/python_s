u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [sum(t) for t in zip(u,v,z)]
print(result)

u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2
result = [alpha*sum(t) for t in zip(u, v)]
print(result)

matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)


#Matrix Transpose
matrix_a = [[1,2,3], [4,5,6]]
result = [[element for element in t] for t in zip (*matrix_a)]
print(result)

# Matrix Product
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)




#겁나 어렵다, 그래도 대애충은 이해함
row_a = [1, 2, 3]
column_b = [4, 5, 6]
column_c = [7, 8, 9]
[print(str(a) + ":" + str(b)) for a, b, c in zip(row_a, column_b, column_c)]
[print(str(a)) for a in zip(row_a, column_b)]