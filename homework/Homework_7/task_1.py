
secret_number = 7

while True:
    user_guess = int(input("Guess the number: "))

    if user_guess == secret_number:
        print("Congratulations! You guessed it!")
        break
    else:
        print("Try again")