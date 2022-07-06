"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""


def phi(x, y):
    return (x - 1) * (y - 1)


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def convert_to_ascii(m):
    final_message = []

    for i in range(len(m)):
        final_message.append(int(ord(m[i])))

    return final_message


def convert_from_ascii(m):
    return list(map(lambda x: chr(int(x)), m))
