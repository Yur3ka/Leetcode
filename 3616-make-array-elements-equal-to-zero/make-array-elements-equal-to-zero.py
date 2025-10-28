class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            temp = nums[:]
            curr = i
            dx = 1
            while curr >= 0 and curr < len(nums):
                if temp[curr] > 0:
                    temp[curr] -= 1
                    dx *= -1
                    curr += dx
                else:
                    curr += dx
            # print(i,temp,'right')
            if sum(temp) == 0:
                ans += 1
            temp = nums[:]
            curr = i
            dx = -1
            while curr >= 0 and curr < len(nums):
                if temp[curr] > 0:
                    temp[curr] -= 1
                    dx *= -1
                    curr += dx
                else:
                    curr += dx
            # print(i,temp,'left')
            if sum(temp) == 0:
                ans += 1
        return ans