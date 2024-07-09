# Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is an empty string, return 0
        if needle == "":
            return 0

        # Get the lengths of haystack and needle
        len_haystack = len(haystack)
        len_needle = len(needle)

        # Traverse through the haystack
        for i in range(len_haystack - len_needle + 1):
            # Check if the substring from the current index matches the needle
            if haystack[i : i + len_needle] == needle:
                return i

        # If needle is not found, return -1
        return -1


def main():
    param_1 = "hello"
    param_2 = "ll"
    ret = Solution().strStr(param_1, param_2)
    print(ret)  # Output should be 2

    param_1 = "aaaaa"
    param_2 = "bba"
    ret = Solution().strStr(param_1, param_2)
    print(ret)  # Output should be -1


if __name__ == "__main__":
    main()
