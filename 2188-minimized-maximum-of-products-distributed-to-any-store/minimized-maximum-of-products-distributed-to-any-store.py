class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        quantities.sort()
        ans = 0
        l = 1
        r = quantities[-1]
        def can_split(arr,num,quan):
            count = 0
            # temp = arr[:]
            for i in range(len(arr)):
                count += ceil(arr[i]/quan)
            # print(count,quan)
            return count <= num
        while l <= r:
            m = (l+r)//2
            if can_split(quantities,n,m):
            # print(k)
                ans = m
                r = m-1
            else:
                l = m + 1
        return ans