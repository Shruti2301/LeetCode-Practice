class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        len1 = len(word1)
        len2 = len(word2)

        # Iterate until the length of the smallest word
        for i in range(min(len1, len2)):
            # Add element of word1
            res += word1[i]
            # Add element of word2
            res += word2[i]

        if len1 > len2:
            res += word1[len2: ]
        
     
        if len1 < len2:
            res += word2[len1: ]
    

        return res
