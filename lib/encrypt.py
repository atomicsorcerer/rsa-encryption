"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.utils import convert_to_ascii


def encrypt(plain_text, e, n):
    ascii_message = convert_to_ascii(plain_text)

    return [(i**e) % n for i in ascii_message]
