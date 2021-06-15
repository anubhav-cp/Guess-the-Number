import random

rand_num = random.randint(0, 10)

attempts = 3
while attempts > 0:

    guess_num = int(input("Guess the Number: "))
    if guess_num == rand_num:
        print("You Guessed Correctly")
        break
    elif guess_num < rand_num:
        print("Guessed Number is Low")
        print("Attempts Remaining: ", attempts - 1)

    elif guess_num > rand_num:
        print("Guessed Number is High")
        print("Attempts Remaining: ", attempts - 1)

    attempts -= 1
