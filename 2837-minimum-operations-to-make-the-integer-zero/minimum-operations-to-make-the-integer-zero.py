class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        for i in range(1,61):
            if num1-i*num2 < i:
                return -1
            cnt = bin(num1-i*num2).count("1")
            if cnt <= i:
                return i
        return -1