def add(a, b):
    return a + b

def minus(a, b):
    if a > b:
        return a - b
    elif b > a:
        return b - a
    
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

div = divide(4, 6)
sum = add(4, 6)
mul = multiply(4, 6)
mi = minus(4, 6)
print("두수의 합=>", sum, "두수의 차 =>", mi, "두수의 곱=>", mul, "나눗셈=>", div)
