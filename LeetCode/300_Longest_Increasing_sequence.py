import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tails = []

        for element in nums:
            i = bisect.bisect_left(tails, element)
            if i == len(tails):
                tails.append(element)
            else:
                tails[i] = element
        return len(tails)

print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))  # Output: 3