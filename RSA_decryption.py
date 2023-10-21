import math

# Given values
p = 73
q = 97
e = 275
c = 3

# Calculate N
N = p * q

# Calculate phi(N)
phi_N = (p - 1) * (q - 1)

# Calculate d using Extended Euclidean Algorithm
a = e
b = phi_N

# Extended Euclidean Algorithm
x0 = 1
x1 = 0
while b != 0:
    quotient = a // b
    a, b = b, a % b
    x0, x1 = x1, x0 - quotient * x1

# Ensure d is positive
if x0 < 0:
    x0 = x0 + phi_N

d = x0

# Decrypt the ciphertext
plaintext = pow(c, d, N)

# Print all the results
print("Given values:")
print(f"N = {N}")
print(f"e = {e}")
print(f"ciphertext (c) = {c}")
print()

print("Calculating phi(N):")
print(f"phi(N) = (p - 1) * (q - 1) = ({p} - 1) * ({q} - 1) = {phi_N}")
print()

print("Calculating private key (d) using Extended Euclidean Algorithm:")
print(f"Initial values: a = {e}, b = {phi_N}")
print(f"x0 = 1, x1 = 0")
while b != 0:
    quotient = a // b
    a, b = b, a % b
    x0, x1 = x1, x0 - quotient * x1
    print(f"a = {a}, b = {b}, x0 = {x0}, x1 = {x1}")
if x0 < 0:
    x0 = x0 + phi_N
print(f"Private key (d) = {d}")
print()

print("Decrypting the ciphertext:")
print(f"plaintext = c^d mod N = {c}^{d} mod {N} = {plaintext}")
