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

    if len(result) == len(matrix_variables):
        result = True
    else:
        result = False

    return result


def is_matrix_equal(*matrix_variables):
    return None


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None


def matrix_transpose(matrix_variable):
    return None


def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return None


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return None

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

    matrix_x = [[2, 2], [2, 2]]
    matrix_y = [[2, 5], [2, 1]]

    print(is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y))  # Expected value: False
    print(is_matrix_equal(matrix_x, matrix_x))  # Expected value: True