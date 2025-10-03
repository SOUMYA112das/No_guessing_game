import random


def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("\n🎲 Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to find it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < number:
                print(f"Too Low! ❌ (Attempts left: {max_attempts - attempts})")
            elif guess > number:
                print(f"Too High! ❌ (Attempts left: {max_attempts - attempts})")
            else:
                print(
                    f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts."
                )
                break

        except ValueError:
            print("⚠ Invalid input! Please enter a number.")

    if attempts == max_attempts and guess != number:
        print(f"😢 Sorry, you've run out of attempts. The number was {number}.")


while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("👋 Thanks for playing! Goodbye.")
        break
