class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        c = defaultdict(list)
        temp = 0
        for n in nums:
            temp += n
            if n %3==1:
                c[1].append(n)
            elif n % 3 == 2:
                c[2].append(n)
        if temp %3==0:
            return temp
        elif temp %3==1:
            if len(c[1]) > 0:
                ans= max(ans,temp-c[1][0])
            if len(c[2]) > 1:
                ans = max(ans, temp-c[2][0]-c[2][1])
        else:
            if len(c[2]) > 0:
                ans= max(ans,temp-c[2][0])
            if len(c[1]) > 1:
                ans = max(ans, temp-c[1][0]-c[1][1])
        return ans