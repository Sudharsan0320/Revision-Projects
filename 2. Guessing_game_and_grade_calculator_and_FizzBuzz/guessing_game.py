import random

secret_number = random.randint(1, 100)
tries = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    tries += 1
    if guess < secret_number:
        print("higher")
    elif guess > secret_number:
        print("lower")
    else:
        print(f"Exactly right! You won in {tries} tries!")
        break
    if tries == 7:
        print(f"Game over! You've reached the maximum of 7 tries. The number was {secret_number}.")
        break