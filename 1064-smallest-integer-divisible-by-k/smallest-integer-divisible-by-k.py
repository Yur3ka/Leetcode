class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()
        ans = 1
        curr = 1 % k
        while curr not in seen:
            if curr == 0:
                return ans
            seen.add(curr)
            curr = (curr*10+1)%k
            ans += 1
        return -1