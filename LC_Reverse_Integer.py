"""
Given a signed 32-bit integer x, return x with its digits reversed. 
 If reversing x causes the value to go outside the s
 igned 32-bit integer range [-231, 231 - 1], then return 0. """

class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0

        while x != 0:
            digit = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + digit

        reversed_num *= sign

        # Check for 32-bit integer overflow
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num
    
    # Create an instance of Solution and call reverse you cant do print(reverse(123) directly in a class)
sol = Solution()
print(sol.reverse(123))     # Output: 321
print(sol.reverse(-456))    # Output: -654
print(sol.reverse(1534236469))  # Output: 0 (overflow)
