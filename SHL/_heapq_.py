import heapq            #note - smallest is always root node bcoz heapq only works with min heap
                        
list1 = [5, 3, 8, 1, 2]


heapq.heapify(list1)  # Convert to a heap    [1, 2, 8, 3, 5]       

heapq.heappush(list1, 0)     # Add a new element    [0, 2, 1, 3, 5, 8]

heapq.heappop(list1)    # Remove the smallest element     [0]

heapq.heappushpop(list1, 4)      # Push(4) then pop(smallest) in one go   

heapq.heapreplace(list1, 6)  # Pop(smallest) then push(6) 


# Top 3 largest/smallest
print("3 largest:", heapq.nlargest(3, list1))
print("3 smallest:", heapq.nsmallest(3, list1))



nums = [5, 1, 9, 3, 7]


# Convert to max-heap by pushing negative values

max_heap = [-x for x in nums]
heapq.heapify(max_heap)

# Output: [-9, -5, -7, -3, -1]
#just convert the final answer you need after using same methods by multiplying with -1 or directly -nums[i]