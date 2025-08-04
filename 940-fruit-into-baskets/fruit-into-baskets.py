class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        types = set()
        fruits_count = defaultdict(int)
        curr = 0
        left = 0
        for i in range(len(fruits)):
            curr += 1
            fruits_count[fruits[i]] += 1
            types.add(fruits[i])
            if len(types) <= 2:
                ans = max(ans,curr)
            else:
                while len(types) > 2:
                    fruits_count[fruits[left]] -= 1
                    curr -= 1
                    if fruits_count[fruits[left]] == 0:
                        types.remove(fruits[left])
                    left += 1
        return ans