class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        left=0
        right = ones
        score = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                left +=1
            else:
                right -=1
            sum = left + right
            score = max(sum,score)
        return score
