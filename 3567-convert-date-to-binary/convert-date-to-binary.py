class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def dec_to_bin(n):
            return bin(n)[2:]
        d = date.split('-')
        ans = []
        for num in d:
            ans.append(dec_to_bin(int(num)))
        return '-'.join(ans)