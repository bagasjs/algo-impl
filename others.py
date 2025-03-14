# euclid's greatest common divisor
def egcd(a: int, b: int) -> int:
    if b > a: 
        t = a
        a = b
        b = t

    while b != 0:
        r = a % b
        a = b
        b = r
    return a

if __name__ == "__main__":
    print(egcd(100, 75))

