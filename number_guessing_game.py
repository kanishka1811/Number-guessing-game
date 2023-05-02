import random
from art_number_guess import logo
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1,100)

if difficulty == "easy":
    rounds=10
else:
    rounds=5

while rounds>0:
    print(f"You have {rounds} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess>number:
        print("Too high.")
        rounds = rounds-1
    elif guess<number:
        print("Too low.")
        rounds = rounds-1
    elif guess==number:
        print(f"You got it! The answer was {number}")
        break

if rounds==0:
    print(f"You lost! You ran out of lives. The number was {number}.")

