## Inspired by [video a](https://www.youtube.com/watch?v=xmwxDHX6xUc) and [video b](https://www.youtube.com/watch?v=uNzaMrcuTM0) by Zach Star with a bit help of ChatGPT
# A simple frequency analysis for a simple encryption algorithm which is the vigener cipher

key   = "Whatever"
data  = "THIS IS SUPER SECRET"

key   = [ ord(c) for c in key ]
data  = [ ord(c) for c in data ]

def encrypt(plain: list[int], key: list[int]) -> list[int]:
    return [ c + key[i % len(key)] for i, c in enumerate(plain) ] 

def decrypt(cipher: list[int], key: list[int]) -> list[int]:
    return [ c - key[i % len(key)] for i, c in enumerate(cipher) ] 

print(data)
print(encrypt(data, key))
print(decrypt(encrypt(data, key), key))
