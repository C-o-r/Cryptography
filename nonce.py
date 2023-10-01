import hashlib
import random
import os

# Simulated shared secret between Alice and Bob
shared_secret = os.urandom(16)  # Generate a random 16-byte secret

# Define a function to generate a random nonce
def generate_nonce():
    return os.urandom(8)  # Generate an 8-byte (64-bit) random nonce

# Simulate Alice and Bob's exchange of nonces
alice_nonce = generate_nonce()
bob_nonce = generate_nonce()

# Simulate the exchange of nonces over a public channel (e.g., the Internet)
# In practice, nonces should be transmitted securely.

# Alice and Bob calculate their shared keys using the nonces and shared secret
alice_key = hashlib.sha256(shared_secret + alice_nonce + bob_nonce).digest()
bob_key = hashlib.sha256(shared_secret + bob_nonce + alice_nonce).digest()

# Simulate the exchange of messages with encrypted keys
# In practice, a secure channel should be used for this exchange.

# Define a simple encryption function (for demonstration purposes)
def encrypt(plaintext, key):
    # In practice, use a secure encryption algorithm like AES
    encrypted_text = bytes([p_byte ^ k_byte for p_byte, k_byte in zip(plaintext, key)])
    return encrypted_text

# Define a simple decryption function (for demonstration purposes)
def decrypt(ciphertext, key):
    # In practice, use a secure decryption algorithm like AES
    decrypted_text = bytes([c_byte ^ k_byte for c_byte, k_byte in zip(ciphertext, key)])
    return decrypted_text

# Alice encrypts a message using her derived key
plaintext_message = "Hello, Bob!".encode('utf-8')  # Encode as UTF-8
cipher_text = encrypt(plaintext_message, alice_key)

# Bob decrypts the message using his derived key
decrypted_message = decrypt(cipher_text, bob_key)

# Print the results in hexadecimal format
print("Alice's Nonce:", alice_nonce.hex())
print("Bob's Nonce:", bob_nonce.hex())
print("Alice's Key:", alice_key.hex())
print("Bob's Key:", bob_key.hex())
print("Plaintext Message:", plaintext_message.decode('utf-8'))  # Decode as UTF-8 for printing
print("Cipher Text (Hex):", cipher_text.hex())
print("Decrypted Message (Hex):", decrypted_message.hex())
