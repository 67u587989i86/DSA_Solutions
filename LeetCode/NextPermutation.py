n = [1, 4, 3, 2]

i = len(n) - 2 

while i>= 0 and n[i] >= n[i+1]:
    i-=1
    
if i < 0:
    print("No permutation")
else:
    j = len(n)-1
    
    while n[j] <= n[i]:
        j-=1
        
    n[i],n[j] = n[j],n[i]
    
    n[i+1:] = reversed(n[i+1:])
    
    print(n)