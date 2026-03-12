class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        remove = n//20
        return sum(arr[remove:-remove])/(n-2*remove)