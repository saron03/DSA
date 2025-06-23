class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        for i in bills:
            if i ==5:
                count5 +=1
            if i == 10:
                if count5 == 0:
                    return False
                count10 +=1
                if count5 >0: 
                    count5 -=1
                else:
                    return False
            if i == 20:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count5 -= 3
                else:
                    return False
        return True

            