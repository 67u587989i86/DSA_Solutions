"""
1
7 2
12 8 3
16 13 9 4
19 17 14 10 5
21 20 18 15 11 6
"""
n = 6

print("1")
for i in range(2,n+1):
    res = []
    
    a = i
    for j in range(i , i*2):
        res.append(str(a))
        res.append(" ")
        a += (n-j+(j-1))
        n-= 1
    
    c = list(reversed(res))
    b = ''.join(c)
    print(b[1:len(b)])
    
    n = 6
        
        
        
    
    
        
            
            
        
