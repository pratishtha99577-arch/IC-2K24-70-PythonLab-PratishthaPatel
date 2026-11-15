import random

num = random.randint(1, 100)

for i in range(7):
    guess = int(input("Guess the number: "))

    if guess == num:
        print("Congratulations! Correct guess.")
        break
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

else:
    print("Game over! The number was", num)