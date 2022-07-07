"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""


from lib import mod_inv, phi
from decrypt import get_original_message
from generate_primes import get_prime
import sys


if str(sys.argv[1]) == "decrypt":
    message = str(input("Enter Cipher Text: "))

    n = int(input("Enter n: "))

    private_key = int(input("Enter Private Key: "))

    decipher_text = get_original_message(message, n, private_key)

    print("\nDeciphered Message: " + "".join(decipher_text))

elif str(sys.argv[1]) == "get_keys":
    p = get_prime()

    q = get_prime()

    e = 65537

    n = p * q

    private_key = mod_inv(e, phi(p * q))

    print(f"n = {n}")
    print(f"e = {e}")
    print(f"Private Key (keep secret) = {private_key}")

else:
    print("Please provide valid option: get_keys or decrypt.")
