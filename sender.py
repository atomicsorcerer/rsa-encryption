"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""


from lib.utils import convert_to_ascii

e = int(input("Enter Exponent: "))

n = int(input("Enter N (other part of public key): "))

message = str(input("Enter message: "))

ascii_message = convert_to_ascii(message)

cipher_text = [(i**e) % n for i in ascii_message]

if __name__ == "__main__":
    print(cipher_text)
