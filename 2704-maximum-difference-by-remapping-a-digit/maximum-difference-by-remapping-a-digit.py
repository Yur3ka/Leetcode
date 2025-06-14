class Solution:
    def minMaxDifference(self, num: int) -> int:
        ln = [int(x) for x in str(num)]
        first_min = ln[0]
        first_max = 9
        for n in ln:
            if n < first_max:
                first_max = n
                break
        maxi = 0
        mini = 0
        for n in ln:
            if n == first_min:
                mini = mini*10
            else:
                mini = mini*10 + n
        for n in ln:
            if n == first_max:
                maxi = maxi*10+9
            else:
                maxi = maxi*10 + n
        return maxi - mini
        