"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""
from lib.encrypt import encrypt


e = int(input("Enter Exponent: "))

n = int(input("Enter N (other part of public key): "))

message = str(input("Enter message: "))

cipher_text = encrypt(message, e, n)

if __name__ == "__main__":
    print(cipher_text)
