from typing import List  # Importing List type hint for better readability and type checking

class Solution:  
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # Defining the twoSum method
        mapA = {}  # Initialize an empty dictionary to map numbers to their indices
        
        # Loop through the list 'nums' with both index (i) and value (K)
        for i, K in enumerate(nums):
            diff = target - K  # Calculate the number we need to complete the target sum
            
            # Check if diff is already in the dictionary
            if diff in mapA:
                # If found, return the pair of indices [index of diff, current index]
                return [mapA[diff], i]
            
            # If not found, store the current number and its index in the dictionary
            mapA[K] = i
        
        # If no pair sums to the target, return an empty list (this line is optional based on problem constraints)
        return []
    
sol = Solution()

print(sol.twoSum([1,2,3,4,5,6,7,8] , 8))
