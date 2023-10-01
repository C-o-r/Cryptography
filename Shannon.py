import random

# Simple substitution cipher
def generate_cipher_key():
    # Create a random permutation of the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_key = list(alphabet)
    random.shuffle(cipher_key)
    return dict(zip(alphabet, cipher_key))

def encrypt(plaintext, cipher_key):
    ciphertext = ''
    for char in plaintext:
        if char in cipher_key:
            ciphertext += cipher_key[char]
        else:
            ciphertext += char  # Leave non-alphabet characters unchanged
    return ciphertext

def decrypt(ciphertext, cipher_key):
    decryption_key = {v: k for k, v in cipher_key.items()}
    plaintext = ''
    for char in ciphertext:
        if char in decryption_key:
            plaintext += decryption_key[char]
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = "hello"
cipher_key = generate_cipher_key()
ciphertext = encrypt(plaintext, cipher_key)
decrypted_text = decrypt(ciphertext, cipher_key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
