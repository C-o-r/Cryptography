import hashlib
import random
from cryptography.hazmat.primitives import serialization

# Simulated long-term private keys for Alice and Bob as integers
alice_private_key = 12345  # Example private key as an integer
bob_private_key = 54321    # Example private key as an integer

# Generate Alice and Bob's public keys from their long-term private keys
prime = 17  # A prime number for simplicity (replace with a suitable prime)
generator = 2  # A generator for simplicity (replace with a suitable generator)
alice_public_key = pow(generator, alice_private_key, prime)
bob_public_key = pow(generator, bob_private_key, prime)

# Simulate the exchange of public keys over an unsecured channel
# In a real-world scenario, an attacker can intercept or tamper with these keys

# Calculate shared secrets
alice_shared_secret = pow(bob_public_key, alice_private_key, prime)
bob_shared_secret = pow(alice_public_key, bob_private_key, prime)

# Demonstrate the shared secrets
print("Alice's Shared Secret:", alice_shared_secret)
print("Bob's Shared Secret:", bob_shared_secret)

# Suppose an attacker compromises Alice's private key
attacker_compromised_private_key = alice_private_key

# The attacker can now calculate the shared secret of past sessions
attacker_shared_secret = pow(bob_public_key, attacker_compromised_private_key, prime)

# Demonstrate that the attacker can calculate past shared secrets
print("Attacker's Shared Secret (calculated from Alice's compromised private key):", attacker_shared_secret)
