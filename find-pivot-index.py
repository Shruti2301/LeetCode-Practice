# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array. 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Initialize the leftSum to zero and the rightSum to the sum of all elements in the array
        leftSum, rightSum = 0, sum(nums)
        
        # Iterate through each element of the array using the enumerate() function
        for idx, ele in enumerate(nums):
            # Subtract the current element from the rightSum to calculate the sum of all elements to the right of the current index
            rightSum -= ele
            
            # If the leftSum is equal to the rightSum, return the current index as the pivot index
            if leftSum == rightSum:
                return idx
            
            # Add the current element to the leftSum to calculate the sum of all elements to the left of the current index
            leftSum += ele
        
        # If there is no pivot index, return -1
        return -1
