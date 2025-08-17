""""Return true if you can make
 a string palindrome by removing at
   most one character."""

"""
Input:  "abca"
Output: True   # Remove 'b' or 'c' → "aba" or "aca"

Input:  "racecar"
Output: True   # Already a palindrome

Input:  "abc"
Output: False  # Cannot form palindrome even after 1 deletion
"""

s = "abca"

def is_palindrome_range(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping either character
            return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
        left += 1
        right -= 1

    return True

# Test it
print(valid_palindrome(s))  # Output: True
