# Pythonice Code 파트의 과제2번째
# 도저희 이건 문제가 뭘 뜻하는지 이해를 못했어서 영상을 참고햇음

import  itertools
from functools import reduce
import sys
import time

def insert_operation(length, input_num, input_oper):
    ops = {"0":(lambda x,y:x+y), "1":(lambda x,y: x-y), "2":(lambda x,y: x*y), "3":(lambda x,y: x/y)}
    oper_permutation = []
    result = []
    [oper_permutation.extend([str(index)] * value) for index, value in enumerate(input_oper) if value > 0]
    print(oper_permutation)

    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]
    print(permutation)


    for i in permutation:
        result.append(reduce(lambda x, y : ops[i.pop()](x, y), input_num))

    print(str(max(result)) + " : " + str(min(result)))




if __name__ == "__main__":
    # print(list('ddfwef'))

    # n = 6
    # numbers = [1,2,3,4,5,6]
    # arithmetics = [2,1,1,1]

    # n = 2
    # numbers = [5,6]
    # arithmetics = [0,0,1,0]

    n = 3
    numbers = [3,4,5]
    arithmetics = [1,0,1,0]
    insert_operation(n, numbers, arithmetics)
