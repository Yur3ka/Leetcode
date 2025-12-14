class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        ans = 1
        seats = 0
        curr = 0
        for i in range(len(corridor)):
            if corridor[i] == 'P':
                if seats %2 == 0 and seats != 0:
                    curr += 1
            else:
                seats += 1
                if seats % 2 == 1 and seats > 2:
                    ans *= curr + 1
                    ans %= MOD
                else:
                    curr = 0
        if seats %2 == 1 or seats < 2:
            return 0
        return ans