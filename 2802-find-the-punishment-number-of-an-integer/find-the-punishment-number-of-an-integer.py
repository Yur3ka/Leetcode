class Solution:
    def punishmentNumber(self, n: int) -> int:
        def helper(k,s):
            if k == s:
                return True
            elif k < s or s < 0:
                return
            else:
                for j in range(int(math.log10(k))+1):
                    if helper(k%10**j,s-k//10**j):
                        return True
                return False
        ans = 1
        for i in range(2,n+1):
            if helper(i**2,i):
                ans += i**2
        return ans