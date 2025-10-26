import random

AVAILABLE_ITEMS = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 10


def generate_secret_sequence():
    return [random.choice(AVAILABLE_ITEMS) for _ in range(CODE_LENGTH)]


secret_sequence = generate_secret_sequence()
print("Secret_sequence_generated :", secret_sequence)


def evaluate_guess(secret_sequence, player_guess):
    secret_copy = secret_sequence.copy()
    guess_copy = player_guess.copy()

    correct_position = 0
    for idx in range(CODE_LENGTH):
        if guess_copy[idx] == secret_copy[idx]:
            correct_position += 1
            secret_copy[idx] = guess_copy[idx] = None

    correct_item_wrong_position = 0
    for idx in range(CODE_LENGTH):
        if guess_copy[idx] is not None and guess_copy[idx] in secret_copy:
            correct_item_wrong_position += 1
            secret_copy[secret_copy.index(guess_copy[idx])] = None

    return correct_position, correct_item_wrong_position


secret_sequence = generate_secret_sequence()
test_guess = ["Red", "Green", "Blue", "Yellow"]
feedback = evaluate_guess(secret_sequence, test_guess)
print("Secret sequence:", secret_sequence)
print("Player guess:", test_guess)
print("Feedback:", "*" * feedback[0] + "-" * feedback[1])
