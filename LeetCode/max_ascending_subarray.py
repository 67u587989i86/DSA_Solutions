n = [10,20,30,5,10,50]

sum1 = n[0]
max1 = 0
for i in range(1,len(n)):
    if n[i] > n[i-1]:
        sum1+= n[i]
        if sum1 > max1:
            max1 = sum1
    else:
        sum1= n[i]
        
print(max1)