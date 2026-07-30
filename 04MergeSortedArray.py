# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# We are given two array nums1 and nums2, sorted in non-decreasing order, 
# m = valid elements in nums1 and n = valid elements in nums2
# Array nums1 has length m + n , with last n positions filled with 0s for merging.
# We want to merge elements from both the arrays into nums1, without using any space.
# We can take advantage of 0s at the end of nums1 and merge arrays from right to left.
# We can compare the largest remaining elements from both the arrays and place the largest of both
# in last position in nums1. The process of backward movement continues till all nums2 elements are placed in nums1.

# The core concept is Reverse In Place Merging
# In this problem. we are required to modify nums1 in-place (without allocating a new array). 
# If we start filing nums1 from index 0, we will overwrite elements in nums1 that have not been compared yet.

# nums1 has enough empty space (filled with zeros) at the very back to fit all elements of nums2
# By comparing elements from largest to smallest (back to front)
# 1. We compare the largest remaining numbers from nums1 and nums2.
# 2. We write the larger number to the very end of nums1
# 3. We move backwards towards index 0

class Solution(object):
    def merge(self, nums1, m, nums2, n):
            # Pointer for last index of merged arrays
            write = m + n - 1
            
            # Merge from the end in nums1, only continue if nums1 has elements in it.
            # Loop as long as there are still elements left to place from nums2
            while n > 0: 
                # If nums1 still has elements and current element is bigger than nums2, compare its last unplaced elemnt (nums1[m-1]) against nums2's last unplaced elemnt (nums2[n-1])
                if m > 0 and nums1[n-1] > nums2[n-1]:
                    nums1[write] = nums1[m-1] # Place the larger nums1 element in write position at the back
                    m = m - 1 # Put pointer in nums1 backwards (Shift nums1 read pointer left)
                    
                else:
                    nums1[write] = nums2[n - 1] # Place nums2 element in the write position
                    n = n - 1 # Move pointer in nums2 backward (Shift nums2 read pointer left)
                
                write = write - 1  # Move write pointer left for the next iteration


sol = Solution()

# Test Case 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol.merge(nums1, m, nums2, n)
print(" Test Case 1 Result:", nums1)

# Test Case 2
nums1_b = [0]
m_b = 0
nums2_b = [1]
n_b = 1

sol.merge(nums1_b, m_b, nums2_b, n_b)
print(" Test Case 2 Result:", nums1_b)
