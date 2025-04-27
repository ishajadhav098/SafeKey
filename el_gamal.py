el gamal

# Function to calculate modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, p):
    t, new_t = 0, 1
    r, new_r = p, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None  # No inverse exists
    if t < 0:
        t = t + p
    return t

# ElGamal encryption function
def elgamal_encryption(p, e1, d, pt, r):
    # Calculate e2 = e1^d mod p
    e2 = pow(e1, d, p)
    
    # Calculate c1 = e1^r mod p
    c1 = pow(e1, r, p)
    
    # Calculate c2 = pt * (e2^r mod p) mod p
    c2 = (pt * pow(e2, r, p)) % p
    
    return e1, e2, d, c1, c2

# ElGamal decryption function
def elgamal_decryption(p, c1, c2, d):
    # Calculate c1^d mod p
    c1_d = pow(c1, d, p)
    
    # Calculate modular inverse of c1^d mod p
    c1_d_inv = mod_inverse(c1_d, p)
    
    # Decrypt plaintext pt = c2 * (c1^d)^-1 mod p
    pt = (c2 * c1_d_inv) % p
    
    return pt

# Example Usage
p = int(input("Enter a large prime number (p): "))  # User-based prime number
e1 = int(input("Enter the public key component e1: "))  # User-based e1
d = int(input("Enter the private key d: "))  # User-based private key
pt = int(input("Enter the plaintext (pt) less than p: "))  # User-based plaintext
r = int(input("Enter a random integer r: "))  # User-based random integer

# Encryption
e1, e2, d, c1, c2 = elgamal_encryption(p, e1, d, pt, r)
print(f"e1 = {e1}, e2 = {e2}, d = {d}")
print(f"Ciphertext: c1 = {c1}, c2 = {c2}")

# Decryption
decrypted_pt = elgamal_decryption(p, c1, c2, d)
print(f"Decrypted plaintext: {decrypted_pt}")
