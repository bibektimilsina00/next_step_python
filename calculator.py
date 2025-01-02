def add(a, b):
    return a + b
def mult(a, b):
    return a * b
def div(a, b):
    if b ==0:
        print("Cant div by 0")
    else:
        return a / b
def sub(a, b):
    return a - b
def main():
    operator = input("Enter the operator")
    a = 1
    b = 2
    if operator == "+":
        print(f"Sum is {add(a,b)}")
    if operator == "-":
        print(f"Diff is {sub(a,b)}")
    if operator == "*":
        print(f"Proudct is {mult(a,b)}")
    if operator == "/":
        print(f"Value is {div(a,b)}")

main()
