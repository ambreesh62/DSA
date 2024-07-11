# Q. Add Binary
# Given two binary strings a and b, return their sum as a binary string.


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        binary = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            binary = char + binary
            carry = total // 2

        if carry:
            binary = "1" + binary
        return binary
