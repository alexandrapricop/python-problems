# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = n - 1 #nums2
        i = m - 1 #nums1
        k = m + n - 1

        # Fill the nums1 from behind by putting the biggest item on the last position
        while j >=0 and i>=0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]     
                i -= 1
            k -= 1

        k = k+1

        # If elements remained in nums2, add them at the begining of nums1
        if j >= 0:
            if k==0:
                nums1[0] = nums2[0]
            else:
                for i in range(k):
                    nums1[i] = nums2[i]
                    j -= 1


