# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # Check if the list is empty
            return ""

        current = strs[0]  # Start with the first string as the current prefix

        for i in range(1, len(strs)):  # Iterate through the remaining strings
            while strs[i].find(current) != 0:  # Reduce current prefix until it matches
                current = current[:-1]
                if not current:
                    return ""

        return current


obj = Solution()

print(obj.longestCommonPrefix(["dog", "racecar", "car"]))  # Output ""
print(obj.longestCommonPrefix(["flower", "flow", "flight"]))  # Output "fl"
