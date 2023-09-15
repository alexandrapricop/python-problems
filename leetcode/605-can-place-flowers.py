#You have a long flowerbed in which some of the plots are planted, and some are not. 
#However, flowers cannot be planted in adjacent plots.
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
#and an integer n, return true if n new flowers can be planted in the flowerbed without violating 
#the no-adjacent-flowers rule and false otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        lgt = len(flowerbed)

        if n == 0:
            return True

        if lgt == 1 and flowerbed[0] == 0:
            return True
        elif lgt == 1:
            return False

        for i, plot in enumerate(flowerbed):
            if plot == 0:
                if i == 0 and flowerbed[i+1] == 0:
                    count = count + 1
                    flowerbed[i] = 1
                elif i == lgt - 1 and flowerbed[i-1] == 0:
                    count = count + 1
                    flowerbed[i] = 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count = count + 1
                    flowerbed[i] = 1

        if n <= count:
            return True
        else:
            return False