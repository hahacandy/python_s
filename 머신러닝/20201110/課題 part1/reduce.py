from functools import reduce

result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# ((((1+2)+3)+4)+5)
print(result)
# 15


result = reduce(lambda x, y: x if x > y else y, [1, 2, 3, 4, 5])
# 최댓값을 구함
print(result)
# 5