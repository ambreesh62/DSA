#  Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        value1, value2, value = m - 1, n - 1, m + n - 1

        while value1 >= 0 and value2 >= 0:
            if nums1[value1] > nums2[value2]:
                nums1[value] = nums1[value1]
                value1 -= 1
            else:
                nums1[value] = nums2[value2]
                value2 -= 1
            value -= 1

        while value2 >= 0:
            nums1[value] = nums2[value2]
            value2 -= 1
            value -= 1    

        
        
        
 # Example 
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output  [1, 2, 2, 3, 5, 6]