# You are given a string s, which contains stars *.
# In one operation, you can:
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

class Solution:
    def removeStars(self, s: str) -> str:
        t = ""
        n = len(s) - 1
        k = 0

        for i in range(n, -1, -1):
            if s[i] == '*':
                k = k + 1
            else:
                if k > 0:
                    k -= 1
                else:
                    t = t + s[i]
        
        return t[::-1]


# with array/stack

class Solution:
    def removeStars(self, s: str) -> str:
        t = []
        n = len(s) - 1
        k = 0

        for i in range(n, -1, -1):
            if s[i] == '*':
                k = k + 1
            else:
                if k > 0:
                    k -= 1
                else:
                    t.append(s[i])

        return ''.join(t[::-1])
