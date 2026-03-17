class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        heap = []
        for i in range(n):
            heappush(heap,[i,i])
        deck.sort()
        ans = [-1]*n
        l = 0
        while heap:
            turn, idx = heappop(heap)
            if turn %2 == 1:
                heappush(heap,[n,idx])
                n += 1
            else:
                ans[idx] = deck[l]
                l += 1
        return ans
