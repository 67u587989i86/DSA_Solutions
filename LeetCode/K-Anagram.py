from collections import Counter

s1 = "anagram"  #how many characters to change in s1 to make it equal to s2
s2 = "grammar"  #change s1 to s2
k = 2

if len(s1) != len(s2):
    print("Not K-anagrams")
else:
    
    
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    print(count1)
    print(count2)

    diff = 0
    for char in count1:
        if count1[char] > count2.get(char, 0):   # 0 means default value if char not in count2
            diff += count1[char] - count2.get(char, 0)

    if diff <= k:
        print("K-anagrams")
    else:
        print("Not K-anagrams")
