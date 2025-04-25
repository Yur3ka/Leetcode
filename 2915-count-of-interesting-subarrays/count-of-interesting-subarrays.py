class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        pos = [0]
        for num in nums:
            temp = 0
            if num % modulo == k:
                temp = 1
            pos.append(pos[-1]+temp)
        ans = 0
        count = defaultdict(int)
        for num in pos:
            target = (num-k)%modulo
            while target < 0:
                target += modulo
            ans += count[target]
            count[num%modulo] += 1
        return ans