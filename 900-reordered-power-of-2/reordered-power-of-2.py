class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        string_n = list(str(n))
        c = Counter(string_n)
        string_n.sort()
        low = int(''.join(string_n))
        string_n.reverse()
        high = int(''.join(string_n))
        low_idx = floor(log2(low))
        high_idx = ceil(log2(high))
        for i in range(low_idx,high_idx+1):
            count = Counter(str(2**i))
            if count == c:
                return True
        return False