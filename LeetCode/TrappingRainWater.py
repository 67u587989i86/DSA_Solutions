class Solution(object):
    def trap(self, height):
        
        a = 0
        z = len(height)-1   #two pointers
        
        total = 0
        
        maxa = 0            #max storage
        maxz = 0
        
        while a <= z:       
            if height[z] <= height[a]:              #smaller is always safe to proceed
                if height[z] >= maxz:
                    maxz = height[z]
                else:
                    total += maxz - height[z]

                z -=1
            else:       
                if height[a] >= maxa:
                    maxa = height[a]
                else:
                    total += maxa - height[a]
                a += 1

        return total
                
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
                
            



        