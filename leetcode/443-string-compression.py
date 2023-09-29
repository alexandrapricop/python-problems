# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

class Solution:
    def compress(self, chars: List[str]) -> int:
        c = chars[0]
        amount = 0
        n = len(chars)
        j = 0

        for i in range(n):
            if chars[i] == c :
                amount += +1
            else:
                chars[j] = c
                j += 1
                if amount > 1:
                    if amount < 9:
                        chars[j] = str(amount)
                        j += 1
                    else: 
                        nr_numbers = []
                        while amount > 0:
                            nr_numbers.append(str(amount%10))
                            amount = int(amount / 10)
                        nr_numbers.reverse()
                        for k in range(len(nr_numbers)):
                            chars[j] = nr_numbers[k]
                            j += 1

                amount = 1
                c = chars[i]
        

        chars[j] = c
        j += 1
        if amount > 1:
            nr_numbers = []
            while amount > 0:
                nr_numbers.append(str(amount%10))
                amount = int(amount / 10)
            nr_numbers.reverse()
            for k in range(len(nr_numbers)):
                chars[j] = nr_numbers[k]
                j += 1

        nr_numbers = []

        print(chars)

        return j


