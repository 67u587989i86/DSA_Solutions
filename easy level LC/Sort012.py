def sortColors(nums):
    low = 0        # pointer for 0 storing
    cur = 0        # pointer for current
    high = len(nums) - 1  # pointer for 2 storing

    while cur <= high:       

        if nums[cur] == 0:          # append to front by replacing with low
            nums[low], nums[cur] = nums[cur], nums[low]
            low += 1
            cur += 1
        elif nums[cur] == 1:      # leave 1 as it is and move forward
            cur += 1
        else:  # nums[cur] == 2  append to last by replacing with cur
            nums[cur], nums[high] = nums[high], nums[cur]
            high -= 1
        # print(nums) Debugging line to see the state of nums after each operation

nums = [2, 0, 2, 1 , 0 , 1]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

#"When it reaches 1, all elements before it must have already become 0."
 