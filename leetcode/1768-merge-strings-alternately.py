# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        word3 = ""
        len1 = len(word1)
        len2 = len(word2)

        for i in range(0, min(len1, len2)):
            word3 = word3 + word1[i] + word2[i]

        if(len1 > len2):
            for i in range(len2, len1):
                word3 = word3 + word1[i]
        else:
            for i in range(len1, len2):
                word3 = word3 + word2[i]

        return word3
    
#improved version

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        min_len = min(len1, len2)

        merged = [None] * (len1 + len2)

        for i in range(min_len):
            merged[2 * i] = word1[i]
            merged[2 * i + 1] = word2[i]

        if len1 > len2:
            merged[min_len * 2:] = word1[min_len:]
        else:
            merged[min_len * 2:] = word2[min_len:]

        return ''.join(merged)
