class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = (n+1)*n//2
        if n < m:
            num2 = 0
        else:
            while n%m!=0:
                n-=1
            if n==m:
                num2 = m
            else:
                k = (n-m)//m + 1
                num2 = (n+m)*k//2
        return num1 - 2*num2