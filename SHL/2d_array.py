# -----------------------------------------------------------
# 2‑D list for the sample data (m = 3 days, n = 4 sales each)
# -----------------------------------------------------------
sales = [
    [221, 333, 190, 452],
    [102, 199, 590, 100],
    [350, 399, 450,  99]
]                               #output -> 452 590 450 

# -----------------------------------------------------------
# Find the maximum sale of every day
# -----------------------------------------------------------
max_each_day = []                     # list to store each day's max

for day in sales:                     # outer loop → one row (day)
    largest = day[0]                  # start with first value
    for amount in day:                # inner loop → each sale
        if amount > largest:          # update if bigger
            largest = amount
    max_each_day.append(largest)      # store result for this row

# -----------------------------------------------------------
# Print the results in one line
# -----------------------------------------------------------
for value in max_each_day:
    print(value, end=' ')
