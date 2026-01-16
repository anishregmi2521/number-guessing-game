from art import logo
import random
print("Welcome to the Number Guessing Game!")
print(logo)
number_to_guess = random.randint(1, 100)
level = int(input("Choose difficulty: Type 1 for Easy or 2 for Hard: "))

if level == 1:
    attempts = 5
elif level == 2:
    attempts = 3
else:
    print("Invalid level selected.")
    exit()
while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You've guessed the number.")
        break

    attempts -= 1
    print(f"Attempts left: {attempts}")
if attempts == 0:
    print("❌ You ran out of attempts.")
    print("The number was:", number_to_guess)
