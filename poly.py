vigerene cipher

def generate_key(msg, key):
    # Repeats or trims the key to match the length of the message
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_polyalphabetic(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)  # Generate a key of the same length as the message
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            res = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))  # Encrypt uppercase letters
        elif char.islower():
            res = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))  # Encrypt lowercase letters
        else:
            res = char  # Keep non-alphabet characters unchanged
        encrypted_text.append(res)
    return "".join(encrypted_text)

def decrypt_polyalphabetic(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)  # Generate a key of the same length as the message
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            res = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))  # Decrypt uppercase letters
        elif char.islower():
            res = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))  # Decrypt lowercase letters
        else:
            res = char  # Keep non-alphabet characters unchanged
        decrypted_text.append(res)
    return "".join(decrypted_text)

# Main program
text = input("Enter the text to encrypt: ").strip()
key = input("Enter the key: ").strip()

generated_key = generate_key(text, key)
print("\nGenerated Key: ", generated_key)

encrypted_text = encrypt_polyalphabetic(text, key)
print("\nEncrypted Text: ", encrypted_text)

decrypted_text = decrypt_polyalphabetic(encrypted_text, key)
print("Decrypted Text: ", decrypted_text)
