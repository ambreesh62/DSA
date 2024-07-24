# Pascal's Triangle II
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        
        row = [1]
        
        for i in range(1, rowIndex + 1):
            # Start the new row with 1
            new_row = [1]
            # Generate the in-between elements by summing up the pairs from the previous row
            for j in range(1, i):
                new_row.append(row[j - 1] + row[j])
            # End the new row with 1
            new_row.append(1)
            # Update row to the new row
            row = new_row
        
        return row

# Example 
solution = Solution()
rowIndex = 8
print(solution.getRow(rowIndex)) 

        