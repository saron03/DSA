class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []  
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:  
                if stack[-1] < -ast:  
                    stack.pop()
                    continue
                elif stack[-1] == -ast:  
                    stack.pop()
                    break
                else:  
                    break
            else:
                stack.append(ast)

        return stack