# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, subsequence: str, sequence: str) -> bool:
        # Base case
        if not subsequence:
            return True
        
        # Initialize pointers for the subsequence and sequence
        subseq_pointer = 0
        seq_pointer = 0
        
        # Traverse elements of the sequence
        while seq_pointer < len(sequence):
            # If this character matches the character in the subsequence, increment subsequence pointer
            if sequence[seq_pointer] == subsequence[subseq_pointer]:
                subseq_pointer += 1
            # If the subsequence pointer is equal to the length of the subsequence, we have found a match and can exit the loop
            if subseq_pointer == len(subsequence):
                return True
            seq_pointer += 1
        
        # If we haven't found a match by the end of the sequence, the subsequence is not a valid subsequence of the sequence
        return False
 
