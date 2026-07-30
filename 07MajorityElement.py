# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Our goal is to return the majority element
# We can use a hashmap or dictionary to count the frequency of each element present.
# Iterate over the dictionary to find element with count > n/2

class Solution(object):
    def majorityElement(self,nums):
        # Create a hashmap
        countMap = {}
        n = len(nums)
        
        for num in nums:
            # Update frequency of nums. This is used as a counter to count
            countMap[num] = countMap.get(num,0) + 1
            # Check if this number is already in the majority
            if countMap[num] > n//2:
                return num

# Test Case
sol = Solution()

# Test Case 1 : Standard Case (n = 3, threshold > 1)
nums1 = [3,2,3]
result1 = sol.majorityElement(nums1)
print("Test Case 1 Result:", result1)

# Test Case 2 : Array with multiple elements (n = 7, threshold > 3)
nums2 = [2,2,1,1,1,2,2]
result2 = sol.majorityElement(nums2)
print("Test Case 2 Result:", result2)

# Test Case 3 : Single Element Array (n - 1, threshold > 0)
nums3 = [5]


# Time Complexity : O(n) We iterate through the input list nums of length n exactly once
# Space Complexity : O(n) We are storing the frequency of distinct numbers in CountMap



            