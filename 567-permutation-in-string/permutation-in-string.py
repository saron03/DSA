class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        dic1 = {}
        for char in s1:
            if char in dic1:
                dic1[char] += 1
            else:
                dic1[char] = 1

        dic2 = {}
        for char in s2[:m]:
            if char in dic2:
                dic2[char] += 1
            else:
                dic2[char] = 1
        if dic1 == dic2:
            return True

        for i in range(1, n-m+1 ):

            new_char = s2[i+m-1]
            if new_char in dic2:
                dic2[new_char] += 1
            else:
                dic2[new_char] = 1

           
            old_char = s2[i - 1]
            if dic2[old_char] == 1:
                del dic2[old_char]
            else:
                dic2[old_char] -= 1

            
            if dic1 == dic2:
                return True

        return False