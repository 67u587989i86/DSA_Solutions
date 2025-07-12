from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []         # Final result list to store all subsets
        subset = []      # Temporary list for the current subset being built

        def dfs(i):
            # Base case: if we have considered all elements
            if i >= len(nums):   #index 3 which not in list
                res.append(subset.copy())  # Add a snapshot of current subset
                return

            # ---- Choice 1: Include nums[i] in the subset ----
            subset.append(nums[i])
            dfs(i + 1)                     # Move to the next element

            # ---- Backtrack: remove nums[i] and try without it ----
            subset.pop()
            dfs(i + 1)                     # Try next without including nums[i]

        dfs(0)  # Start from index 0
        return res

sol = Solution()
print(sol.subsets([1, 2, 3]))
