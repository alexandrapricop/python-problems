# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        zero = 0
        for i in range(n, -1, -1):
            if nums[i] == 0:
                del nums[i]
                zero = zero + 1

        for i in range(0,zero):
            nums.append(0)
