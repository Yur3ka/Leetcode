class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_1 = floor(n/2)
        odd_2 = floor(m/2)
        even_1 = n-odd_1
        even_2 = m-odd_2
        return odd_1*even_2 + odd_2*even_1