class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subLength = float('-inf')
        indexLeft = 0
        sub = ""
        for i in range(len(s)):
            while(s[i] in sub):
                subLength = max(subLength, len(sub))
                sub =sub[1:]
                indexLeft +=1 
            sub += s[i]

        subLength = max(subLength, len(sub))
        return subLength if subLength != float('inf') else 0

