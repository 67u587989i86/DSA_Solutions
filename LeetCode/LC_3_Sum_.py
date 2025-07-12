from typing import List

""" Question: Implement 3Sum using three pointers (i, pointer1, pointer2)
 Find all unique triplets in the array which gives the sum of zero."""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the input list to make it easier to avoid duplicates and use two pointers
        
        result = []  # Initialize an empty list to store the resulting triplets
        
        for i in range(len(nums)):  # Iterate over each number in the sorted list with index i
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for i to avoid duplicate triplets
                continue  # Move to the next iteration if current number is the same as previous
            
            pointer1 = i + 1  # Initialize pointer1 to the element just after i
            pointer2 = len(nums) - 1  # Initialize pointer2 to the last element of the list
            
            while pointer1 < pointer2:  # Loop until the two pointers meet
                
                total = nums[i] + nums[pointer1] + nums[pointer2]  # Calculate sum of the three numbers
                
                if total == 0:  # If the sum is zero, we found a valid triplet
                    result.append([nums[i], nums[pointer1], nums[pointer2]])  # Add it to the results
                    
                    # Skip duplicates for pointer1 to avoid repeating triplets
                    while pointer1 < pointer2 and nums[pointer1] == nums[pointer1 + 1]:
                        pointer1 += 1
                        
                    # Skip duplicates for pointer2 to avoid repeating triplets
                    while pointer1 < pointer2 and nums[pointer2] == nums[pointer2 - 1]:
                        pointer2 -= 1
                        
                    pointer1 += 1  # Move pointer1 forward to continue searching
                    pointer2 -= 1  # Move pointer2 backward to continue searching
                
                elif total < 0:  # If sum is less than zero, move pointer1 forward to increase sum
                    pointer1 += 1
                
                else:  # If sum is greater than zero, move pointer2 backward to decrease sum
                    pointer2 -= 1
        
        return result  # Return the list of all unique triplets that sum to zero

print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) # instance dirrectly created and calls function , goot for single call

sol = Solution()

print(sol.threeSum([-1, 0, 1, 2, -1, -4])) # good for multiple calls