"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.decrypt import get_original_message, get_keys
from lib.encrypt import encrypt
from settings import E
import time


def run_test(key_size: int, e: int, sample_message: str) -> tuple[str, int, int, int]:
    p, q, private_key = get_keys(key_size=key_size, e=e)
    n = p * q

    encrypted_message = encrypt(sample_message, e, n)

    decrypted_message = get_original_message(encrypted_message, private_key, p, q, n)

    return "".join(decrypted_message), p, q, private_key


def run_series_test(
    iterations: int,
    starting_key_size: int = 8,
    e: int = E,
    sample_message: str = "Hello, world!",
) -> None:
    current_key_size = starting_key_size

    for i in range(iterations):
        start = time.time()
        test_output, p, q, private_key = run_test(current_key_size, e, sample_message)
        end = time.time()

        if test_output == sample_message:
            print(
                f"\033[92mTest #{i + 1}: \033[1mPassed\033[0m\033[92m - key_size={current_key_size}\t\tduration={round(end - start, 4)}s\033[0m"
            )
        else:
            print(
                f"\033[91mTest #{i + 1}: \033[1mFailed\033[0m\033[91m - key_size={current_key_size}\t\tduration={round(end - start, 4)}s\033[0m"
            )
        current_key_size *= 2


if __name__ == "__main__":
    run_series_test(10, sample_message="Hello, world!")
