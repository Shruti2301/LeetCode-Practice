class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[0]

        # Move slow pointer one step and fast pointer two steps until they meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Return the duplicate element
        return slow

# Time Complexity: O(n)
# Space Complexity: O(1)
