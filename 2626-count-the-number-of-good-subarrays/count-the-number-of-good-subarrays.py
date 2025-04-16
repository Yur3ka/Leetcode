class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        temp = 0
        start = 0
        current = defaultdict(int)
        for i in range(n):
            current[nums[i]] += 1
            temp += (current[nums[i]]-1)
                
            while temp >= k and start < i:
                ans += n - i
                current[nums[start]] -= 1
                temp -= (current[nums[start]])
                # print(i,temp,start)
                start += 1
        return ans