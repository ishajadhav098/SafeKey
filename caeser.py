caeser cipher

encrypt_txt = input("Enter the text to encrypt: ")
n = int(input("Enter the shift value: "))

def encrypt(e_text, shift):
    result = ""
    for i in range(len(e_text)):
        char = e_text[i]
        if char.isalpha(): 
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char 
    return result
print("Encrypted text:", encrypt(encrypt_txt, n))


# decrypt_txt = input("Enter the text to decrypt: ")
# n = int(input("Enter the shift value: "))

def decrypt(d_text, shift):
    result = ""
    for char in d_text:
        if char.isalpha(): 
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char 
    return result

# print("Decrypted text:", decrypt(decrypt_txt, n))
