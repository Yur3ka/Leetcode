class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def get_heigh(pos):
            ans = 0
            curr = 1
            while curr < pos:
                curr *= 2
                ans += 1
            return ans

        def get_char(pos):
            if pos == 1:
                return 0
            h = get_heigh(pos)
            return get_char(pos-2**(h-1)) + operations[h-1]

        ans = get_char(k)
        return chr(ord('a')+ans%26)
