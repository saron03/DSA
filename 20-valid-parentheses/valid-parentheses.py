class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if(not stack) and ( i =="]" or i =="}" or i ==")"):
                return False
            if i == "(" or i =="[" or i =="{":
                    stack.append(i)
            else:
                if stack[-1] + i == "()" or stack[-1] + i == "[]" or stack[-1] + i == "{}":
                    stack.pop()
                    continue
                else:
                    return False
        return True if not stack else False

        