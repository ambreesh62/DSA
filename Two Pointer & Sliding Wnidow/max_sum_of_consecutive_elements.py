class Solution:
    def __init__(self, array, k) -> None:
        self.array = array
        self.k = k

    def max_sum_of_consecutive_elemeents(self):
        if len(self.array) < self.k:
            return "The length of the array is less then k"
        max_sum = sum(self.array[:self.k])
        current_sum = max_sum
        for i in range (self.k, len(self.array)):
            current_sum = current_sum - self.array[i - self.k] + self.array[i]
            max_sum = max(max_sum, (current_sum))
        return max_sum
        

array = [-1, 2, 3, 3, 4, 5, -1]
k = 4

sol = Solution(array, k)
print(sol.max_sum_of_consecutive_elemeents())