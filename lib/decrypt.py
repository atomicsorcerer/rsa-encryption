"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.generate_primes import get_prime
from lib.utils import phi, convert_from_ascii, mod_inv
from settings import KEY_BIT_SIZE, E

from math import lcm
import decimal

decimal.getcontext().prec = KEY_BIT_SIZE


def decrypt(cipher: int, private_key: int, p: int, q: int) -> int:
    d_p = private_key % (p - 1)
    d_q = private_key % (q - 1)
    q_inv = pow(q, -1, p)

    m_1 = pow(cipher, d_p, p)
    m_2 = pow(cipher, d_q, q)

    h = int(
        (decimal.Decimal(q_inv) * decimal.Decimal(m_1 - m_2)) % decimal.Decimal(p * q)
    )

    return (m_2 + (h * q)) % (p * q)


def get_original_message(
    message: str | list[int], private_key: int, p: int, q: int, n: int
) -> list[str]:
    if isinstance(message, str):
        message_list = message.replace("[", "").replace("]", "").split(",")

        message_list = [int(i) for i in message_list]

        return convert_from_ascii(
            [decrypt(i, private_key, p, q) for i in message_list]
        )

    return convert_from_ascii([int(decrypt(i, private_key, p, q)) for i in message])


def get_keys(key_size: int = KEY_BIT_SIZE, e: int = E) -> tuple[int, int, int]:
    p = get_prime(bit_size=key_size / 2)

    q = get_prime(bit_size=key_size / 2)

    if p == q:
        return get_keys(key_size, e)

    carmichael_totient = lcm(p - 1, q - 1)

    private_key = mod_inv(e, carmichael_totient)

    return p, q, private_key
