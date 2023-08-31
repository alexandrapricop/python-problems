#Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_length = 0
        for c in range(len(s)-1, -1, -1):
            if s[c] != " ":
                last_length = last_length + 1
            else:
                if last_length > 0:
                    return last_length
        
        return last_length
    

# Another solution, better runtime, worse memory

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])