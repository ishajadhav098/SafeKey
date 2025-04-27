playfair cipher

def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    return text.replace(" ", "")

def groupLetters(text):
    groups = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            groups.append(text[i] + 'x')
            i += 1
        elif i + 1 < len(text):
            groups.append(text[i] + text[i + 1])
            i += 2
        else:
            groups.append(text[i] + 'x')  
            i += 1
    return groups
            
            
def generateMatrix(key, list): 
    keyLetters = []
    for i in key:
        if i not in keyLetters:
            keyLetters.append(i)
            
    elements = []
    for i in keyLetters:
        if i not in elements:
            elements.append(i)
            
    for i in list:
        if i not in elements:
            elements.append(i)
            
    matrix = []
    while elements != []:
        matrix.append(elements[0:5])
        elements = elements[5:]
        
    return matrix

def findPosition(matrix, ch):
    for i, row in enumerate(matrix):
        if ch in row:
            return i, row.index(ch)

def encryptPair(pair, matrix):
    r1, c1 = findPosition(matrix, pair[0])
    r2, c2 = findPosition(matrix, pair[1])
    
    if r1 == r2: 
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2: 
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]
    
def encryptText(text, key):
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i/j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = removeSpaces(toLowerCase(text)).replace('j', 'i')
    key = removeSpaces(toLowerCase(key)).replace('j', 'i')
    
    text = ''.join(groupLetters(text))
    matrix = generateMatrix(key, list)
    
    print("Playfair Cipher Matrix:") 
    for row in matrix:
        print(' '.join(row))
        
    encryptedText = ''
    for pair in groupLetters(text):
        encryptedText += encryptPair(pair, matrix)
    return encryptedText

text = input("Enter the text to encrypt: ")
key = input("Enter the key: ")

encrypted_text = encryptText(text, key)
print("\nEncrypted text:", encrypted_text)
