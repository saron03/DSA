class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        limit = len(p)
        if limit > len(s):
            return [] 
        dic1= {}
        for i in p:
            if i in dic1:
                dic1[i] +=1
            else:
                dic1[i] = 1

        dic2= {}
        for char in s[:limit]:
            if char in dic2:
                dic2[char] += 1
            else:
                dic2[char] = 1
        res = []
        if dic1 == dic2:
            res.append(0)

        for j in range(1, len(s) - limit + 1):
            outgoing = s[j - 1]
            if dic2[outgoing] == 1:
                del dic2[outgoing]
            else:
                dic2[outgoing] -= 1

            incoming = s[j + limit - 1]
            if incoming in dic2:
                dic2[incoming] += 1
            else:
                dic2[incoming] = 1
            if dic1 == dic2:
                res.append(j)
        return res
                    
            


