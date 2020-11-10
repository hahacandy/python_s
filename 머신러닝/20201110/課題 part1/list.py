oper_permutation = []
input_oper = [1,2,3,4]
[oper_permutation.extend("a") for index, value in enumerate(input_oper) if value > 0]
print(oper_permutation)