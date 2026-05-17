class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit = set()
        n = len(arr)
        stack = [start]
        while stack:
            curr = stack.pop()
            if curr in visit:
                continue
            if arr[curr] == 0:
                return True
            visit.add(curr)
            if curr + arr[curr] < n:
                stack.append(curr + arr[curr])
            if curr - arr[curr] > -1:
                stack.append(curr - arr[curr])
        return False