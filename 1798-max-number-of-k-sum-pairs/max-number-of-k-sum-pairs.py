class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic1={}
        count = 0
        for i in nums:
            dic1[i] = dic1.get(i, 0) + 1
        for i in nums:
            num = k - i
            if num in dic1 and dic1[num] >=1 and dic1[i] >=1:
                if i == num:
                    if dic1[i] >= 2:
                        dic1[i] -= 2 
                        count += 1
                else:
                    dic1[num] -= 1
                    dic1[i] -=1
                    count +=1
        return count
            


                

