"""
Input: s = "barfoothefoobarman", words = ["foo","bar"]
#           0--------9
Output: [0, 9]
"""


def findSubstring(s, words):
    from collections import Counter

    result = []

    total_len = len(words[0]) * len(words)

    word_count = Counter(words)

    
    # Try every possible offset within a word length
    for i in range(len(words[0])):
        left = i
        right = i
        window_count = Counter()
        
        words_used = 0

        while right + len(words[0]) <= len(s):
            word = s[right:right + len(words[0])]
            right += len(words[0])
            if word in word_count:
                window_count[word] += 1
                words_used += 1
                # If we have too many of one word, shrink from the left
                while window_count[word] > word_count[word]:
                    left_word = s[left:left + len(words[0])]
                    window_count[left_word] -= 1
                    words_used -= 1
                    left += len(words[0])
                # If window is valid
                if words_used == len(words):
                    result.append(left)

            else:
                # Reset window
                window_count.clear()
                words_used = 0
                left = right

    return result


s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words))
# Output: [6, 9, 12]


print(findSubstring("barfoothefoobarman", ["foo","bar"]))
# Output: [0, 9]
