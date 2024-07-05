class Solution:
    def two_sum(self, nums, target):
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

solution = Solution()

print(solution.two_sum([2, 7, 11, 15], 9))  
print(solution.two_sum([3, 2, 4], 6))      
print(solution.two_sum([3, 3], 6))        
