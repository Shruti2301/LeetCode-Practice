class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in nums:
            if(i != 0):
                nums[j] = i
                j += 1
        for i in range(j,n):
            nums[i] = 0
