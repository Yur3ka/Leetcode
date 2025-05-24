class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        change = []
        n = len(nums)
        pos = 0
        s_pos = 0
        neg = 10000000000
        for i in range(n):
            curr = (k^nums[i]) - nums[i]
            print(nums[i],k^nums[i], curr)
            if curr >= 0:
                pos += 1
                change.append(curr)
            else: 
                if abs(curr) < abs(neg):
                    neg = curr
        change.sort()    
        s = sum(nums)
        print(s)
        if pos %2 == 0:
            return s + sum(change)
        else:
            if abs(neg) > change[0]:
                return s + sum(change[1:])
            else:
                return s + neg + sum(change)