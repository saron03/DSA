class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        x = sorted(strs)
        first = x[0]
        last = x[-1]
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        
        return result
