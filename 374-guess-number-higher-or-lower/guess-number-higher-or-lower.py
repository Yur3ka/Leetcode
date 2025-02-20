# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def helper(left,right):
            mid = (left + right) // 2
            rs = guess(mid)
            if rs == 0:
                return mid
            elif rs == -1:
                return helper(left,mid-1)
            else:
                return helper(mid+1,right)
        return helper(1,n)