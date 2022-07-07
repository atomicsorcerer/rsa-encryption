"""
RSA Encryption from Scratch
Empire Encryption
© Atomic Sorcerer 2022
"""


from math import gcd


def phi(n, x=None):
    if x is None:
        result = 1

        for i in range(2, n):
            if gcd(i, n) == 1:
                result += 1

        return result
    else:
        return (n - 1) * (x - 1)


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def mod_inv(a, m):
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
