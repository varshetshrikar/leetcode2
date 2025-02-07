class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Negative numbers are not palindromes
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x //= 10  # Integer division

        return original == reversed_num
