arr1 = [1, 2, 1, 2,2,1,2]


char = arr1[0]
cnt = 1
for nums in arr1:
    if nums == char:
        cnt +=1
    else:
        cnt -= 1
        if cnt == 0:
            char = nums
            
print(nums)

            

