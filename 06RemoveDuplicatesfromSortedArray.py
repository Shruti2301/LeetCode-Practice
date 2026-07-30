# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. 
# After removing duplicates, return the number of unique elements k. The first k elements of nums should contain the unique numbers in sorted order. 
# The remaining elements beyond index k - 1 can be ignored.

# We are given a sorted array nums in non-decreasing order. Our goal is to remove duplicates in place (no new array). 
# After removal, each unique element appears only once, first k elements of array should hold unique numbers.
# Rest of the array can be ignored. We need to return k, the number of unique elements.

# The array is already sorted, all duplicate values are grouped together side by side.
# We maintain a prefix of unique elements at the front using two pointers
# i --> Slow Pointer + Write Position : Points to the last known unique element placed at the front of the array
# j --> Fast Pointer + Reader Position : Scans forward through the array from index 1 to len(nums) - 1

class Solution(object):
    def removeDuplicates(self, nums: list[int]) -> int:
        # If there are no elements in array, return 0
        if not nums:
            return 0
    
        # Let i be the index of last element found (unique)
        i = 0
    
        # Start Fast Pointer j from 1 and go through the array
        for j in range(1, len(nums)):
            # Check if current element is different from last unique element
            # As j iterates through the array, we compare nums[j] against nums[i]
            # If nums[j] == nums[i], it is a duplicate - we ignore it and move j forward
            # If nums[j] != nums[i], we found a new unique value
            # --> Increment i ( i = i + 1) to point to the next write slot
            # --> Copy the new value over (nums[i] = nums[j])
        
            if nums[j] != nums[i]:
                # Move the unique index forward
                i = i + 1
                # Place the new unique element at i 
                nums[i] = nums[j]
            
        # Return the number of unique elements as i is 0-indexed
        return i + 1

sol = Solution()

# Test Case 1
nums1 = [1,1,2]
k1 = sol.removeDuplicates(nums1)
print(f"Test Case 1: k = {k1}, Unique Prefix = {nums1[:k1]}")

# Test Case 2
nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = sol.removeDuplicates(nums2)
print(f"Test Case 2: k = {k2}, Unique Prefix = {nums2[:k2]}")

# Test Case 3
nums3 = [5,5,5,5]
k3 = sol.removeDuplicates(nums3)
print(f"Test Case 3: k = {k3}, Unique Prefix = {nums3[:k3]}")

# Time Complexity : O(n) - single pass through the array
# Space Complexity : O(1) - modified in-place with zero extra memory allocations