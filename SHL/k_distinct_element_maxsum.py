# Sample Input


# 11
# 2
# 1
# 2
# 2
# 3
# 2
# 3
# 5
# 1
# 2
# 1
# 1

#  Output  - 12
   
#  Here, N = 11, k = 2
#  A = [1, 2, 2, 3, 2, 3, 5, 1, 2, 1, 1]
#  We can select the subarray = [2, 2, 3, 2, 3]
#  It is a good subarray because it contains at most k 
# distinct elements.
#  Its sum = 2+2+3+2+3 = 12
#  So, our answer is 12.

n = int(input())        # Number of elements
k = int(input())        # distinct elements
A = [int(input()) for _ in range(n)] #list building through input

left = 0
curr_sum = 0
max_sum = 0
count = {}              # Regular dictionary

for i in range(n):
    
    # Increase count of current element
    if A[i] in count:
        count[A[i]] += 1
    else:
        count[A[i]] = 1

    curr_sum += A[i]

    # If distinct elements > k, shrink window
    while len(count) > k:  # count = {3: 1, 2: 1, 5: 1} 
                           # len(count) = 3 → violates the k = 2 rule!
        rem_val = A[left]
        curr_sum -= rem_val
        count[rem_val] -= 1

        if count[rem_val] == 0:   # {3: 0, 2: 1, 5: 1}
            del count[rem_val]    # now: {2: 1, 5: 1}

        left += 1

    # Update max sum
    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
