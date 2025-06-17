class Solution(object):
    def myAtoi(self, s):
        # Step 1: Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0 # otherwise s[0] will give out of index if s won't remain anything after stripping
                     # or empty string passed
                     
        # Step 2: Determine the sign
        sign = 1        #default if not get - or plus in 0th index
        index = 0       #if not any sign means pointer is already at integer
        if s[0] == '-':     # if got minus index will move forward to integer 
            sign = -1
            index += 1
            
        elif s[0] == '+':  #bymistakely if user give +231 it will handle it and
            index += 1     # put pointer forward to int 

        # Step 3: Convert digits
        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result *= sign

        # Step 4: Clamp to 32-bit signed integer range

        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1

        return result

sol = Solution()

print(sol.myAtoi("-321"))
print(sol.myAtoi("00045"))
print(sol.myAtoi("    -1234"))
print(sol.myAtoi("-098"))
print(sol.myAtoi("+1123"))
print(sol.myAtoi("   "))
print(sol.myAtoi(""))