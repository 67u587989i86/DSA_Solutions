def rearrange_alternate_inplace(arr):
    n = len(arr)
    
    # Step 1: Partition negative and positive
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Now, all negative numbers are before index i

    pos = i + 1  # Starting index of positive
    neg = 0      # Starting index of negative

    # Step 2: Swap alternate negatives with next positives
    while pos < n and neg < pos and arr[neg] < 0:
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2  # next alternate position

    return arr




"""

def rearrange_alternate(arr):
    pos = []
    neg = []

    # Separate positive and negative numbers
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    result = []
    i = j = 0

    # Alternate elements from pos and neg
    while i < len(pos) and j < len(neg):
        result.append(neg[j])
        result.append(pos[i])
        i += 1
        j += 1

    # Append remaining elements (if any)
    while j < len(neg):
        result.append(neg[j])
        j += 1

    while i < len(pos):
        result.append(pos[i])
        i += 1

    return result



"""


# Test
arr = [1, 2, -3, -4, 5, -6, 7, -8]
print(rearrange_alternate_inplace(arr))



