def formatted_string(s):
    result = []
    i = 0  
    group_sizes = [1, 2, 3, 3, 2, 1]  #declare pattern
    j = 0  #index for group_sizes

    while i < len(s):
        size = group_sizes[j]
        result.append(s[i:i+size])
        i += size
        j = (j + 1) % len(group_sizes)  #cycle the pattern to keep repeating it

    return ' '.join(result)

# Example usage
print(formatted_string("abcdefghijklm"))  # Output: "a bc def ghi jk l m"
