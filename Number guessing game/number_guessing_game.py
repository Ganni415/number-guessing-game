import random
import time
import json
import os
from colorama import Fore, Style, init
init(autoreset=True)

from utils import get_hint

SCORE_FILE = "high_scores.json"

def welcome():
    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Choose a difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

def get_difficulty():
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                return "Easy", 10
            elif choice == 2:
                return "Medium", 5
            elif choice == 3:
                return "Hard", 3
            else:
                print("Invalid input. Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def load_high_scores():
    if not os.path.exists(SCORE_FILE):
        return {}
    with open(SCORE_FILE, 'r') as f:
        return json.load(f)

def save_high_score(level, attempts):
    scores = load_high_scores()
    best = scores.get(level)
    if best is None or attempts < best:
        scores[level] = attempts
        with open(SCORE_FILE, 'w') as f:
            json.dump(scores, f, indent=2)
        print(f"🎖️ New High Score for {level} difficulty: {attempts} attempts!")
    else:
        print(f"🏆 Current High Score for {level}: {best} attempts")

def play_game():
    number_to_guess = random.randint(1, 100)
    level, chances = get_difficulty()
    print(f"\nYou have selected '{level}' difficulty with {chances} chances.\n")
    
    attempts = 0
    start_time = time.time()

    while chances > 0:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == number_to_guess:
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts and {duration} seconds.")
                save_high_score(level, attempts)
                return
            elif guess < number_to_guess:
                print("❌ Too low!", get_hint(number_to_guess, guess))
            else:
                print("❌ Too high!", get_hint(number_to_guess, guess))
            chances -= 1
            print(f"🔁 Remaining chances: {chances}\n")
        except ValueError:
            print("Please enter a valid number.")

    print(f"💀 You lost! The number was {number_to_guess}.")

def main():
    while True:
        welcome()
        play_game()
        again = input("\nWould you like to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing! See you again!")
            break

if __name__ == "__main__":
    main()
# This code implements a number guessing game with different difficulty levels and high score tracking.