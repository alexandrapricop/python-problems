# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        return nums[n//2]

        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i in range(n):
           if nums[i] == nums[i + int(n/2)]:
            return nums[i]

# Moore's Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = 0
        count = 0

        for i in nums:
            if count == 0:
                cand = i
            if cand == i:
                count += 1
            else:
                count -= 1


        return cand

        

        
        

