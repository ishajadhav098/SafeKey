RSA decryption

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def generateKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    d = modInverse(e, phi)
    return e, d, n

def encrypt(m, e, n):
    return power(m, e, n)

def decrypt(c, d, n):
    return power(c, d, n)

p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
M = int(input("Enter the message (as a number): "))

e, d, n = generateKeys(p, q)

print(f"\nPublic Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")

print(f"\nOriginal Message: {M}")
C = encrypt(M, e, n)
print(f"Encrypted Message: {C}")
        
C = int(input("\nEnter the ciphertext to decrypt: "))
decrypted = decrypt(C, d, n)
print(f"Decrypted Message: {decrypted}")
