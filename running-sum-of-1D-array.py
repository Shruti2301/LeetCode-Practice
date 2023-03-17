#Running Sum of 1D Array - Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        runningSum = []

        for i in nums:
            sums += i
            runningSum.append(sums)
        return runningSum
