class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        peak = 0
        past_peak = 0
        up = True
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return False
            if up == True:
                if nums[i] < nums[i-1]:
                    if i-past_peak == 1 and past_peak ==0:
                        return False
                    else:
                        up = False
                        past_peak = i
                        peak += 1
            else:
                if nums[i] > nums[i-1]:
                    
                    up = True
                    past_peak = i
                    peak += 1
        return peak ==2
            
        