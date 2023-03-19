# Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Check if the number of unique characters in the strings are equal
        if len(set(s)) != len(set(t)):
            return False
        
        # Check if the mapping between characters is unique
        char_map = {}
        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = t[i]
            elif char_map[s[i]] != t[i]:
                return False
        return True
