class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        def single(x):
            sum = 0
            for i in str(x):
                sum += int(i) 
            if len(str(sum)) == 1:
                    return sum
            else:
                num = sum
                return single(num)

        return single(num)
