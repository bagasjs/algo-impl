import random
import math

# NOTE(1): The random prime value should not be less than the value it will be encrypted.
# i.e. if we're gonna encrypt and decrypt unicode codepoints then we might need
# number bigger than 2**32
random_prime_a = 101
random_prime_b = 103
n = random_prime_a * random_prime_b
euler_phi_of_n = (random_prime_a - 1) * (random_prime_b - 1)

# pick e such that gcd(e, euler_phi_of_n) == 1
e = random.randrange(1, n)
while math.gcd(e, euler_phi_of_n) != 1:
    e = random.randrange(1, n)

# find d such that (e * d) % euler_phi_of_n == 1
d = pow(e, -1, euler_phi_of_n)  # Python 3.8+ syntax

print("random_prime_a = ", random_prime_a)
print("random_prime_b = ", random_prime_b)
print("n              = ", n)
print("euler_phi_of_n = ", euler_phi_of_n)
print("e              = ", e)
print("d              = ", d)

public_key  = (e, n)
private_key = (d, n)

def encrypt_message(plain: list[int], e: int, n: int) -> list[int]:
    return [ ((i ** e) % n) for i in plain ]

def decrypt_message(cipher: list[int], d: int, n: int) -> list[int]:
    return [ ((i ** d) % n) for i in cipher ]

# NOTE(2): Usually the data is chunked into a several bytes (i.e. 4 bytes)
# packed as a single word either little or big endian
data  = "Hello, World"
plain = [ ord(c) for c in data ]
print("Message: ", plain)
encrypted = encrypt_message(plain, e, n)
print("Encrypted: ", encrypted)
decrypted = decrypt_message(encrypted, d, n)
print("Decrypted: ", decrypted)


"""
TODO:
- Do NOTE(2)
- Use large prime (i.e. 1024 bit-prime) thus we need to generate fresh primes for each generation of public and private key.
  Runs probabilistic primality tests like Miller-Rabin multiple times to ensure the number is very likely prime.
- Ensure random_prime_a and random_prime_b is not too close
"""
