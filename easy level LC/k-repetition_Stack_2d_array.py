def remove_k_adjacent(string: str, k: int) -> str:
    stack = []  # each element: [char, count]         top = [-1]
                            #    [0]    [1]
    
    for char in string:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1          # same char → count++
            if stack[-1][1] == k:      # exactly k → delete group
                stack.pop()
        else:
            stack.append([char, 1])       # new char starts

    # Build final answer
    return ''.join(char * cnt for char, cnt in stack)
print(remove_k_adjacent("abbcccbbaaa", 3))



#perfect use of stack and 2d array