def exp(x, y):
    result = 1
    for i in range(y):
        result = result * x
        print(i)
        print(result)
    return result

print(exp(4,3))
