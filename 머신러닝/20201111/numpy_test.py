import numpy as np

test_array =  np.array([1,4,5,8], float)
# print(test_array)
# print(type(test_array[3]))

# test_array =  np.array([1,4,5,8], dtype=float16) 이런건 주피터나, 구글코랩에서만 가능한듯, 아니면 아나콘다 풀버전
# test_array =  np.array([1,4,5,8], dtype=float)
# print(type(test_array[3]))


#가로 세로 크기를 나타냄 shape
test_array =  np.array([1,4,5,8], float)
test_array2 =  np.array([[1,4,5,8],[1,2,3,4]], float)
test_array3 =  np.array([[[1,4,5,8],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]], float)
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

#flatten 다차원 array를 1차원 array 로 표현
print(test_array3.flatten())