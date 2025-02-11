class Solution(object):
    def removeOccurrences(self, s, part):
        stack= []
        for i in s:
            stack.append(i)
            if len(stack) >= len(part):
                if ''.join(stack[-len(part):]) == part:
                    j = 0
                    while j < len(part):
                        stack.pop()
                        j+=1
        return ''.join(stack)