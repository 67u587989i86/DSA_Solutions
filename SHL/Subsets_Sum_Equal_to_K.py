def find_subsets_with_sum_k(arr, k):
    result = []         # Subsets where sum == k
    failed = []         # Subsets that were valid paths but didn't sum to k
    all_subsets = []    # Every subset considered

    def backtrack(index, current, total):
        if index == len(arr):
            all_subsets.append(current.copy())  # Add to all subsets
            if total == k:
                result.append(current.copy())   # Valid subset
            else:
                failed.append(current.copy())   # Invalid (but complete) subset
            return

        # Include arr[index]
        current.append(arr[index])
        backtrack(index + 1, current, total + arr[index])

        # Exclude arr[index]
        current.pop()
        backtrack(index + 1, current, total)

    backtrack(0, [], 0)
    return result, failed, all_subsets






arr = [1, 2, 3]
k = 3

valid_subsets, failed_subsets, all_subsets = find_subsets_with_sum_k(arr, k)

print("✅ Subsets with sum =", k)
for s in valid_subsets:
    print(s)

print("\n❌ Subsets without sum =", k)
for s in failed_subsets:
    print(s)

print("\n📋 All subsets:")
for s in all_subsets:
    print(s)
