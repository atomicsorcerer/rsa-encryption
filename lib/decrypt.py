"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.generate_primes import get_prime
from lib.utils import phi, convert_from_ascii, mod_inv
from settings import KEY_BIT_SIZE, E


def decrypt(cipher, private_key, p, q, mod):
    return (cipher ** (private_key % phi(p, q))) % mod


def get_original_message(message, private_key, p, q, n):
    if isinstance(message, str):
        message_list = message.replace("[", "").replace("]", "").split(",")

        message_list = [int(i) for i in message_list]

    decipher_text = convert_from_ascii(
        [int(decrypt(i, private_key, p, q, n)) for i in message]
    )

    return decipher_text


def get_keys(key_size=KEY_BIT_SIZE, e=E) -> tuple[int, int, int]:
    p = get_prime(bit_size=key_size / 2)

    q = get_prime(bit_size=key_size / 2)

    private_key = mod_inv(e, phi(p, q))

    return p, q, private_key
