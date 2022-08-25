"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.decrypt import get_original_message, get_keys
from settings import E
import sys


option = ""

try:
    option = str(sys.argv[1])
except IndexError:
    pass


if option == "decrypt":
    message = str(input("Enter Cipher Text: "))

    p = int(input("Enter p: "))

    q = int(input("Enter q: "))

    private_key = int(input("Enter Private Key: "))

    decipher_text = get_original_message(message, private_key, p, q, p * q)

    print("\nDeciphered Message: " + "".join(decipher_text))

elif option == "get_keys":
    p, q, private_key = get_keys()

    n = p * q

    print("--Public Key--")

    print(f"n = {n}")
    print(f"e = {E}\n")

    print("--Private Key--")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"Private Key = {private_key}")

    do_save = True

    try:
        if sys.argv[2] == "--nosave":
            do_save = False
    except IndexError:
        pass

    if do_save:
        keys_file = open("keys.txt", "w")

        keys_file.write("--Public Key--\n")
        keys_file.write(f"n = {n}\n")
        keys_file.write(f"e = {E}\n\n")

        keys_file.write("--Private Key--\n")
        keys_file.write(f"p = {p}\n")
        keys_file.write(f"q = {q}\n")
        keys_file.write(f"Private Key = {private_key}\n")

        keys_file.close()

else:
    print("Please provide valid option: 'get_keys' or 'decrypt'.")
