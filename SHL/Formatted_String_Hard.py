def formatted_string(s):
    result = []
    pointer1 = 0
    pointer2 = 1  # Start with pointer2 length 1
    while pointer1 < len(s):
        result.append(s[pointer1:pointer1+pointer2])
        pointer1 += pointer2
        pointer2 = pointer2 + 1 if pointer2 < 3 else 1  # Loop pattern 1, 2, 3
    return ' '.join(result)

# Example usage
print(formatted_string("abcdefghijklm"))  # Output: "a bc def g hi jkl m"

"""
[0:0+1(1)]  I : I + J   and 
            J += 1 unitil J == 3 else J = 1
[1:1+2(3)]  I = I + J

[3:3+3(6)]

[6:6+1(7)]

[7:7+2(9)]

[9:9+3(12)]



"""