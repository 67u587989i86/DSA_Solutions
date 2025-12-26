n = [10,20,30,5,11,50] #wall

for i in range(len(n)-1,-1,-1):
    for j in range(i):
        
        if n[j] > n[j+1]:
            n[j] , n[j+1] = n[j+1] , n[j]
            
print(n)