# -----------------------------------------------------------
# Original array (you can change this to any valid permutation)
# Example given by you: a = [0, 2, 1, 3]
# Another example      : a = [3, 2, 1, 0]   # a[0] = 3, so after
#                                            #           change, a[3] = 0
# -----------------------------------------------------------
a = [0, 2, 1, 3]          # each value < len(a)

# -----------------------------------------------------------
# Step 1: Create a new list to store the transformed values
# -----------------------------------------------------------
n = len(a)

new_a = [0] * n           # same length, all zeros for now

# -----------------------------------------------------------
# Step 2: Invert the mapping
#         For every index i, value = a[i]
#         Place i at position 'value' in new_a
# -----------------------------------------------------------
for i in range(n):
              # what was stored at index i
    new_a[a[i]] = i      # put i at index = that value

# -----------------------------------------------------------
# Step 3: Copy the result back into a (optional)
# -----------------------------------------------------------
# a = new_a

# -----------------------------------------------------------
# Step 4: Display the final array
# -----------------------------------------------------------
print("Transformed array:", new_a)
