def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


# Example usage

print(isPowerOfTwo(1))  # Output: True (2^0)
print(isPowerOfTwo(2))  # Output: True (2^1)
print(isPowerOfTwo(3))  # Output: False
print(isPowerOfTwo(4))  # Output: True (2^2)
print(isPowerOfTwo(5))  # Output: False
print(isPowerOfTwo(16)) # Output: True (2^4)
print(isPowerOfTwo(18)) # Output: False



"""
1   →  0001
2   →  0010
4   →  0100
8   →  1000
"""


"""
n     :  0100   (4)
n - 1 :  0011   (3)
--------------------
&     :  0000   (0)




n     :  0110   (6)
n - 1 :  0101   (5)
--------------------
&     :  0100   (4)  ≠ 0 → Not a power of 2




   100000   (32)
&  011111   (31)
  --------
   000000   (0 in decimal)


"""