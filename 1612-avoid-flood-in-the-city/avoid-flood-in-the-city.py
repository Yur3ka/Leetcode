class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rained = set()
        ans = [1]*(len(rains))
        pos = []
        used = defaultdict(int)
        for i in range(len(rains)):
            if rains[i] == 0:
                pos.append(i)
            else:
                # print(used)
                if rains[i] not in used:
                    ans[i] = -1
                    used[rains[i]] = i
                else:
                    idx = bisect_left(pos,used[rains[i]])
                    if idx >= len(pos):
                        return []
                    else:
                        ans[pos[idx]] = rains[i]
                        pos.pop(idx)
                        used[rains[i]] = i
                        ans[i] = -1
        return ans