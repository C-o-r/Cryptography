def prime_factors(n):
    factors = []
    # Divide the number by 2 to remove all even factors
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # After this loop, n becomes odd
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors

def euler_totient(n):
    factors = prime_factors(n)
    result = n  # Initialize result as the input number
    for factor in set(factors):
        result -= result // factor
    return result

# Input a number to calculate Euler's Totient function for
num = int(input("Enter a number: "))
phi = euler_totient(num)
print(f"Euler's Totient function (φ) for {num} is {phi}")
