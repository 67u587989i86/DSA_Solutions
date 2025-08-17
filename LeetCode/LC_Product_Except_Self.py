def productExceptSelf(nums):
    
    answer = [1] * len(nums)

    # Step 1: Fill left product
    left_product = 1
    for i in range(len(nums)):
        answer[i] = left_product
        left_product *= nums[i]
    print(f"After left product: {answer}")

    # Step 2: Multiply with right product
    right_product = 1
    for i in range(len(nums) - 1 , -1 , -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

#  usage:
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]     