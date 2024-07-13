# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climb_stairs(self, n: int) -> int:
        d = {}

        def fun(n):
            if d.get(n, -1) != -1:
                return d[n]
            if n < 2:
                return 1
            else:
                s = fun(n - 1) + fun(n - 2)
                d[n] = s
                return s

        return fun(n)


x = Solution()
print(x.climb_stairs(2))
