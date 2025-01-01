def add_sub(a: int, b: int = 0):
    addition = a + b
    subtraction = a - b

    return addition, subtraction


sum, diff = add_sub(2, 5)
print(sum)
print(diff)
