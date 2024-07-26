# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1

        while left < right:
            while left < right and not self.alpha_num(s[left]):
                left += 1
            while right > left and not self.alpha_num(s[right]):
                right -= 1    
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right-1
        return True    

    def alpha_num(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))
    
sol = Solution()
x = "A man, a plan, a canal: Panama"
w = "rracca"

print(sol.is_palindrome(x))
print(sol.is_palindrome(w))