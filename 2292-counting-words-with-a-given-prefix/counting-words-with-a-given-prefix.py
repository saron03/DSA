class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in words:
            str=""
            k = 0
            while k < len(pref) and k < len(i):
                str += i[k]
                k +=1
            if str == pref:
                count +=1
        return count