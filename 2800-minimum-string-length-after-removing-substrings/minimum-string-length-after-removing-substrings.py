class Solution:
    def minLength(self, s: str) -> int:
        stack =[]
        str = ""
        for i in s:
            stack.append(i)
            if len(stack) >= 2:
                str = stack[-2] + stack[-1]
                if str  == "AB" or str == "CD":
                    for j in range(2):
                        stack.pop()
        return len(stack)