import random

level = int(input("Level: "))
correct_number= random.randint(1, level)
while True:
    guess = int(input("Guess: "))
    if guess > int(correct_number):
        print("Your guess is too high.")
    elif guess < int(correct_number):
        print("Your guess is too low.")
    else:
       print("Correct!")
       break

