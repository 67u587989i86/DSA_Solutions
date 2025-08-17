n = 5 # Number of chocolates 
k = 2 # for every k wrapper you get a new chocolate

chocolates = n
wrappers = n

while wrappers >= k:
    new_chocolates = wrappers // k
    chocolates += new_chocolates
    wrappers = (wrappers % k) + new_chocolates

print(chocolates)  # Output: 9
