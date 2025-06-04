class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if not stack or n > 0:
                stack.append(n)
            elif n * stack[-1] > 0:
                stack.append(n)
            else:
                insert = False
                while stack and n < 0 and stack[-1] > 0:
                    if abs(stack[-1]) > abs(n):
                        insert = False
                        break
                    elif abs(stack[-1]) == abs(n):
                        stack.pop()
                        insert = False
                        break
                    else:
                        stack.pop()
                        insert = True
                if insert:
                    stack.append(n)
        return stack
                
