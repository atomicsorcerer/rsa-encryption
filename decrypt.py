"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""


from lib import phi, convert_from_ascii


def decrypt(cipher, private_key, mod):
    return (cipher ** (private_key % phi(mod))) % mod


def get_original_message(message, n, private_key):
    message_list = message.replace("[", "").replace("]", "").split(",")

    message_list = [int(i) for i in message_list]

    decipher_text = convert_from_ascii([int(decrypt(i, private_key, n)) for i in message_list])

    return decipher_text
