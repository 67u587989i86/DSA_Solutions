def longestPalindrome(s):
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length
        odd = expandAroundCenter(i, i)
        # Even length
        even = expandAroundCenter(i, i + 1)
        
        # Update longest
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even

    return longest
# Example usage
print(longestPalindrome("babad"))  # Output: "bab" or "aba"