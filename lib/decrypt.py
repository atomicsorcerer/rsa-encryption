"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""


from lib.utils import phi, convert_from_ascii


def decrypt(cipher, private_key, p, q, mod):
    return (cipher ** (private_key % phi(p, q))) % mod


def get_original_message(message, private_key, p, q, n):
    message_list = message.replace("[", "").replace("]", "").split(",")

    message_list = [int(i) for i in message_list]

    decipher_text = convert_from_ascii(
        [int(decrypt(i, private_key, p, q, n)) for i in message_list]
    )

    return decipher_text
