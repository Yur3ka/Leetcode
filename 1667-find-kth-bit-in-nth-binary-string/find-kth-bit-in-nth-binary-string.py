class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = [0]
        for i in range(1,n+1):
            ans.append(1)
            temp = []
            for bit in range(len(ans)-2,-1,-1):
                temp.append(1-ans[bit])
            ans.extend(temp)
        # print(ans)
        return str(ans[k-1])