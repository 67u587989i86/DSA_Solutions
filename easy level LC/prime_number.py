def is_prime(n):   #lets n = 29
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):  #√29 ≈ 5.38 → int(√n) + 1 → loop from 2 to 6 (i.e. 2, 3, 4, 5)
        if n % i == 0:           # 29 % 2 , 3 , 4 , 5
            return False
    return True

print(is_prime(79))