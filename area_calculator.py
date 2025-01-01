def calculate_area(length: int = 0, breath: int = 0) -> int:
    return length * breath


def main():
    length = int(input("Enter the Length of Rectangle: \t"))
    breath = int(input("Enter the Breanth of Rectangle: \t"))
    area = calculate_area(length=length, breath=breath)

    print(f"The Area of Rectangle with length {length} and breath {breath} is {area}")


main()
