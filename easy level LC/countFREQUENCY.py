n = [1,2,3,4,4,3,2,5,6,7,6,7,8,9,9,9,9]

m = {}

for i in range(len(n)):
    if n[i] not in m.keys():
        m[n[i]] = 1
    else:
        m[n[i]] += 1
for z in m:           
    print(f"the {z} occurs {m[z]} times")