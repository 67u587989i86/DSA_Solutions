def permute(nums):
    result = []

    def backtrack(arr):
        if len(arr) == len(nums):           # ✅ base condition: full permutation
            result.append(arr.copy())           # store a copy
            return

        for i in nums:                       # try each number
            if i not in arr:                # 🚫 skip if already used
                arr.append(i)               # ➕ add number to current arr
                backtrack(arr)              # 🔁 recurse with updated arr
                arr.pop()                   # ↩️ undo: remove last added (backtrack)

    backtrack([])                            # start with empty path
    return result


nums = [1, 2, 3]
print(permute(nums))  
