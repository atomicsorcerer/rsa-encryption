from lib import modinv, phi, convert_from_ascii
from generate_primes import get_prime
import sys

p = get_prime()

q = get_prime()

e = 65537

n = p * q

publicKey = (n, e)

privateKey = modinv(e, phi(p, q))

if str(sys.argv[1]) == "get_keys":
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"Private Key (keep secret) = {privateKey}")
elif str(sys.argv[1]) == "decrypt":
    message = str(input("Enter Cipher Text: "))

    message_list = message.replace("[", "")
    message_list = message_list.replace("]", "")
    message_list = message_list.split(",")
    message_list = [int(i) for i in message_list]

    privateKeyLocal = int(input("Enter Secret Key: "))

    decipher_text = [int((i ** privateKeyLocal) % n) for i in message_list]

    decipher_text = convert_from_ascii(decipher_text)

    print("\nDeciphered Message: " + "".join(decipher_text))
