class Solution(object):
    def removeOccurrences(self, s, part):
        stack= []
        for i in s:
            stack.append(i)
            if len(stack) >= len(part):
                if ''.join(stack[-len(part):]) == part:
                    del stack[-(len(part)):]
        return ''.join(stack)