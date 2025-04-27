simple columnar

def encrypt(message, key_order):
    key_length = len(key_order)
    while len(message) % key_length != 0:
        message += '_'

    # Create the grid
    grid = ['' for _ in range(key_length)]
    for index, char in enumerate(message):
        col = index % key_length
        grid[col] += char

    # Reorder columns based on key_order
    ciphertext = ''
    for col_index in key_order:
        ciphertext += grid[col_index]
    
    return ciphertext

def decrypt(ciphertext, key_order):
    key_length = len(key_order)
    num_rows = len(ciphertext) // key_length

    # Create an empty grid
    grid = [''] * key_length

    start = 0
    for col_index in key_order:
        grid[col_index] = ciphertext[start:start+num_rows]
        start += num_rows

    # Read off the grid row by row
    plaintext = ''
    for i in range(num_rows):
        for col in range(key_length):
            plaintext += grid[col][i]

    # Remove padding underscores if any
    return plaintext.rstrip('_')

if __name__ == "__main__":
    msg = input("Enter the message to encrypt: ")
    key_input = input("Enter the key order (space-separated column indices, starting from 0): ")
    key_order = list(map(int, key_input.strip().split()))

    encrypted_text = encrypt(msg, key_order)
    print("Encrypted:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key_order)
    print("Decrypted:", decrypted_text)
