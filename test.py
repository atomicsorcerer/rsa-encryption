"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.decrypt import get_original_message, get_keys
from lib.encrypt import encrypt
from settings import E

from timeit import timeit


def run_test(key_size, e, sample_message):
    p, q, private_key = get_keys(key_size=key_size, e=e)
    n = p * q

    encrypted_message = encrypt(sample_message, e, n)

    decrypted_message = get_original_message(encrypted_message, private_key, p, q, n)

    return "".join(decrypted_message), p, q, private_key


def run_series_test(
    iterations, starting_key_size=8, e=E, sample_message="Hello, world!"
):
    current_key_size = starting_key_size

    for i in range(iterations):
        test_output, p, q, private_key = run_test(current_key_size, e, sample_message)

        if test_output == "Hello, world!":
            print(
                f"Test #{i + 1}: Passed - key_size={current_key_size}, p={p}, q={q}, private_key={private_key}"
            )
        else:
            print(
                f"Test #{i + 1}: Failed - key_size={current_key_size}, p={p}, q={q}, private_key={private_key}"
            )

        current_key_size *= 2


if __name__ == "__main__":
    run_series_test(2)
