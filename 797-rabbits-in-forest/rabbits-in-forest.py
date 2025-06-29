class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic1 = defaultdict(int)
        count = 0
        for i in answers:
            if i ==0:
                count ==1
            
            dic1[i] +=1
            if dic1[i] == i +1:
                count += i +1
                dic1[i] = 0
        for i in dic1:
            if dic1[i] >0:
                count += i+1
        return count
