import random
import os
import time

COLOR_SYMBOLS = {
    1: "🟣",
    2: "🔴",
    3: "🔵",
    4: "🟠",
    5: "🟢",
    6: "🟡",
}


def generate_secret_combination():
    return [random.randint(1, 6) for _ in range(4)]


def display_combination(combination):
    """Return a string of emoji colors for the given combination."""
    return " ".join(COLOR_SYMBOLS[num] for num in combination)


def get_player_guess():
    """Ask the player to input 4 numbers (1-6)."""
    while True:
        try:
            guess = [int(num) for num in input("Enter 4 numbers (1-6): ").split()]
            if len(guess) != 4 or any(num < 1 or num > 6 for num in guess):
                raise ValueError
            return guess
        except ValueError:
            print("❌ Invalid input. Please enter exactly 4 numbers between 1 and 6.")


def compute_feedback(secret_combination, player_guess):
    correct_position = sum(s == g for s, g in zip(secret_combination, player_guess))
    secret_remaining = []
    guess_remaining = []
    for s, g in zip(secret_combination, player_guess):
        if s != g:
            secret_remaining.append(s)
            guess_remaining.append(g)
    correct_color = 0
    for color in guess_remaining:
        if color in secret_remaining:
            correct_color += 1
            secret_remaining.remove(color)
    return correct_position, correct_color


# --- Main game loop ---
secret_combination = generate_secret_combination()
max_attempts = 10
attempt = 0

print("🎯 Welcome to MasterMind!")
print("Colors available:")
for number, symbol in COLOR_SYMBOLS.items():
    print(f"{number}: {symbol}")
print("\nTry to guess the secret combination of 4 colors!")
print("Symbol meaning → * : correct position | - : correct color\n")

while attempt < max_attempts:
    attempt += 1
    print(f"\nAttempt {attempt}/{max_attempts}")
    player_guess = get_player_guess()
    correct_position, correct_color = compute_feedback(secret_combination, player_guess)
    feedback = "*" * correct_position + "-" * correct_color
    print("Your guess:", display_combination(player_guess))
    print("Feedback:", feedback)

    if correct_position == 4:
        print("\n🎉 You found the secret combination!")
        print("Secret was:", display_combination(secret_combination))
        break
else:
    print(
        "\n😢 You lost! The secret combination was:",
        display_combination(secret_combination),
    )
