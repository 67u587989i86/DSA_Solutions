data = [8, 8, 7, 3, 4, 5, 7, 7, 8, 3, 8, 2, 1, 4, 6]  #output - [8, 7, 3, 4, 1, 2, 5, 6]

#sort based on frequency and then by value if frequency is same , tuple sorting

# Step 1: Count frequency
freq = {}
for num in data:
    freq[num] = freq.get(num, 0) + 1 #if num is not present then it add num with value 0 & add 1 to it
                                      #if num present it will simply add 1

# Output: {8: 4, 7: 3, 3: 2, 4: 2, 5: 1, 2: 1, 1: 1, 6: 1}


# Step 2: Remove duplicates         bcoz output should not have duplicates
unique_elements = list(freq.keys())
# Output: [8, 7, 3, 4, 5, 2, 1, 6]



# Step 3: Sort by frequency (descending), then by value (ascending)
sorted_unique = sorted(unique_elements, key=lambda x: (-freq[x], x))   #This is called Tuple sorting 
# (a,b) → a is frequency and b is value ,  first sortby a & if a is same it starts sorting by b.
# [(-5, 8), (-3, 7), (-2, 3), (-2, 4), (-1, 1), (-1, 2), (-1, 5), (-1, 6)]
 

print(sorted_unique)
