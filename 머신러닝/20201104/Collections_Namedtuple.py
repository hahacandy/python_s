from collections import namedtuple

# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])

x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x=11, y=22))


#
def calc(x, y):
    """두수를 입력받아 합, 곱, 나눈값을 반환한다 """
    return namedtuple(typename='return_calc', field_names=['sum', 'multiplication', 'division'])(x + y, x * y, x / y)

rr = calc(3, 2)
print('덧셈:', rr.sum)
print('곱셈결과:', rr.multiplication)
print('나눗셈:', rr.division)

