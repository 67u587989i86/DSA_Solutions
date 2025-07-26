arr = [4, 5, 2, 25]    #last element result always -1
n = len(arr)
result = [-1] * n
stack = []     #always maintain stack in decreasing order

for i in range(n - 1, -1, -1):
    while stack and arr[i] >= stack[-1]: #1 check if top is smaller
        stack.pop()
    if stack:
        result[i] = stack[-1] #2 append greater element to result
    stack.append(arr[i])   #3 push arr[i] element to stack

print("Input:", arr)
print("Next Greater Elements:", result)
