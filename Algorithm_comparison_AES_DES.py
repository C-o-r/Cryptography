import time
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib

# Function to generate a random key of a specified length
def generate_key(length):
    return get_random_bytes(length)

# Function to encrypt data using AES
def aes_encrypt(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return ciphertext, cipher.iv

# Function to decrypt data using AES
def aes_decrypt(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Function to encrypt data using DES
def des_encrypt(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, DES.block_size))
    return ciphertext

# Function to decrypt data using DES
def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext

# Generate random data to encrypt
data_to_encrypt = b"This is a test message for encryption using AES and DES."

# Generate random keys for AES and DES
aes_key = generate_key(16)  # AES-128
des_key = generate_key(8)   # DES

# Measure the time taken for AES encryption and decryption
start_time = time.time()
aes_ciphertext, aes_iv = aes_encrypt(aes_key, data_to_encrypt)
aes_decrypted = aes_decrypt(aes_key, aes_iv, aes_ciphertext)
aes_time = time.time() - start_time

# Measure the time taken for DES encryption and decryption
start_time = time.time()
des_ciphertext = des_encrypt(des_key, data_to_encrypt)
des_decrypted = des_decrypt(des_key, des_ciphertext)
des_time = time.time() - start_time

# Print results
print("Original Data:", data_to_encrypt.decode())
print("\nAES-128 Encryption:")
print("Ciphertext:", aes_ciphertext)
print("Decrypted Data:", aes_decrypted.decode())
print("AES-128 Time Taken:", aes_time, "seconds\n")

print("DES Encryption:")
print("Ciphertext:", des_ciphertext)
print("Decrypted Data:", des_decrypted.decode())
print("DES Time Taken:", des_time, "seconds\n")

# Performance comparison
if aes_time < des_time:
    print("AES is faster.")
else:
    print("DES is faster.")
