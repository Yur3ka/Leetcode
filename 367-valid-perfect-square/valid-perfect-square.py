class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        e = num
        while s <= e:
            m = (s+e)//2
            if m*m == num:
                return True
            elif m*m < num:
                s = m+1
            else:
                e = m-1
        return False