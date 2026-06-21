import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number: "))
    attempts += 1

    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct!")
        print("Attempts:", attempts)
        break
