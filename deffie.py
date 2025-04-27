diffie hellman

def power(a, b, p):
    return pow(a, b, p)

P = int(input("Enter a prime number P: "))

G = int(input("\nEnter a primitive root G for P: "))

a = int(input("\nEnter Alice's private key a: "))

x = power(G, a, P)
print("The public key x for Alice:", x)

b = int(input("\nEnter Bob's private key b: "))

y = power(G, b, P)
print("The public key y for Bob:", y)

ka = power(y, a, P)  
kb = power(x, b, P)  

print("\nSecret key for Alice is:", ka)
print("Secret key for Bob is:", kb)
