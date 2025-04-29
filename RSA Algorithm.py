import random
from sympy import isprime

def generate_keypair(bits=8):
    p = q = 0
    while not isprime(p):
        p = random.getrandbits(bits)
    while not isprime(q) or p == q:
        q = random.getrandbits(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    e = d = 0
    while e < phi:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break
    d = modinv(e, phi)
    
    return (e, n), (d, n)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(plaintext, pubkey):
    e, n = pubkey
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(ciphertext, privkey):
    d, n = privkey
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Example Usage
public_key, private_key = generate_keypair()
plaintext = "Hello"
ciphertext = encrypt(plaintext, public_key)
decrypted = decrypt(ciphertext, private_key)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")
print(f"Encrypted Text: {ciphertext}")
print(f"Decrypted Text: {decrypted}")
