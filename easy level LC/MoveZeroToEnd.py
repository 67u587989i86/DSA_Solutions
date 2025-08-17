def moveZeroes(nums):
    non_zero = 0     #slow pointer

    for i in range(len(nums)):   #fast pointer i
        if nums[i] != 0:
            nums[non_zero], nums[i] = nums[i], nums[non_zero]
            non_zero += 1
    return nums
print(moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]