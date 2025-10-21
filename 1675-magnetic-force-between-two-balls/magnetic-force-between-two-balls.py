class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_put(arr,num,dis):
            count = 1
            last = arr[0]
            for i in range(1,len(arr)):
                if arr[i]-last >= dis:
                    count +=1
                    last = arr[i]
                if count == num:
                    return True
            return False
        ans = 0
        position.sort()
        l = 1
        r = position[-1]
        while l <= r:
            mid = (l+r)//2
            if can_put(position,m,mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans