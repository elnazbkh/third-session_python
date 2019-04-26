import random
secret = random.randint(1, 101)
num_guess = 5

while num_guess <= 5:
    guess = int(input("guess: "))
    if guess < secret:
        print("your guess is lower than the secret")
    elif guess > secret:
        print("your guess is greater than the secret")
    elif guess == secret:
        print("you're lucky!")
else:
    print("you're a LOSER!")


