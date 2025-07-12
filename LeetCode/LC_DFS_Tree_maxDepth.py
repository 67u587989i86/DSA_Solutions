class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # If the tree is empty, depth is 0
        if root is None:
            return 0

        # BFS uses Queue for its implementation
        queue = [root] 
        count = 0  

        #  Working of BFS , how it exactly works ,
        #  how it goes to another level only after completing the first

        while queue:             #level starts
            count += 1  

            
            for _ in range(len(queue)):
                node = queue.pop(0)  # Dequeue the first level to append next level

            # Enqueue left and right children if they exist , both can also enque if present
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # if both exist len Queue become 2 coz appends both, loop runs twice , pop will happen 
        # twice and append their left or right then loop break queue is still present
                # so count +1
        
        return count
