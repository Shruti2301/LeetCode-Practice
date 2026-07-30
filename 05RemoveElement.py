# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# We are given nums array and a value, we need to remove all instances of value from nums array.
# We will use a Two Pointer Approach (Slow and Fast Pointer) - remove all occurences of a value in place

# We use a Two Pointer Technique (Slow-Fast/ Reader - Writer):
# 'index' (slow pointer) : Tracks where to write the next valid element (also serves as the valid count)
# 'j' (fast pointer) : Scans through every element in the array

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0 # Write

        # We then iterate through the elements
        for j in range(len(nums)): # j scans every element
        # If the current element is NOT the value we want to remove
            if nums[j] != val: 
                nums[index] = nums[j] # Overwrite/keep it at the front write position
                index = index + 1 # Move write position forward
        
        # 'index' now represents both the length of the valid prefix
        # and the total count of elements not equal to 'val'
        return index

sol = Solution()

# Test Case 1
nums1 = [3,2,2,3]
val1 = 3
k1 = sol.removeElement(nums1,val1)
print(f"Test Case 1: k = {k1}, Valid Prefix = {nums1[:k1]}")

# Test Case 2
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
k2 = sol.removeElement(nums2,val2)
print(f"Test Case 2: k = {k2}, Valid Prefix = {nums2[:k2]}")

# Test Case 3
nums3 = [7,7,7]
val3 = 7
k3 = sol.removeElement(nums3, val3)
print(f"Test Case 3: k = {k3}, Valid Prefix = {nums3[:k3]}")

# Time Complexity : O(n) - single pass through the array of length n
# Space Complexity : O(1) - modified in place without any extra data structure
