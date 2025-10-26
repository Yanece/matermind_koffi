import random

AVAILABLE_ITEMS = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 10


def generate_secret_sequence():
    return [random.choice(AVAILABLE_ITEMS) for _ in range(CODE_LENGTH)]


secret_sequence = generate_secret_sequence()
print("Secret_sequence_generated :", secret_sequence)
