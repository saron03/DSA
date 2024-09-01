class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = "aeiouAEIOU"
        count = 0
        for i in s[:k]:
            if i in vow:
                count +=1
        max_vow = count
        for i in range(k,len(s)):
            if s[i - k] in vow:
                count -= 1
            if s[i] in vow:
                count += 1
            max_vow = max(max_vow, count)
        return max_vow


