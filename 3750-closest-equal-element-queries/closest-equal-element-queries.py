class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        location = defaultdict(list)
        n = len(nums)
        for i in range(len(nums)):
            location[nums[i]].append(i)
        # print(location)
        res = []
        for index in queries:
            value = nums[index]
            curr = bisect.bisect_left(location[value],index)
            ans = float("inf")
            l = 0
            r = 0
            left = curr - 1
            right = curr + 1
            if left > -1:
                distance = abs(location[value][left]-index)
                l = min(distance, n-distance)
            elif len(location[value]) > 1:
                distance = abs(location[value][-1]-index)
                l = min(distance, n-distance)
            if right < len(location[value]):
                distance = abs(location[value][right]-index)
                r = min(distance, n-distance)
            elif len(location[value]) > 1:
                distance = abs(location[value][0]-index)
                r = min(distance, n-distance)
            # print(left,l,right,r)
            if l:
                ans = min(ans,l)
            if r:
                ans = min(ans,r)
            if ans != float(inf):
                res.append(ans)
            else:
                res.append(-1)
        return res

# [-1,5,2,4,1,1,-1,-1,1,1,2,8]
            