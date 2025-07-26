"""
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Explanation:
- [1,3] and [2,6] overlap, so merge into [1,6].
- [8,10] and [15,18] do not overlap, so keep them.

"""

def merge(intervals):
    if not intervals:
        return []

    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])  #sort by the first element of each list in intervals
    
    merged = [intervals[0]]             # Initialize merged list with the first interval

    # Step 2: Traverse and merge
    for curr in intervals[1:]:
        last = merged[-1]
        if curr[0] <= last[1]:  # overlap
            last[1] = max(last[1], curr[1])
        else:
            merged.append(curr)

    return merged



print(merge( [ [1, 3], [2, 6], [8, 10], [15, 18] ] ))  # Output: [[1, 6], [8, 10], [15, 18]]