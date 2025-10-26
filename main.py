import random

AVAILABLE_ITEMS = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 10


def generate_secret_sequence():
    return [random.choice(AVAILABLE_ITEMS) for _ in range(CODE_LENGTH)]


def evaluate_guess(secret_sequence, player_guess):
    secret_copy = secret_sequence.copy()
    guess_copy = player_guess.copy()

    correct_position = 0
    for index in range(CODE_LENGTH):
        if guess_copy[index] == secret_copy[index]:
            correct_position += 1
            secret_copy[index] = guess_copy[index] = None

    correct_item_wrong_position = 0
    for index in range(CODE_LENGTH):
        if guess_copy[index] is not None and guess_copy[index] in secret_copy:
            correct_item_wrong_position += 1
            secret_copy[secret_copy.index(guess_copy[index])] = None

    return correct_position, correct_item_wrong_position


def play_mastermind(secret_sequence):
    attempts = 0

    print("🎯 Welcome to Mastermind!")
    print(f"Available items: {', '.join(AVAILABLE_ITEMS)}")
    print(
        f"Guess the secret sequence of {CODE_LENGTH} items. You have {MAX_ATTEMPTS} attempts.\n"
    )

    while attempts < MAX_ATTEMPTS:
        player_input = input(f"Attempt {attempts + 1}: ").strip().title().split()

        if len(player_input) != CODE_LENGTH or any(
            item not in AVAILABLE_ITEMS for item in player_input
        ):
            print(
                f"Invalid input! Enter {CODE_LENGTH} items from: {', '.join(AVAILABLE_ITEMS)}\n"
            )
            continue

        attempts += 1
        correct_position, correct_item_wrong_position = evaluate_guess(
            secret_sequence, player_input
        )

        print(
            f"Feedback: {'*' * correct_position}{'-' * correct_item_wrong_position}\n"
        )

        if correct_position == CODE_LENGTH:
            print(
                f"🎉 Congratulations! You guessed the secret sequence in {attempts} attempts."
            )
            return

    print("😢 You lost! The secret sequence was:", " ".join(secret_sequence))


secret_sequence = generate_secret_sequence()
play_mastermind(secret_sequence)
