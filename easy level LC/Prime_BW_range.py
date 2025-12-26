def isprime(n):
    
    if n == 0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
            break
    return True
    
for i in range(1,50):
    if i == 1:  #1 is not a prime number
        continue
    if isprime(i) == True:
        print(i)