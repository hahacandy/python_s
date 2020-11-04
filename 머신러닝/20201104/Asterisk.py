# Asterisk
# 함수에 *를 써서 여러개를 받게함

#1. 튜플? 타입
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)


#2. 딕셔너리타입
def asterisk_test(a, **kargs):
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b=2, c=3, d=4, e=5, f=6)

#. 가로로묶으면 한개의 변수로 넘어감
def asterisk_test(a, *args):
    print(a, args[0])
    print(type(args))

asterisk_test(1, (2, 3, 4, 5, 6))
# 그치만 *args 으로 사용하면 언패킹이라해서 2,3,4,5,6 이 나온다고함, 먼가 헷갈림
def asterisk_test(a, args):
    print(a, *args)
    print(type(args))

asterisk_test(1, (2,3,4,5,6))


#
a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(*data)

#
for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(sum(data))

def asterisk_test(a, b, c, d, e=0):
    print(a, b, c, d, e)

#
data = {"b":1 , "c":2, "d":3, "e":56}
asterisk_test(10, **data)