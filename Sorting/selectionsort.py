n = [3,5,6,1,2,9,7,22,66,32,14,12]  #three pointer


for i in range(len(n)):
    min1 = i
    for j in range(i,len(n)):
        
        if n[j] < n[min1]:
            min1 = j
            
    n[i] , n[min1] = n[min1] , n[i]
            
print(n)
    