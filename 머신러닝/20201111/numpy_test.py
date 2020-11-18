import numpy as np

test_array = np.array([1, 4, 5, 8], float)
# print(test_array)
# print(type(test_array[3]))

# test_array =  np.array([1,4,5,8], dtype=float16) 이런건 주피터나, 구글코랩에서만 가능한듯, 아니면 아나콘다 풀버전
# test_array =  np.array([1,4,5,8], dtype=float)
# print(type(test_array[3]))


# 가로 세로 크기를 나타냄 shape
test_array = np.array([1, 4, 5, 8], float)
test_array2 = np.array([[1, 4, 5, 8], [1, 2, 3, 4]], float)
test_array3 = np.array([[[1, 4, 5, 8], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]]], float)


# print(test_array.shape)
# print(test_array2.shape)

# []의 크기
# print(test_array.ndim)
# print(test_array2.ndim)
# print(test_array3.ndim)

# 전체 data의 개수
# print(test_array.size)
# print(test_array2.size)
# print(test_array3.size)

# 매트릭스를 가로 세로 크기를 바꿈
# print(test_array2.reshape(2,2,2))

# -1을 넣으면 몇개인줄은 모르나 다른값에 의해 그것이 결정됨
# print(test_array2.reshape(-1, 1))

# flatten 다차원 array를 1차원 array 로 표현
# print(test_array3.flatten())


# indexing
a = np.array([[1,2,3], [4.5,5,6]], int)
print(a)
print(a[0,0])
print(a[0][0])
a[0,0] = 12
print(a)
a[0][0] = 5
print(a)

# slicing
# a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], int)
# print(a[:,2:])
# print(a[1,1:3])
# print(a[1:3])


# arange
# print(np.arange(30))
# print(np.arange(0, 5, 0.5)) #시작 끝 스탭
# print(np.arange(30).reshape(5,6))

# 0으로 가득찬 ndarray 생성
# print(np.zeros(shape=(10,), dtype=np.int8))
# print(np.zeros((2,5)))

# 1로 가득찬 생성
# print(np.ones(shape=10, dtype=np.int8))
# print(np.ones((2,5)))

# empty 로 생성, 메모리의 주소값인가 여튼 저건 갈비지값
# print(np.empty(shape=(10,), dtype=np.int8))
# print(np.empty((3,5)))

# something_like
# test_matrix = np.arange(30).reshape(5,6)
# print(test_matrix)
# print()
# print(np.ones_like(test_matrix))

# identity 단위행렬을 생성
# print(np.identity(n=3, dtype=np.int8))
# print()
# print(np.identity(5))

# eye
# print(np.eye(4))
# print(np.eye(N=3, M=6, dtype=np.int8))
# print(np.eye(3,5, k=2)) #k=start index


# #diag 대각행렬의 값을 추출함
# matrix = np.arange(9).reshape(3,3)
# print(matrix)
# print()
# print(np.diag(matrix))
# print()
# print(np.diag(matrix, k=1))

# random sampling 데이터 분포에 따른 sampling 으로 array를 생성
# print(np.random.uniform(0, 1, 10).reshape(2, 5)) # 균등분포
# print()
# print(np.random.normal(0, 1, 10).reshape(2, 5)) # 정규분포

# #sum
# test_array = np.arange(1,11)
# print(test_array)
# print(test_array.su m(dtype=np.float))

# axix 모든 operation function 을 실행할떄, 기준이 되는 dimension 축(머라노)
# 여튼 한 row값을 전체 값을 더한다거나, 한 컬럼의 전체 값을 더하는것인듯
# test_array = np.arange(1,13).reshape(3,4)
# print(test_array)
# print()
# print(test_array.sum(axis=1)) # 한 row의 전체 덧셈
# print()
# print(test_array.sum(axis=0)) # 한 컬럼의 전체 덧셈
# print()
# print(test_array.mean()) # 전체 데이터들의 평균값
# print(test_array.mean(axis=0)) # 한 컬럼 별로 평균값들
# print()
# print(test_array.std()) #표준편차라
# print(test_array.std(axis=0))

# concatenate
# Numpy array를 합치는 함수
# a = np.array([1, 2, 3])
# b = np.array([2, 3, 4])
# print(np.vstack((a,b))) # row 와 row를 붙임
# print()
# a = np.array([[1], [2], [3]])
# b = np.array([[2], [3], [4]])
# print(np.hstack((a, b))) # 컬럼과 컬럼을 붙임

# concatenate2
# a = np.array([[1, 2, 3]])
# b = np.array([[2, 3, 4]])
# print(np.concatenate((a, b), axis=0)) # row 와 row를 붙임
# print()
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# print(np.concatenate((a, b.T), axis=1)) # 컬럼과 컬럼을 붙임 .T가 필요한듯 자세히는 모름


