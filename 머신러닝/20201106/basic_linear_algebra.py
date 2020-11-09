def vector_size_check(*vector_variables):
    result = []
    for vector_variable in vector_variables:
        if(len(vector_variables[0]) == len(vector_variable)):
            result.append(1)
        else:
            result.append(0)
    return all(result)


def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables):
        result = [sum(t) for t in zip(*vector_variables)]
        return result
    else:
        raise ArithmeticError


def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables):
        result = [t[0]-sum([a for idx, a in enumerate(t) if idx > 0]) for idx, t in enumerate(zip(*vector_variables))]
        return result
    else:
        raise ArithmeticError


def scalar_vector_product(alpha, vector_variable):
    result = [alpha*a for a in vector_variable]
    return result


def matrix_size_check(*matrix_variables):
    result = []
    [result.append(1) for a in matrix_variables if len(matrix_variables[0]) == len(a)]

    return len(result) == len(matrix_variables)


def is_matrix_equal(*matrix_variables):
    result = []
    [result.append(matrix_variables[0] == a) for a in matrix_variables]
    return all(result)


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    else:
        result = [[sum(b) for b in zip(*a)] for a in zip(*matrix_variables)]
    return result


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    else:
        result = [[sum(a[0])-sum(b) for b in zip(*a)] for a in zip(*matrix_variables)]
    return result


def matrix_transpose(matrix_variable):
    result = [a for a in zip(*matrix_variable)]
    return result


def scalar_matrix_product(alpha, matrix_variable):
    result = [[alpha*b for b in a] for a in matrix_variable]
    return result


def is_product_availability_matrix(matrix_a, matrix_b):
    return True


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    else:
        result = [[sum(aa*bb for aa, bb in zip(a, b)) for b in zip(*matrix_b)]for a in matrix_a]

    return result

if __name__ == "__main__":
    # print(vector_size_check([1, 2, 3], [2, 3, 4], [5, 6, 7]))  # Expected value: True
    # print(vector_size_check([1, 3], [2, 4], [6, 7]))  # Expected value: True
    # print(vector_size_check([1, 3, 4], [4], [6, 7]))  # Expected value: False

    # print(vector_addition([1, 3], [2, 4], [6, 7]))  # Expected value: [9, 14]
    # print(vector_addition([1, 5], [10, 4], [4, 7]))  # Expected value: [15, 16]
    # print(vector_addition([1, 3, 4], [4], [6, 7]))  # Expected value: ArithmeticError

    # print(vector_subtraction([1, 3], [2, 4]))  # Expected value: [-1, -1]
    # print(vector_subtraction([1, 5], [10, 4], [4, 7]))  # Expected value: [-13, -6]

    # print(scalar_vector_product(5, [1, 2, 3]))  # Expected value: [5, 10, 15]
    # print(scalar_vector_product(3, [2, 2]))  # Expected value: [6, 6]
    # print(scalar_vector_product(4, [1]))  # Expected value: [4]

    # matrix_x = [[2, 2], [2, 2], [2, 2]]
    # matrix_y = [[2, 5], [2, 1]]
    # matrix_z = [[2, 4], [5, 3]]
    # matrix_w = [[2, 5], [1, 1], [2, 2]]
    # print(matrix_size_check(matrix_x, matrix_y, matrix_z))  # Expected value: False
    # print(matrix_size_check(matrix_y, matrix_z))  # Expected value: True
    # print(matrix_size_check(matrix_x, matrix_w))  # Expected value: True
    #
    # matrix_x = [[2, 2], [2, 2]]
    # matrix_y = [[2, 5], [2, 1]]
    # print(is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y))  # Expected value: False
    # print(is_matrix_equal(matrix_x, matrix_x))  # Expected value: True

    # matrix_x = [[2, 2], [2, 2]]
    # matrix_y = [[2, 5], [2, 1]]
    # matrix_z = [[2, 4], [5, 3]]
    # print(matrix_addition(matrix_x, matrix_y))  # Expected value: [[4, 7], [4, 3]]
    # print(matrix_addition(matrix_x, matrix_y, matrix_z))  # Expected value: [[6, 11], [9, 6]]

    # matrix_x = [[2, 2], [2, 2]]
    # matrix_y = [[2, 5], [2, 1]]
    # matrix_z = [[2, 4], [5, 3]]
    # print(matrix_subtraction(matrix_x, matrix_y))  # Expected value: [[0, -3], [0, 1]]
    # print(matrix_subtraction(matrix_x, matrix_y, matrix_z))  # Expected value: [[-2, -7], [-5, -2]]

    # matrix_w = [[2, 5], [1, 1], [2, 2]]
    # print(matrix_transpose(matrix_w))

    # matrix_x = [[2, 2], [2, 2], [2, 2]]
    # matrix_y = [[2, 5], [2, 1]]
    # matrix_z = [[2, 4], [5, 3]]
    # matrix_w = [[2, 5], [1, 1], [2, 2]]
    # print(scalar_matrix_product(3, matrix_x))  # Expected value: [[6, 6], [6, 6], [6, 6]]
    # print(scalar_matrix_product(2, matrix_y))  # Expected value: [[4, 10], [4, 2]]
    # print(scalar_matrix_product(4, matrix_z))  # Expected value: [[8, 16], [20, 12]]
    # print(scalar_matrix_product(3, matrix_w))  # Expected value: [[6, 15], [3, 3], [6, 6]]

    #
    # matrix_x = [[2, 5], [1, 1]]
    # matrix_y = [[1, 1, 2], [2, 1, 1]]
    # matrix_z = [[2, 4], [5, 3], [1, 3]]
    # print(is_product_availability_matrix(matrix_y, matrix_z))  # Expected value: True
    # print(is_product_availability_matrix(matrix_z, matrix_x))  # Expected value: True
    # print(is_product_availability_matrix(matrix_z, matrix_w))  # Expected value: False //matrix_w가없습니다
    # print(is_product_availability_matrix(matrix_x, matrix_x))  # Expected value: True

    # matrix_x = [[2, 5], [1, 1]]
    # matrix_y = [[1, 1, 2], [2, 1, 1]]
    # matrix_z = [[2, 4], [5, 3], [1, 3]]
    # print(matrix_product(matrix_y, matrix_z))  # Expected value: [[9, 13], [10, 14]]
    # print(matrix_product(matrix_z, matrix_x))  # Expected value: [[8, 14], [13, 28], [5, 8]]
    # print(matrix_product(matrix_x, matrix_x))  # Expected value: [[9, 15], [3, 6]]
    # print(matrix_product(matrix_z, matrix_w))  # Expected value: False


    # test
    matrix_y = [[1, 1, 2], [2, 1, 1]]
    matrix_z = [[2,5,1], [4,3,3]]
    print([[sum(aa*bb for aa, bb in zip(a, b)) for b in matrix_z] for a in matrix_y])