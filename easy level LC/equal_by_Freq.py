arr1 = [1, 2, 3, 2,2]
arr2 = [2, 1, 2, 3,2]

Flag = True


if len(arr1) != len(arr1):
    Flag = False
    
if Flag:
    m = {}
    for i in range(len(arr1)):
        if arr1[i] in m:
            m[arr1[i]] += 1
        else:
            m[arr1[i]] = 1
            
    for nums in arr2:
        
        if nums in m:
            m[nums] -= 1
            if m[nums] < 0:
                Flag = False
        else:
            Flag = False
            
print(Flag)
            

