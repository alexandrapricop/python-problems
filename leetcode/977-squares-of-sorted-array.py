# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
    

# Another solution but it doesn't overwrite the input

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return_array = [v**2 for v in A]
        return_array.sort() 
        return return_array