# operations b/t arrays
# Numpy는 array간의 기본적인 사칙연산을 지원함
# test_a = np.array([[1,2,3], [4,5,6]], float)
# print(test_a + test_a)
# print(test_a - test_a)
# print(test_a * test_a) # 같은 위치의 수끼리 곱셈함
# print()
# test_a = np.arange(1,7).reshape(2,3)
# test_b = np.arange(7,13).reshape(3,2)
# print(test_a)
# print(test_b)
# print(test_a.dot(test_b)) # 이게 진짜 행렬 곱셈

# broadcasting
# Shape이 다른 배열 간 연산을 지원하는 기능 + - * / **(제곱) 가능
# test_matrix = np.array([[1,2,3], [4,5,6]], float)
# scalar = 3
# print(test_matrix + scalar)

# test_matrix = np.array([[0,0,0], [10,10,10], [20,20,20], [30,30,30]])
# print(test_matrix)
# print()
# test_matrix2 = np.array([1,2,3])
# print(test_matrix2)
# print()
# print(test_matrix + test_matrix2) # test_matrix2 의 1row값 전체가 test_matrix에 순서대로 더해지는것을 볼수잇음


# # Numpy performance #1
# def sclar_vector_product(_scalar, _vector):
#     result = []
#     for value in vector:
#         result.append(_scalar * value)
#     return result
#
# iternation_max = 10
#
# vector = list(range(iternation_max))
# scalar = 2
#
# import timeit
# #for loop 를 이용한 성능
# t1 = timeit.Timer("sclar_vector_product(scalar, vector)", globals=globals())
# #for loop 를 이용한 성능
# t2 = timeit.Timer("[scalar * value for value in range(iternation_max)]", globals=globals())
# # # numpy를 이용한 성능
# t3 = timeit.Timer("np.arange(iternation_max)*scalar", globals=globals())
#
# print(t1.timeit())
# print(t2.timeit())
# print(t3.timeit())
# #numpy가 c언어로 만들어진거라 더 빨라야하는데 이상함
#
# #넘파이는 계산은 괜찮지만, 매트릭스나 백터끼리 붙이는건 비추한다고함, 그 이유는 메모리공간 확보떄문이라고 함
# # 이떄는 일반 파이썬이 낫다는데, 이유는 파이썬은 그냥 빈메모리공간에 값을 바로 집어넣기 떄문이라고함



##comparisons
# # all & any
# a = np.arange(10)
# print(a)
# print(a > 5)
# print(np.any(a>5), np.any(a<0)) # 하나라도 만족하면 true 그렇지 않으면 false
# print(np.all(a>5), np.any(a<10)) # 모두 만족하면 true, 그렇지않으면 false


# logical
# a = np.array([1, 3, 0], float)
# print(np.logical_and(a>0, a<3)) #and조건
#
# b = np.array([True, False, True], bool)
# print(np.logical_not(b)) # 반대로 된다고 생각하면될듯
#
# c = np.array([False, True, False], bool)
# print(np.logical_or(b, c)) # or조건


# #where
# a = np.array([1, 3, 0], float)
# print(np.where(a>0, 3, 2)) # a>0 true이면 3을 false면 2를 출력
# print(np.where(a)) #true 의 인덱스값을 가져옴


# #argmax & argmin
# # array 내 최대값 또는 최소값의 index를 반환함
# a = np.array([1,2,3,4,5,8,78,23,3])
# print(np.argmax(a), np.argmin(a)) #최대값 최소값
# #axis기반
# a=np.array([[1,2,4,7], [9,88,6,45], [9,76,3,4]])
# print(np.argmax(a, axis=1), np.argmin(a, axis=0)) # axis=1은 가로중의 인덱스, axis=0은 세로중의 인덱스


# #boolean index
# a = np.array(
#     [[0,5,10,15,20],
#     [1,6,11,16,26],
#     [2,7,12,17,22]])
# b = a < 15
# print(b)
# print()
# print(b.astype(np.int))

# #fancy index
# # numpy는 array를 index value로 사용해서 값을 추출하는 방법
# # a = np.array([2,4,6,8])
# # b = np.array([0,0,1,3,2,1], int)
# # print(a[b])
# # print(a.take(b)) # a[b] 와 똑같지만 명시적으로 이렇게 사용하는것을 선호한다고함
#
# #matrix 형태의 데이터도 가능
# a = np.array([[1,4], [9,16]], float)
# b = np.array([0,0,1,1,0], int)
# c = np.array([0,1,1,1,1], int)
# print(a[b,c])


#numpy object -npy
#numpy object (pickle)형태로 데이터를 저장하고 불러옴
#binary 파일 형태로 저장함


