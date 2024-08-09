class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        n = len(num)
        count = 0
        if int(num) % int(num[:k]) == 0:
            count +=1
        for i in range(1, len(num)-k+1):
            if int(num[i:k+i]) != 0 and int(num) % int(num[i:k+i]) == 0:
                count +=1
        return count