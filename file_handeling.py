try:
    file = open("hello.txt", "r")
    print(file.read())
except FileNotFoundError as e:
    print("File Not found", e)
except:
    print("Something went wrong")
finally:
    file.close()
