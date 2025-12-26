n = [7,1,5,4,6,3]
buy = n[0]
profit = 0

for i in range(1,len(n)):
    if n[i]<buy:
        buy = n[i]
        
    if n[i] - buy > profit:
        profit = n[i] - buy
        
print(profit)
        

            
    
    

