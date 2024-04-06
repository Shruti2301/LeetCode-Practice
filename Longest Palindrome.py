class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s == s[::-1]: return s

        length = len(s)-1
        center_left, center_right = 0, 0
        longest_palindrome = s[0]

        while center_right < length:
            while center_right < length:
                if s[center_right] != s[center_right + 1]: break
                center_right += 1
            left, right = center_left, center_right

            while left > 0 and right < length:
                if s[left - 1] != s[right + 1]: break
                left -= 1
                right += 1

            if len(longest_palindrome) < right + 1 - left:
                longest_palindrome = s[left:right+1]

            center_right += 1
            center_left = center_right

        return longest_palindrome
