class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = []
        last = 0
        for i in range(len(nums)):
            if not ans:
                last = nums[i]-k
                ans.append(nums[i]-k)
            else:
                temp = max(nums[i]-k,last + 1)
                if temp > nums[i] + k:
                    continue
                else:
                    last = temp
                    ans.append(last)
        return len(ans)