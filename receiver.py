"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.decrypt import get_original_message, get_keys
from settings import E
import sys
import json
import time


option = ""

try:
    option = str(sys.argv[1])
except IndexError:
    pass

start = time.time()

if option == "decrypt":
    with open("encrypted_message.txt", "r") as encrypted_message:
        message = encrypted_message.read()

    with open("private_key.json", "r") as jsonFile:
        private_key_file = json.load(jsonFile)

        p = private_key_file["p"]
        q = private_key_file["q"]
        private_key = private_key_file["private_key"]

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
        if sys.argv.count("--nosave") > 0:
            do_save = False
    except IndexError:
        pass

    if do_save:
        public_data = {"n": n, "e": E}

        private_data = {"p": p, "q": q, "private_key": private_key}

        with open("public_key.json", "w") as jsonFile:
            json.dump(public_data, jsonFile)

        with open("private_key.json", "w") as jsonFile:
            json.dump(private_data, jsonFile)


else:
    print("Please provide valid option: 'get_keys' or 'decrypt'.")

end = time.time()

print(f"\nTime-to-Complete: {str(round(end - start, 4))}s")
