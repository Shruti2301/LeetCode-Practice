Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        count = 0
        for char in s:
            if char in char_set:
                char_set.remove(char)
                count += 2
            else:
                char_set.add(char)
        return count + 1 if len(char_set) > 0 else count
