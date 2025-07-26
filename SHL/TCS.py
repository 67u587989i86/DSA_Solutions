def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def digit_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def special_prime_product(n):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                break
        num += 1
    prime = num
    root = digit_root(prime)
    return prime * root

# Test
print(special_prime_product(10))  # Output: 58
print(special_prime_product(6))  # Output: 52
