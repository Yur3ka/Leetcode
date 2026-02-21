class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        p = [2,3,5,7,11,13,17,19,23,29,31]
        prime = set(p)
        ans = 0
        for i in range(left,right+1):
            if str(bin(i)).count('1') in prime:
                ans += 1
        return ans