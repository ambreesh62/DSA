# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climb_stairs(self, n: int) -> int:
        dict = {}

        def climb(n):
            if dict.get(n, -1) != -1:
                return dict[n]
            if n < 2:
                return 1
            else:
                result = climb(n - 1) + climb(n - 2)
                dict[n] = result
                return result

        return climb(n)


x = Solution()
print(x.climb_stairs(2))  # Output: 2
