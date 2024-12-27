import random

number = random.randint(1, 10)
attempt = 0

while attempt <= 3:
    user_guess = int(input("Guess the number between 1 to 10"))
    attempt += 1

    if user_guess > 10 or user_guess < 0:
        print("Please Enter the valid number")

    else:
        if number == user_guess:
            print("Congrats you win!!!!!!!")
            break
        elif user_guess < number:
            print("your guess is low, Please guess the higher number")
        else:
            print("Your guess is high, Please guess the lower number")
