from functools import reduce

print(reduce(lambda x,y : (lambda x, y: x / y)(x,y), [1,2]))