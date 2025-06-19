class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        item = sorted(list(set(nums)))
        used = set()
        ans = 0
        for i in range(len(item)):
            if item[i] in used:
                continue
            else:
                ans += 1
                used.add(item[i])
                for j in range(i+1,len(item)):
                    if item[j]-item[i] > k:
                        break
                    used.add(item[j])
        return ans