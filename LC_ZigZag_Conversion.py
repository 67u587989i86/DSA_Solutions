"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR """

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s  # Special case: straight line

        rows = [[] for _ in range(numRows)]  #(list Comprehensiom) V.V.IMP Create empty rows , 
                                               # create no. of list using loop """
        i = 0

        while i < len(s):
            for down in range(numRows):  # Go down the rows
                if i < len(s):
                    rows[down].append(s[i]) # down = 1,2,3 i.e till numRows value
                    i += 1
            for k in range(numRows - 2, 0, -1):  # Go diagonally dow to up , for up to down iterate forwardly 
                if i < len(s):
                    rows[k].append(s[i])
                    i += 1

        ans = "" 
        for lists in rows:  # rows[0] + rows[0] + .... no. of rows created
            ans += ''.join(lists)
        return ans
    
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3)) #PAHNAPLSIIG
print(sol.convert("AJAYGUPTA", 2)) #AAGPA  -> rows[0]
                                    #JYUT  -> rows[1]  
                                    # #AAGPA + JYUT
