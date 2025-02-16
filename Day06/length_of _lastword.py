#  Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def length_of_lastword(self, s: str) -> int:
        i, length = len(s) -1, 0
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
    
# Example Usage 
obj = Solution()

print(obj.length_of_lastword("Hello World"))      #  Output 5