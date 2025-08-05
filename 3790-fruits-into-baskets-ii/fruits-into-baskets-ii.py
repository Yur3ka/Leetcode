class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = len(fruits)
        used = set()
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if j in used:
                    continue
                if fruits[i] <= baskets[j]:
                    ans -= 1
                    used.add(j)
                    break
        return ans