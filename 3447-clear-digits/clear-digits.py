class Solution(object):
    def clearDigits(self, s):
        stack = []
        for i in s:
            if not i.isdigit():
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
