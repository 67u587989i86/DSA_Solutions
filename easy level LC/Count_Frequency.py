a = [1, 3, 2, 1, 4, 1, 3]

m = {}

for i in range(len(a)):
    
    if a[i] in m:
        m[a[i]] += 1
    else:
        m[a[i]] = 1
        
final = None
cnt = 0
for num in m:
    if m[num] > cnt:
        cnt = m[num]
        final = num
print(final)
    