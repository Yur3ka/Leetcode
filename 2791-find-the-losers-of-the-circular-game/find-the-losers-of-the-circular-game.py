class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        ans = []
        received = set()
        i = 0
        curr = 0
        while True:
            if (i+1) not in received:
                received.add(i+1)
                curr += 1
                i = (i + curr*k)%n
            else:
                break
        for i in range(1,n+1):
            if i not in received:
                ans.append(i)
        return ans