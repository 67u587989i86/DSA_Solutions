"""
3[a]2[bc]

output = aaabcbc
  """  
  
s = "3[a]2[bc]"
# s = "3[a2[c]]"
i = 0
finalres = ""
while i < len(s):
    res = ""
    if s[i] == "[" :
        num = int(s[i-1])
        i += 1
        while s[i] != "]":
            res += (s[i])
            i += 1
        finalres += num * res
        i += 1
    i += 1  
print(finalres)        
    
        
            
            
        
