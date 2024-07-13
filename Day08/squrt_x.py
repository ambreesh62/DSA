# 69. Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


class Solution:
    def my_sqrt(self, x: int) -> int:
        if x < 0:
            raise ValueError("x must be non-negative")

        if x == 0 or x == 1:
            return x

        left, rigth = 0, x
        result = 0

        while left <= rigth:
            mid = (left + rigth) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                result = mid
            else:
                rigth = mid - 1

        return result


# Example
obj = Solution()
x = 4

print(obj.my_sqrt(x))  # output 2