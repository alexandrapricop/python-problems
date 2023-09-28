# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        n = len(nums)

        if n == 1:
            return nums[0]

        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum

        for i in range(k, n):
            current_sum = current_sum - nums[i - k] + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum / k
