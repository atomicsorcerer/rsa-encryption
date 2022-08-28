"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.encrypt import encrypt
from os.path import exists
import json


if not exists("public_key.json"):
    print("No keys generated")
    exit()

with open("public_key.json", "r") as jsonFile:
    data = json.load(jsonFile)

    e = data["e"]

    n = data["n"]

message = str(input("Enter message: "))

cipher_text = encrypt(message, e, n)

if __name__ == "__main__":
    with open("encrypted_message.txt", "w") as message_file:
        message_file.write(str(cipher_text))
