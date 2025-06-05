class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        queue = [(0,0)]
        while queue:
            i, bit = queue.pop(0)
            if i > n:
                break
            ans[i] = bit
            small = i << 1
            large = (i << 1) + 1
            if small != 0:
                queue.append((small,bit))
            queue.append((large,bit+1))
        return ans