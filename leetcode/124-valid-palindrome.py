# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i].isalpha() or s[i].isdigit():
                if s[j].isalpha() or s[j].isdigit():
                    if s[i].casefold() != s[j].casefold():
                        return False
                    else:
                        i = i+1
                        j = j-1
                else:                        
                    j = j-1
            else:
                i = i + 1

        return True   
        