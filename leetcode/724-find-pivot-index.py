#Given an array of integers nums, calculate the pivot index of this array.
#The pivot index is the index where the sum of all the numbers strictly to the left of the index 
#is equal to the sum of all the numbers strictly to the index's right.
#If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
#This also applies to the right edge of the array.
#Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_prefix = []
        sum_reversed = []
        n = len(nums)
        index = -1

        for i in range(0, n):
            if i == 0:
                sum_prefix.append(nums[i])
                sum_reversed.append(nums[n-1-i])
            else:
                sum_prefix.append(sum_prefix[i-1] + nums[i])
                sum_reversed.append(sum_reversed[i-1] + nums[n-1-i])

        for i in range(0, n-2):
            print(i+1)
            if(sum_prefix[i] == sum_reversed[n-1-i-2]):
                index = i+1
                break
        
        if n > 1:
            if sum_reversed[n-2] == 0:
                index = 0
            
        if index == -1 and n > 1:
            if sum_prefix[n-2] == 0:
                index = n-1
        
        if n == 1:
            index = 0

        return index