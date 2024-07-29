class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count =  0
        costs.sort()
        for i in costs:
            if i <= coins:
                count +=1
                coins -=i
            
            if i > coins or coins ==0:
                break
        return count
