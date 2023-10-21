# Cryptography
Interesting Material

pip install cryptography
#################################################################
RSA_decrpytion.py output:

Given values:
N = 7081
e = 275
ciphertext (c) = 3
Calculating phi(N):
phi(N) = (p - 1) * (q - 1) = (73 - 1) * (97 - 1) = 6912
Calculating private key (d) using Extended Euclidean Algorithm:
Initial values: a = 275, b = 6912
x0 = 1, x1 = 0
Private key (d) = 1307
Decrypting the ciphertext:
plaintext = c^d mod N = 3^1307 mod 7081 = 122
Process finished with exit code 0
#################################################################
