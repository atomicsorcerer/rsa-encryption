![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# RSA Encryption from Scratch
A full implementation of the original RSA encryption method from scratch
## Description
RSA encryption secures the modern digital world. RSA encryption relies on modular arithmetic and how difficult it is to factor the product of two large prime numbers. This project aims to show how this encryption originally worked in an accessible manner. Though some of the math tricks have changed, the core idea of RSA remains the same.
## Dependencies
Since this project aims to transparently show how RSA encryption works, the only dependencies are the Python standard library and the built-in math module.
## Usage
RSA encryption works with the receiver first sharing a public key. There are two parts to the public key, and they will both be used to encrypt messages. To get the public key and private key, run the following command:
```
$ python receiver.py get_keys

--Public Key--
n = ...
e = 65537 (this is standard for RSA encryption)

--Private Key--
p = ...
q = ...
Private Key = ...

```
After sharing the values of `n` and `e`, the public key, the sender can run the following command to encrypt a message.
```
$ python sender.py

Enter Exponent: ...
Enter N (other part of public key): ...
Enter message: "..."
```
Finally, after sending the encrypted message to the receiver, run the following command and fill out the prompts.
```
$ python receiver.py decrypt

Enter Cipher Text: [..., ..., ..., ....]
Enter n: ...
Enter Private Key: ...

Deciphered Message: "..."
```
## Authors
This project was created and is maintained [@atomicsorcerer](https://github.com/atomicsorcerer).