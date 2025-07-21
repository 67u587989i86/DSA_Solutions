def isValid(s):
    stack = []
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if ch == ')' and top != '(':
                return False
            if ch == '}' and top != '{':
                return False
            if ch == ']' and top != '[':
                return False
    return True if not stack else False   # return not stack     directly we can write like this for bydefault true if brackets is balanced and stack became empty

s = "({[]})"
print(isValid(s))  # Output: True


"""
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

"""