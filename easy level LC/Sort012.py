def sortColors(nums):
    low = 0        # pointer for 0 storing
    mid = 0        # pointer for current
    high = len(nums) - 1  # pointer for 2 storing

    while mid <= high:       
        if nums[mid] == 0:          # append to front
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:      # leave 1 as it is
            mid += 1
        else:  # nums[mid] == 2  append to last
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        # print(nums) Debugging line to see the state of nums after each operation

nums = [2, 0, 2, 1 , 0 , 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

#"When it reaches 1, all elements before it must have already become 0."
 