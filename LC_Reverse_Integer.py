class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1    # Determine the sign
        x = abs(x)                   # Work with the absolute value
        
        reversed_num = 0
        
        while x != 0:
            remainder = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + remainder
        
        reversed_num *= sign         # Apply the sign
        
        # Check for 32-bit overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num

# Create an instance of the Solution class
solution = Solution()

# Call the reverse method with any number and print the output
print(solution.reverse(-123))   # Example with -123
print(solution.reverse(1534236469))   # Example with a large number
print(solution.reverse(120))    # Example with 120
print(solution.reverse(0))      # Example with 0
