class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        delta = abs(x-z) - abs(y-z)
        if delta == 0:
            return 0
        elif delta > 0:
            return 2
        else:
            return 1