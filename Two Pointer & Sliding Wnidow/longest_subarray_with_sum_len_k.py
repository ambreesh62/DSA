# Longest subarray with sum <= k
#Ex: s = [2, 5, 1, 7, 10], k = 14

class Solution:
    def __init__(self, array: int) -> None:
        self.array = array

    def optimal(self, k: int):
        max_length = 0
        current_sum = 0
        start = 0

        for end in range(len(self.array)):
            current_sum += self.array[end]

            # Shrink the window until the current_sum is <= k
            while current_sum > k and start <= end:
                current_sum -= self.array[start]
                start += 1

            # Update the max_length if the current window is valid
            if current_sum <= k:
                max_length = max(max_length, end - start + 1)

        return max_length        
    
s = [2, 5, 1, 7, 10]
k = 14

obj = Solution(s)
print(obj.optimal(k))     