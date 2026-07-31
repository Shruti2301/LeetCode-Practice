# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# 
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# We need to rotate the array to the right by k steps.
# Right rotation means, the last k elements of the array move to the front and remaining elements shift to the right.
# If value of k is greater than array length n, rotating more than n times repeats the same pattern.
# We can reduce k by (k = k % n)
#
# How to reverse?
# Instead of rotating one step at a time (slow pointer), we will reverse using 3 reversals.
# 1. Reverse the entire array : Brings the last elements to the front, but in reverse order.
# 2. Reverse the first k elements : This puts the rotated part in correct order.
# 3. Reverse the remaining (n - k) elements : fixes the order of the remaining elements.
#
# Reversing the whole array moves the elements to the correct side
# Reversing parts moves it in correct order. There is no extra space needed or new array.
# After 3 reversals, array becomes rotated to right by k steps.

class Solution(object):
    def rotate(self, nums, k):
        # Get the length of the array
        n = len(nums)
        
        # If k is greater than n, reduce it using modulo.
        # Rotating n times will give the same array.
        k = k % n
        
        def reverse(left, right):
            # Swap elements until two pointers meet
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1
                right = right - 1
        
        # Reverse the entire array
        reverse(0,n-1)
        # Reverse the first k elements
        reverse(0,k-1)
        # Reverse the remaining n-k elements
        reverse(k,n-1)

sol = Solution()

# Test Case 1 : Standard Case (k < n)
nums1 = [1,2,3,4,5,6,7]
k1 = 3
sol.rotate(nums1,k1)
print('Test Case 1 Result:', nums1)

# Test Case 2 : k > n (k = 3 for length 4 --> effective rotation is k % 4 = 3)
nums2 = [-1,-100,3,99]
k2 = 2
sol.rotate(nums2,k2)
print('Test Case 2 Result',nums2)

# Test Case 3 : k is a multiple of n (effective rotation k % n = 0, no net change)
nums3 = [1,2,3]
k3 = 3
sol.rotate(nums3,k3)
print('Test Case 3 Result:', nums3)
        
# Consider nums = [1,2,3,4,5,6,7] and k = 3
# Think of the array split into two blocks:
# - Block A (First n - k elements) : [1,2,3,4]
# - Block B (Last k elements) : [5,6,7]

# Our target order after right rotation is [Block B, Block A] -> [5,6,7,1,2,3,4]

# Step 1 : Reverse the entire array ( 0 to n - 1)
# Before : [1,2,3,4 | 5,6,7]
# After : [7,6,5 |4,3,2,1]
# Block B is now at the front, Block A is at the back
# But, both individual blocks are reversed ([7,6,5] and [4,3,2,1])

# Step 2 : Reverse the first k elements ( o to k - 1)
# Before : [7,6,5 | 4,3,2,1]
# After : [5,6,7 | 4,3,2,1]
# This restores the correct order of elements inside Block B

# Step 3 : Reverse the remaining n-k elements (k to n-1)
# Before : [5,6,7 | 4,3,2,1]
# After : [5,6,7 | 1,2,3,4]
# This restores the correct order of elements inside Block B

# Time Complexity : O(n) - Every element is swapped twice across 3 reversal steps
# Space Complexity : O(1) - All modifications are performed in place without any extra additional data structures.
