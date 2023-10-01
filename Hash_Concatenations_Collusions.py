import hashlib

# Input values
a = "Hello"
b = "World"

# Method 1: H(a||b) - Concatenate and then hash
concatenated_input = a + b
hash_method_1 = hashlib.sha256(concatenated_input.encode()).hexdigest()

# Method 2: H(a, b) - Hash independently
hash_method_2 = hashlib.sha256(a.encode() + b.encode()).hexdigest()

# Print the input values
print("Input value a:", a)
print("Input value b:", b)

# Print the hash results
print("\nMethod 1 (H(a||b)):")
print("Concatenated input:", concatenated_input)
print("Hash result:", hash_method_1)

print("\nMethod 2 (H(a, b)):")
print("Hash result:", hash_method_2)

# Check if the hash values are equal
if hash_method_1 == hash_method_2:
    print("\nBoth methods produce the same hash.")
else:
    print("\nMethods produce different hashes.")

# Security implications explanation
print("\nSecurity Implications:")
print("- Method 1 (H(a||b)): In this method, values are concatenated before hashing.")
print("  - Security: It depends on the security of the concatenation operation.")
print("  - Vulnerabilities: Possible issues with concatenation may lead to security vulnerabilities (e.g., length extension attacks).")
print("  - Collision Resistance: Concatenation may introduce additional collision opportunities if not handled correctly.")

print("\n- Method 2 (H(a, b)): In this method, values are hashed independently.")
print("  - Security: Generally considered more secure as it doesn't rely on concatenation.")
print("  - Vulnerabilities: Less vulnerable to attacks related to concatenation and doesn't leak information about the input structure.")
print("  - Collision Resistance: Hashing independently enhances collision resistance as the hash of each input is computed separately.")

print("\nCollision Resistance:")
print("- Collision resistance refers to the property of a hash function where it is computationally infeasible to find two different inputs that produce the same hash value.")
print("- Method 2 tends to have better collision resistance because it avoids concatenation vulnerabilities.")
