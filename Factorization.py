def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors.append((divisor, count))
        divisor += 1
    return factors

# user input
n = int(input("Enter an integer for prime factorization: "))
print("Prime factorization:", prime_factorization(n))
