class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        count = 1
        for i in range(1,len(num)):
            if num[i] != num[i-1]:
                count = 1
            else:
                count += 1
                if count >= 3:
                    ans = max(ans,num[i]*3)
        return ans