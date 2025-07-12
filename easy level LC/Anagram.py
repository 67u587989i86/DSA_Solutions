def isAnagram(s: str, t: str) -> bool:

# def isAnagram(s, t): this will also work


    return sorted(s) == sorted(t)


# examples
print(isAnagram("listen", "silent"))   # ➜ True
print(isAnagram("triangle", "integral"))  # ➜ True
print(isAnagram("hello", "world"))     # ➜ False
