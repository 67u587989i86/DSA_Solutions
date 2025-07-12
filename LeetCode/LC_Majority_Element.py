n = [1,2,2,2,3,1,4,2,2,2]  #len of n is 7 , n/2(majority element) should be more than n/2 (3.5)
                            # question has condition that always a majority element present

count = 0
element = None 

for i in range(len(n)):
    if count == 0:
        element = n[i]
    if n[i] == element:
        count += 1
    else: 
        count -= 1

print(element)
