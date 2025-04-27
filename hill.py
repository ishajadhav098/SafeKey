hill cipher

import numpy as np

def generate_key_matrix(key, size=3):
    # Convert the key into a matrix of numbers
    key = key.split()  # Split the key string into individual numbers
    key_matrix = np.array([int(num) for num in key[:size*size]]).reshape(size, size)
    print("Key Matrix (Numerical):")
    print(key_matrix)
    return key_matrix

def generate_text_matrix(text, size=3):
    # Convert the text into numbers (A=0, B=1, ..., Z=25)
    text = text.replace(" ", "").upper()  # Remove spaces and make it uppercase
    
    # Add padding (26) if the length of the text is not a multiple of 'size'
    while len(text) % size != 0:
        text += 'X'  # Padding with 'X', which will be treated as 26
    
    # Convert each character to its corresponding numerical value
    text_matrices = []
    for i in range(0, len(text), size):
        text_matrix = np.array([ord(c) - 65 if c != 'X' else 26 for c in text[i:i+size]])  # 'X' is 26
        text_matrices.append(text_matrix)
    
    print("\nText Matrix:")
    for mat in text_matrices:
        print(mat.flatten())
    
    return text_matrices

def encrypt_text(text, key_matrix):
    size = key_matrix.shape[0]
    text_matrices = generate_text_matrix(text, size)
    
    encrypted_text = ""
    for matrix in text_matrices:
        encrypted_matrix = np.dot(key_matrix, matrix) % 27  # Modulo 27 to handle padding (26)
        encrypted_text += "".join(chr(num + 65) if num < 26 else 'X' for num in encrypted_matrix)  # Convert back to letters
    
    return encrypted_text

# Input text and key from the user
text = input("Enter the text to encrypt: ").strip()
key = input("Enter the key (numerical values space-separated, length should be a perfect square): ").strip()

# Generate the key matrix from the input key
key_matrix = generate_key_matrix(key, 3)

# Encrypt the text using the key matrix
encrypted_text = encrypt_text(text, key_matrix)

# Show the encrypted text
print("\nEncrypted Text:", encrypted_text)
