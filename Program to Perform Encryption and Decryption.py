# Encrypt the string using Transposition Cipher
def encrypt(text, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(text):
            cipher[col] += text[pointer]
            pointer += key
    return ''.join(cipher)

# Decrypt the string using Transposition Cipher
def decrypt(ciphertext, key):
    num_of_columns = len(ciphertext) // key
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)

    plaintext = [''] * num_of_columns
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Example Usage
text = "Hello World"
key = 4

ciphertext = encrypt(text, key)
print(f"Encrypted Text: {ciphertext}")

decrypted_text = decrypt(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
