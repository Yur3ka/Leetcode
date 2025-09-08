class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        num1 = 0
        num2 = 0
        level = 0
        while n > 0:
            extra = 0
            last_digit = n %10
            if last_digit == 0:
                num1 = num1 + 5* 10**level
                num2 = num2 + 5* 10**level
                extra = 1
            elif last_digit == 1 and n>9:
                num1 = num1 + 5*10**level
                num2 = num2 + 6*10**level
                extra = 1
            else:
                num1 = num1 + (last_digit//2) * 10**level
                num2 = num2 + (last_digit - last_digit//2)* 10**level
            n = n//10 - extra
            level +=1
        return [num1,num2]