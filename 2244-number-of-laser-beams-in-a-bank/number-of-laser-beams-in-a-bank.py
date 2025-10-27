class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        row = []
        for i in range(len(bank)):
            curr = 0
            for char in bank[i]:
                if char == '1':
                    curr += 1
            if curr != 0:
                row.append(curr)
        ans = 0
        for i in range(len(row)-1):
            ans += row[i]*row[i+1]
        return ans