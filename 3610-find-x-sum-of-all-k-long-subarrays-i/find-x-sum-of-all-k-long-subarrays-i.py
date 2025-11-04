class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(arr,x):
            c = Counter(arr)
            fr = [(v,k) for k,v in c.items()]
            res = 0
            fr.sort(reverse=True)
            i = 0 
            while i <x and i < len(fr):
                res += fr[i][0]*fr[i][1]
                i += 1
            return res
        ans = []
        for i in range(len(nums)-k+1):
            ans.append(x_sum(nums[i:i+k],x))
        return ans
