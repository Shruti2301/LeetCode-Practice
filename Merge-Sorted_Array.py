# July 7 - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place, so that nums1 becomes a single sorted array.
        """
        # If nums2 is empty, there's nothing to merge, return immediately
        if n == 0:
            return
        
        # Replace the last n elements of nums1 with all elements of nums2
        nums1[-n:] = nums2
        
        # Sort the entire nums1 to ensure it is a single sorted array
        nums1.sort()

        # Time Complexity: O((m + n) log(m + n)) due to the sort operation
        # Space Complexity: O(1) as the merge is done in-place without using extra space
