# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Soution with division

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [0] * n
        all_prod = 1
        zeroes = 0

        for i in nums:
            if i == 0:
                zeroes = zeroes + 1
            else:
                all_prod = all_prod * i

        for i, num in enumerate(nums):
            if num == 0:
                if zeroes == 1:
                    prod[i] = all_prod
                else:
                    prod[i] = 0
            else:
                if zeroes > 0:
                    prod[i] = 0
                else:
                    prod[i] = int(all_prod / num)


        print(prod)

        return prod

#Soution without division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1] * n
        prod_rev = [1] * n
        zeroes = 0

        for i, num in enumerate(nums):
            if num == 0:
                zeroes = zeroes + 1
            if i == 0:
                prod[i] = num
                prod_rev[n-1] = nums[n-1]
            else:
                prod[i] = prod[i-1] * num
                prod_rev[n-i-1] = prod_rev[n-i] * nums[n-i-1]

        if zeroes > 2:
            return [0] * n
        
        for i, num in enumerate(nums):
            if i == 0:
                prod_rev[i] = prod_rev[i+1]
            elif i == n-1:
                prod_rev[i] = prod[n-2]
            else:
                prod_rev[i] = prod[i-1] * prod_rev[i+1]

        return prod_rev