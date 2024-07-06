class Soluation:
    def is_palindrome(self, x: int) -> bool:
        # Convert the integer to a string
        num = str(x)
        # Reverse the string and compare with the original
        return num == num[::-1]


soluation = Soluation()

print(soluation.is_palindrome(121))
print(soluation.is_palindrome(-121))
print(soluation.is_palindrome(10))
