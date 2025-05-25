class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = defaultdict(int)
        for move in moves:
            count[move] += 1
        return count['L'] == count['R'] and count['U'] == count['D']
        