class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ans[stack[-1]] = i- stack[-1]
                stack.pop()
            stack.append(i)
        return ans
