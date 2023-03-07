def factorial_1(num):
    # Recursion
    if num <= 1:
        return 1
    else:
        return num * factorial_1(num - 1)

def factorial_2(num):
    # While loop
    result = 1
    while num != 0:
        result *= num
        num -= 1
    return result

def factorial_3(num):
    # For loop
    result = 1
    for v in range(1, num + 1):
        result *= v
    return result

def factorial(input):
    method = {
        1: factorial_1,
        2: factorial_2,
        3: factorial_3
    }
    return method.get(input)