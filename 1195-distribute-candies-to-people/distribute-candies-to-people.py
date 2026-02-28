class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0]*num_people
        turn = 0
        while candies > 0:
            distribute = min(candies, turn+1)
            ans[turn%num_people] += distribute
            candies -= distribute
            turn += 1 
        return ans