# nums = [1, 2, 3, 4]

# def backtrack(nums, i):
#     backtrack1 = 1
#     for j in range(i, 0, -1):
#         backtrack1 *= nums[j]
#     return backtrack1

# def Fronttrack(nums, i):
#     Ftrack1 = 1
#     for k in range(i, len(nums)):
#         Ftrack1 *= nums[k]
#     return Ftrack1

# for i in range(1, len(nums) - 1):
#     fronttrack = Fronttrack(nums, i)
#     back = backtrack(nums, i)
#     result = fronttrack * back
#     print(f"Index {i}: Front = {fronttrack}, Back = {back}, Product = {result}")
#O(n**2)


# Optimized code is below O(n) , prefix and suffix method


def productExceptSelf(nums):
    
    output = [1] * len(nums)

    # Step 1: Prefix products , left to right leaving starting index
    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]

    # Step 2: Suffix products , right to left leaving end index
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output

# Example
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]



